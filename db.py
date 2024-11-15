import mysql.connector
from mysql.connector import Error

class UserDatabase:
    def __init__(self):
        try:
            # db config
            self.connection = mysql.connector.connect(
                host='localhost',
                database='db',
                user='root',
                password='root'
            )  
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
        except Error as e:
            print(f"connection error: {e}")


    # Create
    def create_user(self, name, user_name):
        try:
            insert_query = """
            INSERT INTO user (name, user_name)
            VALUES (%s, %s)
            """
            self.cursor.execute(insert_query, (name, user_name))
            self.connection.commit()
            print("create success")
            return self.cursor.lastrowid
        except Error as e:
            print(f"create failure: {e}")
            return None

    # Retrieve by user_id
    def get_user_by_id(self, user_id):
        try:
            select_query = "SELECT * FROM user WHERE id = %s"
            self.cursor.execute(select_query, (user_id,))
            user = self.cursor.fetchone()
            return user
        except Error as e:
            print(f"retrieve error: {e}")
            return None

    # Retrieve all
    def get_all_users(self):
        try:
            select_query = "SELECT * FROM user"
            self.cursor.execute(select_query)
            users = self.cursor.fetchall()
            return users
        except Error as e:
            print(f"retrieve all error: {e}")
            return None

    # Update
    def update_user(self, user_id, name=None, user_name=None):
        try:
            update_parts = []
            values = []
            
            if name is not None:
                update_parts.append("name = %s")
                values.append(name)
            if user_name is not None:
                update_parts.append("user_name = %s")
                values.append(user_name)
                
            if not update_parts:
                return False
                
            values.append(user_id)
            update_query = f"""
            UPDATE user 
            SET {', '.join(update_parts)}
            WHERE id = %s
            """
            
            self.cursor.execute(update_query, tuple(values))
            self.connection.commit()
            print("update success")
            return True
        except Error as e:
            print(f"update failure: {e}")
            return False

    # Delete
    def delete_user(self, user_id):
        try:
            delete_query = "DELETE FROM user WHERE id = %s"
            self.cursor.execute(delete_query, (user_id,))
            self.connection.commit()
            print("delete success")
            return True
        except Error as e:
            print(f"delete failure: {e}")
            return False


# demo
if __name__ == "__main__":
    db = UserDatabase()

    # create
    new_user_id = db.create_user("Edison", "Edison")
    print(f"user_id: {new_user_id}")

    # retrieve
    #user = db.get_user_by_id(1)
    #print(f"user info: {user}")

    # retrieve all
   # all_users = db.get_all_users()
   # print(f"all user info: {all_users}")

    # udpate
    #db.update_user(4, name="Edward", user_name="Edward")

    # delete
    #db.delete_user(4)
