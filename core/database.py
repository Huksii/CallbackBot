import psycopg2

connection = psycopg2.connect(
    host = "localhost",
    database = "test_regs",
    user = "yeraly",
    password = "123",
    port = "5432"
)

def create_table():
    with connection.cursor() as cursor:
        cursor.execute(
        "CREATE TABLE IF NOT EXISTS users(\
        id SERIAL PRIMARY KEY,\
        user_id BIGINT,\
        username VARCHAR(45) DEFAULT NULL,\
        first_name VARCHAR(255) DEFAULT NULL,\
        last_name VARCHAR(255) DEFAULT NULL,\
        phone VARCHAR(255) DEFAULT NULL,\
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
        )
    connection.commit()

def insert_users(user_id, username, first_name, last_name, phone,):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users(\
                       user_id, username, first_name, last_name, phone)\
                       VALUES(%s,%s,%s,%s,%s)",
                       (user_id, username, first_name, last_name, phone))
        connection.commit()
        

def find_user(user_id):
    with connection.cursor() as cursor:
        cursor.execute(f"select user_id from users where user_id = {user_id}")

        user = cursor.fetchone()
        return user


def pull_user(user_id):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * from users where user_id = {user_id}")
            user = cursor.fetchone()           
        u = f"""User Id: {user[1]}
        First name : {user[3]}
        last name : {user[4]}
        username : {user[2]}
        phone : {user[5]}"""         
        return u

def admin_get_users():
    with connection.cursor() as cursor:
        cursor.execute("select * from users")

        all_users = cursor.fetchall()
    info = ""
    for user in all_users:
        # print(user[[index]])
        info += f"username: {user[2]}\nPhone: {user[5]}\n\n"

    return info

# print(admin_get_users)