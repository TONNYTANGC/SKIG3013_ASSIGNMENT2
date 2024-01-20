from flask import Flask, render_template, request, redirect, url_for, flash
from flask_ngrok import run_with_ngrok
# from google.colab import drive
import sqlite3
import secrets

# # Mount Google Drive
# drive.mount('/content/drive')

# Set the template and static folders
templates_folder = '/content/drive/MyDrive/SKIG3013Asg2/templates'
static_folder = '/content/drive/MyDrive/SKIG3013Asg2/static'

# Create a Flask app
app = Flask(__name__, template_folder=templates_folder, static_folder=static_folder)
app.secret_key = secrets.token_hex(32)

# Use ngrok to expose the local development server to the internet
# run_with_ngrok(app)

# db_folder = '/content/drive/MyDrive/SKIG3013Asg2'
# db_path = db_folder + '/mydatabase.db'

# SQLite database initialization
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()


# def initialize_database():
#     with sqlite3.connect(db_path) as conn:
#         cursor = conn.cursor()

#         # Query to create the 'users' table
#         create_table_query = '''
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT NOT NULL,
#             password TEXT NOT NULL
#         )
#         '''
#         cursor.execute(create_table_query)

#         # Query to insert a user if not exists
#         insert_query = '''
#         INSERT INTO users(username, password)
#         SELECT ?, ?
#         WHERE NOT EXISTS (
#             SELECT 1 FROM users WHERE username = ?
#         )
#         '''

#         user_data = ('tonny@uum.com', '67890', 'tonny')
#         cursor.execute(insert_query, user_data)
#         conn.commit()

#         # Query to select and print all users for verification
#         select_query = 'SELECT * FROM users'
#         cursor.execute(select_query)
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)

# # Initialize the database when the application starts
# initialize_database()

# Define routes
# @app.route("/", methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get("username")
#         password = request.form.get("password")

#         print(f"Received login request. Username: {username}, Password: {password}")

#         conn = sqlite3.connect(db_folder + '/mydatabase.db')
#         cursor = conn.cursor()

#         query = '''
#         SELECT * FROM users WHERE username = ? AND password = ?
#         '''

#         cursor.execute(query, (username, password))
#         result = cursor.fetchone()

#         print(f"Query Result: {result}")

#         if result:
#             # Login successful
#             logged_in_username = result[1]  # Access the username from the tuple
#             print(f"Login successful. Welcome, {logged_in_username}!")

#             return render_template("landing_page.html", username=logged_in_username)
#         else:
#             message = "WRONG USERNAME OR PASSWORD. PLEASE TRY AGAIN!"
#             print(message)  # Print error message for debugging
#             flash(message, "error")
#             return render_template('login.html', message=message)
#     else:
#         return render_template('login.html')

@app.route("/")
def base():
    return render_template("base.html")

@app.route("/landing")
def home():
    return render_template("landing_page.html")

@app.route("/main")
def main():
    return render_template("main_page.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/counts")
def counts():
    return render_template("counts.html")

@app.route("/cta")
def cta():
    return render_template("cta.html")

@app.route("/portfolio")
def portfolio_page():
    return render_template("portfolio_page.html")

@app.route("/hobby")
def hobby():
    return render_template("hobby_page.html")

@app.route("/help_contact")
def help_contact():
    return render_template("help_contact_page.html")

# Run the app
if __name__ == "__main__":
    app.run()





