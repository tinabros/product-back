from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db_connection():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host="localhost",      # Your MySQL server host
        user="root",  # Your MySQL username
        password="",  # Your MySQL password
        database="shop"        # Database name
    )
    return conn

@app.route('/products', methods=['GET'])
def get_all_products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tblproduct')
    products = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tblproduct WHERE product_id = %s', (product_id,))
    product = cursor.fetchone()
    cursor.close()
    conn.close()

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product)

if __name__ == '__main__':
    app.run(debug=True)

