from flask_wtf import FlaskForm
from wtforms import (
    StringField, SelectField, IntegerField, FieldList, FormField
)
from wtforms.validators import DataRequired, Email, Optional
from flask_wtf.file import FileField, FileAllowed


# --------------------------
# CHILD FORM (for each kid)
# --------------------------
class ChildForm(FlaskForm):
    class Meta:
        csrf = False
    name = StringField("Child full name", validators=[Optional()])
    gender = SelectField(
        "Gender",
        choices=[("", "--"), ("male", "Male"), ("female", "Female")],
        validators=[Optional()]
    )
    day = SelectField("Day", choices=[("", "Day")] + [(str(i), str(i)) for i in range(1, 32)], validators=[Optional()])
    month = SelectField("Month", choices=[("", "Month")] + [(str(i), str(i)) for i in range(1, 13)], validators=[Optional()])
    year = SelectField("Year", choices=[("", "Year")] + [(str(i), str(i)) for i in range(1980, 2030)], validators=[Optional()])
    city = StringField("Child birth city", validators=[Optional()])
    country = StringField("Child birth country", validators=[Optional()])
    photo = FileField(
        "Child passport-style photo",
        validators=[
            Optional(),
            FileAllowed(["jpg", "jpeg"], "JPEG or JPG only.")
        ]
    )


# --------------------------
# MAIN DV LOTTERY FORM
# --------------------------
class DVForm(FlaskForm):

    # ADDED: Hidden field to carry the chat_id from the URL to the POST request
    chat_id = StringField('Chat ID', validators=[DataRequired()])

    # A. Personal Information
    fullName = StringField("Full Name", validators=[DataRequired()])
    gender = SelectField(
        "Gender",
        choices=[("", "-- Select gender --"), ("male", "Male"), ("female", "Female")],
        validators=[DataRequired()]
    )

    day = SelectField("Day", choices=[("", "Day")] + [(str(i), str(i)) for i in range(1, 32)], validators=[DataRequired()])
    month = SelectField("Month", choices=[("", "Month")] + [(str(i), str(i)) for i in range(1, 13)], validators=[DataRequired()])
    year = SelectField("Year", choices=[("", "Year")] + [(str(i), str(i)) for i in range(1950, 2025)], validators=[DataRequired()])

    birthCity = StringField("Birth City", validators=[DataRequired()])
    birthCountry = StringField("Birth Country", validators=[DataRequired()])

    photo = FileField(
        "Applicant Photo",
        validators=[
            DataRequired(),
            FileAllowed(["jpg", "jpeg"], "Must be JPG/JPEG")
        ]
    )

    # B. Contact Info
    region = StringField("Region", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    district = StringField("District", validators=[DataRequired()])
    phone = StringField("Phone", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])

    # C. Education
    education = SelectField(
        "Education",
        choices=[
            ("", "-- Select education --"),
            ("primary", "Primary school"),
            ("high_only", "High school only"),
            ("high_deg", "High school degree"),
            ("some_uni", "Some university"),
            ("grad_course", "Graduate-level course"),
            ("uni_deg", "University degree"),
            ("masters", "Master’s degree"),
            ("phd", "Doctorate degree"),
        ],
        validators=[DataRequired()]
    )

    # D. Marital Status
    marital = SelectField(
        "Marital Status",
        choices=[
            ("", "-- Select --"),
            ("unmarried", "Unmarried"),
            ("married", "Married"),
            ("divorced", "Divorced"),
            ("widowed", "Widowed"),
            ("legally_separated", "Legally Separated"),
        ],
        validators=[DataRequired()]
    )

    # Spouse info (optional)
    spouseName = StringField("Spouse Name", validators=[Optional()])
    spouseDay = SelectField("Spouse Day", choices=[("", "Day")] + [(str(i), str(i)) for i in range(1, 32)], validators=[Optional()])
    spouseMonth = SelectField("Spouse Month", choices=[("", "Month")] + [(str(i), str(i)) for i in range(1, 13)], validators=[Optional()])
    spouseYear = SelectField("Spouse Year", choices=[("", "Year")] + [(str(i), str(i)) for i in range(1950, 2025)], validators=[Optional()])
    spouseCity = StringField("Spouse Birth City", validators=[Optional()])
    spouseCountry = StringField("Spouse Birth Country", validators=[Optional()])
    spousePhoto = FileField(
        "Spouse Photo",
        validators=[Optional()]
    )

    # E. Children
    hasChildren = SelectField(
        "Has Children?",
        choices=[("", "-- Select --"), ("yes", "Yes"), ("no", "No")],
        validators=[DataRequired()]
    )
    childrenCount = SelectField(
        "Number of Children",
        choices=[("", "-- Select --")] + [(str(i), str(i)) for i in range(1, 11)],
        validators=[Optional()]
    )

    # Dynamic children entries
    children = FieldList(FormField(ChildForm), min_entries=0)

    # F. Payment Verification
    payment = FileField(
        "Payment Screenshot",
        validators=[
            DataRequired(),
            FileAllowed(["jpg", "jpeg", "png"], "Images only.")
        ]
    )
