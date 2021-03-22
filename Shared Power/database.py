import hashlib
import datetime

import sqlite3
from sqlite3 import Error


class DatabaseManager:

#___________________________________________________________________________________
#    Database Instance
#___________________________________________________________________________________

    __dbclass_instance = None
    __database_name    = 'MARS.db'
    __connection_obj   = None
    __cursor_obj       = None

    def __init__(self):

        DatabaseManager.__dbclass_instance = self
        DatabaseManager.connect_database()

    @classmethod
    def getClassInstance(cls):
            return cls.__dbclass_instance


    @classmethod
    def getConnObj(cls):
            return cls.__connection_obj


    @classmethod
    def getCurObj(cls):
            return cls.__cursor_obj


    @classmethod
    def connect_database(cls):

        #db_object = self.getClassInstance()
        connection = sqlite3.connect(DatabaseManager.__database_name)
        cursor = connection.cursor()
        DatabaseManager.__connection_obj = connection
        DatabaseManager.__cursor_obj = cursor
        return connection, cursor

    def create_UserInfo_table(self):

        table = None
        try:
            table = DatabaseManager.__cursor_obj.execute('''
            CREATE TABLE UserInfo
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Email VARCHAR(25) UNIQUE NOT NULL,
            Password VARCHAR(100) NOT NULL,
            Gender CHAR(1) NOT NULL,
            Phone VARCHAR(15) NOT NULL,
            Address VARCHAR(40) NOT NULL,
            status CHAR(1) NOT NULL
            );
            ''')

        except Error as e:
            print(e)

    def create_ProdInfo_table(self):

        table = None
        try:
            table = DatabaseManager.__cursor_obj.execute('''
            CREATE TABLE ProdInfo
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tool_name VARCHAR(25) UNIQUE NOT NULL,
            owner_name VARCHAR(25) NOT NULL,
            tool_desc VARCHAR(100) NOT NULL,
            half_day_price FLOAT NOT NULL,
            full_day_price FLOAT NOT NULL,
            tool_cond VARCHAR(15) NOT NULL,
            tool_image BLOB NOT NULL,
            tool_taken INTEGER NOT NULL
            );
            ''')

        except Error as e:
            print(e)

    def create_Orders_table(self):

        table = None
        try:
            table = DatabaseManager.__cursor_obj.execute('''
            CREATE TABLE Orders
            (
            id integer PRIMARY KEY AUTOINCREMENT,
            date_hired TEXT NOT NULL,
            date_returned TEXT,
            owner_name VARCHAR(25) NOT NULL,
            tool_name VARCHAR(25) UNIQUE NOT NULL,
            user_email VARCHAR(100) NOT NULL,
            half_day_price FLOAT NOT NULL,
            full_day_price FLOAT NOT NULL,
            dispatch_service FLOAT,
            fine FLOAT NOT NULL,
            insurance FLOAT
            );
            ''')

        except Error as e:
            print(e)



    def close_connection(self):

        DatabaseManager.__connection_obj.close()
        DatabaseManager.__dbclass_instance = None

#___________________________________________________________________________________
#    UserInfo Instance
#___________________________________________________________________________________

class UserManager:


    def generate_hash_password(self, pawd):

        hashed_pwd = hashlib.sha1(bytes(pawd, 'UTF-8'))
        return hashed_pwd.hexdigest()

    def insert_registered_info(self,
                               email,
                               passw,
                               gender_selected,
                               contact,
                               address,
                               role):

        passw = self.generate_hash_password(passw)
        statement = 'INSERT INTO UserInfo \
        (Email, Password, Gender, Phone, Address, status) \
        VALUES \
        (?,?,?,?,?,?);'

        val = (email,
               passw,
               gender_selected,
               contact,
               address,
               role
        )

        conn, cur = DatabaseManager().connect_database()
        result = cur.execute(statement, val)
        conn.commit()

        if result:
            return f'{email} has been added to the system'

        else:
            return "Sorry. There was an error in database transaction."

    def insert_login_info(self, Email, pwd):

        hash_pwd = self.generate_hash_password(pwd)
        statement = 'SELECT * FROM UserInfo \
        WHERE Email = ? and Password = ?;'

        conn, cur = DatabaseManager().connect_database()
        result = cur.execute(statement, (Email,hash_pwd))

        resultset = cur.fetchone()

        if resultset is not None:
            return resultset
        else:
            return f"You have enter Either Email or Password wrong"




#___________________________________________________________________________________
#    ProdInfo Instance
#___________________________________________________________________________________


