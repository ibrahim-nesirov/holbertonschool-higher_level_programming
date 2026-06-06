from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)


def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    conn.commit()
    conn.close()


def read_json():
    path = os.path.join(os.path.dirname(__file__), 'products.json')
    with open(path, 'r') as f:
        return json.load(f)


def read_csv():
    path = os.path.join(os.path.dirname(__file__), 'products.csv')
    products = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products


def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [{'id': r[0], 'name': r[1], 'category': r[2], 'price': r[3]} for r in rows]


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id:
        data = [p for p in data if p['id'] == int(product_id)]
        if not data:
            return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=data)


create_database()

if __name__ == '__main__':
    app.run(debug=False, port=5000)