import os
import json
import uuid
from datetime import datetime
from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.utils import secure_filename
from .form import DVForm
from app.utils import config
from app.services import db_helper

app = Flask(__name__)

DataBase = db_helper.DatabaseService()

logger = config.setup_logger(__name__)

app.config['csrf_token'] = '2044e273cd16a216bf174d639eaa8b71'
# --- Configuration ---
app.config['SECRET_KEY'] = '3c036c3d251ba30f07bb6aa0ea48f294'
# Define upload folder paths relative to the app's instance folder for robustness
PHOTO_STORAGE_PATH = config.PHOTO_STORAGE
PAYMENT_STORAGE_PATH = config.PAYMENT_STORAGE
# Ensure upload directories exist
os.makedirs(PHOTO_STORAGE_PATH, exist_ok=True)
os.makedirs(PAYMENT_STORAGE_PATH, exist_ok=True)


def save_file(file_storage, upload_folder):
    """Saves a file from a FileStorage object to a specified folder with a unique name."""
    if not file_storage or not file_storage.filename:
        logger.debug("No file provided or filename is empty.")
        return None
    
    original_filename = secure_filename(file_storage.filename)
    file_extension = os.path.splitext(original_filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(upload_folder, unique_filename)
    
    logger.debug(f"Attempting to save original file '{original_filename}' as '{unique_filename}' to: {file_path}")

    try:
        file_storage.save(file_path)
        logger.info(f"Successfully saved file: {file_path}")
        return file_path
    except Exception as e:
        logger.error(f"Error saving file '{original_filename}': {e}", exc_info=True)
        return None


@app.route('/apply', methods=['GET', 'POST'])
def apply():
    form = DVForm()
    if request.method == 'GET':
        chat_id_from_url = request.args.get('chat_id')
        
        if chat_id_from_url:
            DataBase.start()
            if DataBase.search_user(chat_id_from_url) == None:
                DataBase.end()
                return render_template('invalid_access.html'), 403
            
            # Case 1: Initial visit with chat_id in URL. Store it and redirect.
            session['chat_id'] = chat_id_from_url
            # REDIRECT to the clean URL /apply without the parameter (hides it from the user)
            
            return redirect(url_for('apply')) 
        
        chat_id_from_session = session.get('chat_id')
        if not chat_id_from_session:
            # Case 2: No chat_id in URL AND no chat_id in session. Unauthorized access.
            return render_template('invalid_access.html'), 403
        
        # Case 3: Redirected visit or returning user with chat_id in session.
        # Pass the chat_id from the session to the form object for rendering the hidden field.
        form.chat_id.data = chat_id_from_session
        return render_template('index.html', title='Registry', form=form)
    try:
        if form.validate_on_submit():
            logger.info("Form validation successful. Starting data collection.")
            
            # Retrieve the chat_id from the submitted form data (hidden field)
            chat_id = form.chat_id.data
            
            # Clear chat_id from session after successful submission to prevent accidental re-use
            session.pop('chat_id', None)
            
            # --- Data Collection ---
            # ADDED: Start data with chat_id
            data_to_save = {'chat_id': chat_id}
            
            for field in form:
                # SKIP: chat_id is already handled above
                if field.name == 'chat_id': continue

                if field.type not in ['CSRFTokenField', 'FieldList', 'FormField']:
                    if field.type == 'FileField':
                        upload_folder = PAYMENT_STORAGE_PATH if 'payment' in field.name else PHOTO_STORAGE_PATH
                        logger.debug(f"Processing file field '{field.name}' for upload to '{upload_folder}'.")
                        saved_path = save_file(field.data, upload_folder)
                        data_to_save[field.name] = saved_path
                    else:
                        data_to_save[field.name] = field.data
            
            # Handle children separately
            children_data = []
            if form.children.data:
                logger.info(f"Processing {len(form.children.data)} children entries.")
                for i, child_form_data in enumerate(form.children.data):
                    child_data = {}
                    for key, value in child_form_data.items():
                        if key == 'csrf_token': continue
                        if key == 'photo' and form.children[i].photo.data:
                            logger.debug(f"Processing photo for child {i+1}.")
                            child_photo_path = save_file(form.children[i].photo.data, PHOTO_STORAGE_PATH)
                            child_data['photo_path'] = child_photo_path
                        elif key != 'photo':
                            child_data[key] = value
                    children_data.append(child_data)
            data_to_save['children'] = children_data

            # --- Save to JSON File ---
            # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # json_filename = f'application_{timestamp}.json'
            # json_filepath = os.path.join(os.path.dirname(__file__), json_filename)
            
            # logger.info(f"Saving collected data to JSON file: {json_filepath}")
            # with open(json_filepath, 'w') as f:
            #     json.dump(data_to_save, f, indent=4, default=str) # Use default=str for non-serializable data

            DataBase.start()
            DataBase.submit_family_application(data_to_save)
            DataBase.end()

            logger.info("Successfully saved application data to database(maybe json)")

            return render_template('success.html')
    
        if form.errors:
            logger.warning("Form validation failed.")
            for field, errors in form.errors.items():
                # Check if the error is a list of strings (standard field)
                if isinstance(errors, list) and all(isinstance(e, str) for e in errors):
                    logger.warning(f"Field '{field}': {', '.join(errors)}")
                else:
                    # It's a nested error (like from children FieldList), just log it directly
                    logger.warning(f"Field '{field}': {errors}")
            
    except Exception as e:
        logger.error("An unexpected error occurred in the apply view.", exc_info=True)
        return render_template('500.html', error=e), 500

    return render_template('index.html', title='Registry', form=form)

def flask_run():
    logger.info('flask app starts running')
    app.run(debug=True)
    logger.info('flask app stops running')