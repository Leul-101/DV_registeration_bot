import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool
from app.utils import config

logger = config.setup_logger(__name__)

try:
    db_pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="bot_pool",
        pool_size=5,
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )
    logger.info("Database connection pool created successfully.")
except Exception as e:
    logger.error(f"Failed to create connection pool: {e}")
    pool = None

class DatabaseService:
    """
    Handles every interaction between the code and the database.
    -after making a connection it can be use through out the program
    """
    def __init__(self):
        """Initializes the DatabaseService, setting the path to the database file."""
        pass
    def start(self):
        """Establishes a connection to the SQLite database and creates a cursor."""
        try:
            self.conn = db_pool.get_connection() 
            self.cursor = self.conn.cursor(buffered=True)

            logger.info('connected with the database successfully')
        except Exception as e:
            logger.error(f"failed to connect with the database: {e}")

    def end(self):
        """Closes the connection to the database."""
        if self.conn and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
        logger.info('database conection is closed')

    def execute(self,sql_code: str, process_name: str) -> bool:
        """
        Executes a given SQL command and commits the changes.

        Args:
            sql_code (str): The SQL query to execute.
            process_name (str): A descriptive name for the operation, used for logging.

        Returns:
            bool: True if the execution was successful, False otherwise.
        """
        if self.conn:
            try:
                self.cursor.execute(sql_code)
                self.conn.commit()
                return True
            except Exception as e:
                logger.error(f"data {process_name} failed: {e}")
        else:
            logger.warning(f"there is no connection with the database")
        return False

    def _insert(self, table: str, columns_list: tuple, values_list: tuple) -> bool:
        """
        this method will handle the insertion opration
        -tabele paramater will accept the table name
        -columns_list will take the the colums where data will be inserted
        -values_list will take the values for the columns respectivlly
        """
        column_list_str = ', '.join(columns_list)
        
        sql_code = f"INSERT INTO {table} ({column_list_str}) VALUES {values_list};"
        return self.execute(sql_code, "insertion")

    def _select(self, table: str,  key: str) -> list | None:
        """
        will and return the result in a list using fetchall()
        -table will take tabele name
        -key is a condition to select the rows
        """
        sql_code = f"SELECT * FROM {table} WHERE {key};"
        if self.execute(sql_code, "selection"):
            return self.cursor.fetchall()
        return None

    def _delete(self, table: str,  key: str)  -> int:
        """
        will and delete the specified row
        -table will take tabele name
        -key is a condition to delete the rows
        """
        sql_code = f"DELETE FROM {table} WHERE {key};"
        return self.execute(sql_code, "deletion")

    def _update(self, table: str, set: str, key: str)  -> int:
        """
        will updates data from a table
        -tabele will take a table name
        -set is the changed columns along with there value with the pattern:-
        column1=value, column2=value
        -key is a condition to identify the rows 
        """
        sql_code = f"UPDATE {table} SET {set} WHERE {key};"
        return self.execute(sql_code, "update")
    
    #methods for data insertion

    def insert_user(self, name: str, lang: str, chat_id: int) -> bool:
        if self._insert('BotUsers', ('ChatID', 'TgName', 'Lang'), (chat_id, name, lang)):
           logger.info(f"new user with chat id {chat_id} starts the bot")
           return True
        else:
           logger.warning(f"failed to create user account for {chat_id}")
           return False
    def insert_agent(self, user_id: int, name: str, phone: str, bank: int) -> bool:
        if self._insert('Agent', ('UserID', 'AgentName', 'PhoneNumber', 'BankAccount'), (user_id, name, phone, bank)):
           logger.info(f"new agent with chat id {user_id} starts the bot")
           return True
        else:
           logger.warning(f"failed to create agent account for {user_id}")
           return False
    #methods for searching data
    def _fetch_data(self,table: str, column: str, id: int, fetch: str = 'one') -> list | tuple | None:
        """
        A generic helper to fetch data from a table based on a column-value pair.

        Args:
            table (str): The name of the table to fetch from.
            column (str): The name of the column to use in the WHERE clause.
            id (int): The value to match in the specified column.
            fetch (str, optional): 'one' to fetch a single record, 'all' to fetch all matching records. Defaults to 'one'.

        Returns:
            list | tuple | None: A tuple for a single record, a list of tuples for multiple records, or None if not found.
        """
        data = self._select(table, f"{column}={id}")
        if type(data) == list and data != []:
            logger.debug(f"{table} data  with id {id} is retrieved")
            if fetch == 'one':
                return data[0]
            if fetch == 'all':
                return data
        logger.warning(f"{table} with id {id} is not found or some thing is wrong")
        return None
    def search_user(self, chat_id: int) -> tuple | None:
        return self._fetch_data('BotUsers', 'chatID', chat_id)
    def search_agent(self, chat_id: int) -> tuple | None:
        user = self.search_user(chat_id)
        if user == None:
            return None
        return self._fetch_data('Agent', 'UserID', user[0])
    def update_lang(self, chat_id: int, lang: str) -> None:
        try:
            self._update('BotUsers', f"Lang='{lang}'", f'ChatID={chat_id}')
            logger.debug(f'language updated for {chat_id}')
        except Exception as e:
            logger.error(f'failed to update language for {chat_id}')
    def update_role(self, chat_id: int, role: str) -> None:
        try:
            self._update('BotUsers', f"UserRole='{role}'", f'ChatID={chat_id}')
            logger.debug(f'role updated for {chat_id}')
        except Exception as e:
            logger.error(f'failed to update role for {chat_id}: {e}')
    def update_payment(self, code: int, status: str) -> None:
        try:
            self._update('Applications', f"PaymentStatus='{status}'", f"PaymentPath LIKE '%{code}%'")
            logger.debug(f'payment updated for {code}')
        except Exception as e:
            logger.error(f'failed to update payment for {code}: {e}')
    def update_register(self, app_id: int, status: str) -> None:
        try:
            self._update('Applications', f"RegisterStatus='{status}'", f"ApplicationID='{app_id}'")
            logger.debug(f'registeration status updated for {app_id}')
        except Exception as e:
            logger.error(f'failed to update registeration status for {app_id}: {e}')
    def search_appliction(self, code: str) -> None | tuple:
        try:
            result = self._select('Applications',
                                  f"PaymentPath LIKE '%{code}%'")
            if result != None:
                logger.debug(f'app search found for {code}')
                return result[0]
            else:
                logger.debug(f'app search not found for {code}')
                return None
        except Exception as e:
            logger.error(f'failed to search app {code}: {e}')
    def submit_application(self,
                    user_id: int,
                    full_name: str,
                    gender: str,
                    birth_date: str,
                    birth_city: str,
                    current_city: str,
                    phone: str,
                    email: str,
                    education: str,
                    marital_status: str,
                    photo_path: str,
                    payment_path: str
                    ) -> bool:

        if self._insert('Applications',
                        (
                            'UserID',
                            'FullName',
                            'Gender',
                            'BirthDate',
                            'BirthCity',
                            'CurrentCity',
                            'PhoneNumber',
                            'Email',
                            'Education',
                            'MaritalStatus',
                            'PhotoPath',
                            'PaymentPath',
                            ),
                        (
                            user_id,
                            full_name,
                            gender,
                            birth_date,
                            birth_city,
                            current_city,
                            phone,
                            email,
                            education,
                            marital_status,
                            photo_path,
                            payment_path
                            )):
           logger.info(f"new application created by {user_id}")
           return True
        else:
           logger.warning(f"failed to create application for {user_id}")
           return False