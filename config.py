import os

DB_FILE_NAME = 'user_fakt.db'
full_path = os.path.join(os.path.dirname(__file__), 'data')
DB_NAME = os.path.join(full_path, DB_FILE_NAME)
