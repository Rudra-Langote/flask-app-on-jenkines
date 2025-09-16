from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Allow all domains (for dev)

# Database configuration
db_config = {
    'host': 'database-1.ccd280ii2iao.us-east-1.rds.amazonaws.com',
    'user': 'root',
    'password': 'rudraaws295',
    'database': 'std',
    'port': 3306
}

@app.route('/api', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        address = request.form['address']
        contact = request.form['contact']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = '''
        INSERT INTO students (name, email, phone, course, address, contact)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        values = (name, email, phone, course, address, contact)

        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "Student Registered Successfully!"})

    # GET request
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(students)


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)
