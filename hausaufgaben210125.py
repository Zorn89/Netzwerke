# Aufgabe 1
#Erstelle eine Flask-App mit mindestens drei GET-Endpunkten.
#2. Die GET-Anfragen sollen unterschiedliche Funktionen ausführen:
# ○ Route 1: /brand/<id>?type=<type>&condition=<condition>
# ■ Beispiel: http://localhost:6060/brand/10?type=clothes&condition=new
# ■ Ausgabe: "Brand-ID: 10, Type: clothes, Condition: new"
# ○ Route 2: /product/<product_id>
# ■ Beispiel: http://localhost:6060/product/123
# ■ Ausgabe: "Product-ID: 123"
# ○ Route 3: /search
# ■ Beispiel: http://localhost:6060/search?query=shoes
# ■ Ausgabe: "Searching for: shoes" 

from flask import Flask, request

app = Flask(__name__)

# Route 1: /brand/<id>?type=<type>&condition=<condition>
@app.route('/brand/<int:id>')
def brand(id):
    type = request.args.get('type')
    condition = request.args.get('condition')
    return f"Brand-ID: {id}, Type: {type}, Condition: {condition}"

# Route 2: /product/<product_id>
@app.route('/product/<int:product_id>')
def product(product_id):
    return f"Product-ID: {product_id}"

# Route 3: /search
@app.route('/search')
def search():
    query = request.args.get('query')
    return f"Searching for: {query}"

if __name__ == '__main__':
    app.run(debug=True, port=6060)