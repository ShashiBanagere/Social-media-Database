import mysql.connector

def execute_query(query, params=None, fetch=False):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rasha123",
        database="social_media"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params)
    if fetch:
        result = cursor.fetchall()
    else:
        conn.commit()
        result = None
    cursor.close()
    conn.close()
    return result

def get_user_id(username):
    query = "SELECT id FROM users WHERE username = %s"
    result = execute_query(query, (username,), fetch=True)
    if result:
        return result[0]['id']
    return None

def get_username(user_id):
    query = "SELECT username FROM users WHERE id = %s"
    result = execute_query(query, (user_id,), fetch=True)
    if result:
        return result[0]['username']
    return None

def like_image(user_id, image_id):
    username = get_username(user_id)
    
    # Check if the user already liked the image
    query = "SELECT * FROM likes WHERE user_id = %s AND image_id = %s"
    result = execute_query(query, (user_id, image_id), fetch=True)
    if result:
        return "already_liked"

    # Insert like into the database
    query = "INSERT INTO likes (user_id, image_id, username, like_count) VALUES (%s, %s, %s, %s)"
    execute_query(query, (user_id, image_id, username, 1))

    return "liked"

def get_like_count(image_id):
    query = "SELECT COUNT(*) AS like_count FROM likes WHERE image_id = %s"
    result = execute_query(query, (image_id,), fetch=True)
    if result:
        return result[0]['like_count'] or 0
    return 0

def comment_on_image(user_id, image_id, comment):
    username = get_username(user_id)
    query = "INSERT INTO comments (user_id, image_id, comment, username) VALUES (%s, %s, %s, %s)"
    execute_query(query, (user_id, image_id, comment, username))

def get_comments(image_id):
    query = """
    SELECT username, comment FROM comments
    WHERE image_id = %s
    ORDER BY id DESC
    """
    comments = execute_query(query, (image_id,), fetch=True)
    return comments

def check_user_credentials(username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    result = execute_query(query, (username, password), fetch=True)
    return len(result) > 0

def insert_user(username, password, first_name, last_name):
    query = "INSERT INTO users (username, password, first_name, last_name) VALUES (%s, %s, %s, %s)"
    execute_query(query, (username, password, first_name, last_name))

def username_exists(username):
    query = "SELECT * FROM users WHERE username = %s"
    result = execute_query(query, (username,), fetch=True)
    return len(result) > 0
