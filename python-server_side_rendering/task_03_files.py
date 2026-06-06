from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


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


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id:
        data = [p for p in data if p['id'] == int(product_id)]
        if not data:
            return render_template('product_display.html', error='Product not found')

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=False, port=5000)