class ProductManager:

    def read_binary_file(self, filename):

        with open(filename, 'rb') as fobj:
            content = fobj.read()
            return content

    def add_tool(self,
                 tool_name,
                 username,
                 tool_desc,
                 half_day_rate,
                 full_day_rate,
                 tool_cond,
                 tool_image
                 ):

        statement = 'INSERT INTO ProdInfo \
        (tool_name, owner_name, tool_desc, half_day_price, \
        full_day_price, tool_cond, tool_image, tool_taken) \
        VALUES \
        (?,?,?,?,?,?,?,?);'

        val = (tool_name,
               username,
               tool_desc,
               half_day_rate,
               full_day_rate,
               tool_cond,
               tool_image,
               0
        )

        conn, cur = DatabaseManager().connect_database()
        result = cur.execute(statement, val)
        conn.commit()

        if result:
            return f'{tool_name} has been added to the system'

        else:
            return "Sorry. There was an error in database transaction."

    def hire_tool(self, tool_info):

        statement = 'INSERT INTO Orders \
        (date_hired, date_returned, owner_name, tool_name, user_email \
        half_day_price, full_day_price, dispatch_service, fine, insurance) \
        VALUES \
        (datetime("now"),"null",?,?,?,?,?,"null",?) \
        );'

        result = DatabaseManager.getCurObj().execute(statement, tool_info)
        if result:
            statement_prod = 'UPDATE ProdInfo \
            SET tool_taken 1 \
            WHERE tool_name=?'

            inner_result = DatabaseManager.getCurObj().execute(statement_prod, tool_info[2])
            if inner_result:
                return f'{tool_info[2]} has been hired'

            else:
                return 'Sorry there was error in database transaction'
        else:
            return 'Sorry. There was error in database transaction'


    def return_tool(self,user_email, owner_name, tool_name, halfday, fullday):

        statement = 'UPDATE Orders \
        SET date_returned = datetime("now") and fine = ? \
        WHERE user_email=? and owner_name=? and tool_name=?;'

        total_fine = Orders.calculate_fine(user_email, owner_name, tool_name, halfday, fullday)

        result = DatabaseManager.getCurObj().execute(statement, (total_fine, user_email, owner_name, tool_name))
        if result:
            statement = 'UPDATE ProdInfo \
            SET tool_taken 0 \
            WHERE owner_name=? and tool_name=?'

            inner_result = DatabaseManager.getCurObj().execute(
                statement,
                owner_name,
                tool_name
            )
            if inner_result:
                return f'{tool_info[2]} has been hired'

            else:
                return 'Sorry there was error in database transaction'
        else:
            return 'Sorry. There was error in database transaction'



class Orders:

    @staticmethod
    def generate_invoice(user_email):

        statement = 'SELECT date_hired \
        FROM Orders \
        WHERE user_email=? \
        ORDER BY date_hired DESC;'
        result = DatabaseManager.getCurObj().execute(user_email)

        if result:
            data = DatabaseManager.getCurObj().fetchone()
            date = data[0]
            month = int(date.split(" ")[0].split("-")[1])

            cur_month = datetime.date.today().month

            if cur_month != month:
                statement = 'SELECT * \
                FROM Orders \
                WHERE user_email=? ;'

                result = DatabaseManager.getCurObj().execute(user_email)
                if result is not None:
                    return result
                else:
                    return "Error in Database executing statement"

            else:
                return 'Statement will be published at the begining of new month'

        else:
            f"No data could be found for user {user_email}"

    @staticmethod
    def calculate_fine(user_email, owner_name, tool_name, halfday, fullday):
        statement_fine = 'SELECT date_hired \
        FROM Orders \
        WHERE user_email=? and owner_name=? and tool_name=?;'

        result = DatabaseManager.getCurObj().execute(statement_fine,user_email, owner_name, tool_name)
        if result:
            resultset = DatabaseManager.getCurObj().fetchone()
            if resultset is not None:
                date_hired = resultset[0]
                date_hired_date, date_hired_time = date_hired.split(' ')
                date_hired_year,date_hired_month,date_hired_day = date_hired_date.split("-")
                date_hired_hour,date_hired_min,date_hired_sec = date_hired_time.split(":")

                new_hired_date = datetime.datetime(
                    int(date_hired_year),
                    int(date_hired_month),
                    int(date_hired_day),
                    int(date_hired_hour),
                    int(date_hired_min),
                    int(date_hired_sec)
                )

                fine = float()
                current_date = datetime.datetime.now()

                diff = current_date - new_hired_date
                if diff.days > 3:
                    fine += (diff.days - 3) * fullday
                    if diff.seconds:
                        fine += halfday

            else:
                f"No data could be found for user {user_email}"

        else:
            f"No data could be found for user {user_email}"

        return fine
