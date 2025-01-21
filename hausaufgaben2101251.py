# Aufgabe 2: Flask-App mit Nutzeraktionen (100 Pkunkte)

# Ziel: Erstelle eine Flask-App, die auf GET-Routen reagiert und verschiedene Nutzeraktionen
# simuliert.
# Beschreibung:
# Hintergrund: Du hast eine Liste von Nutzern mit id, name und email:
# users = [

# {"id": 1, "name": "Alice", "email": "alice@example.com"},
# {"id": 2, "name": "Bob", "email": "bob@example.com"},
# {"id": 3, "name": "Charlie", "email": "charlie@example.com"}

# ]

# 1. Erstelle eine Flask-App mit den folgenden Routen:
# ○ Route 1: /user/<id>
# Beispiel: http://localhost:6060/user/1
# Rückgabe: Nutzerdetails wie {"id": 1, "name": "Alice", "email":
# "alice@example.com"}
# ○ Route 2: /login/<id>
# Beispiel: http://localhost:6060/login/2
# Rückgabe: "User Bob successfully logged in!" (oder Fehler, falls ID nicht
# existiert)
# ○ Route 3: /search?name=<name>
# Beispiel: http://localhost:6060/search?name=Charlie
# Rückgabe: "Found user: Charlie" oder "No user found with name: Charlie"

# 2. Extras:
# ○ Validiere, ob die User-ID oder der Name existiert. Falls nicht, gib eine
# passende Fehlermeldung aus.
# ○ Formatiere die Antworten als JSON.
# 3. Teste die App mit Postman oder deinem Browser.

# Abgabe:
# ● Eine funktionierende Flask-App, die auf Port 6060 läuft.
# ● Eine Datei users.py mit der Liste der Nutzer.
# ● Klar definierte Routen mit JSON-Ausgab 

from flask import Flask, request, jsonify
from users import users  
app = Flask(__name__)

# Route 1: /user/<id> - Nutzerdetails zurückgeben
@app.route('/user/<int:id>', methods=['GET'])
def user(id):
    # Suche nach dem Nutzer mit der gegebenen ID
    user = next((user for user in users if user["id"] == id), None)
    if user:
        return jsonify(user)  # Gibt die Nutzerdetails als JSON zurück
    else:
        return jsonify({"error": "User not found"}), 404  # Fehler, wenn der Nutzer nicht gefunden wird

# Route 2: /login/<id> - Nutzer einloggen
@app.route('/login/<int:id>', methods=['GET'])
def login(id):
    # Suche nach dem Nutzer mit der gegebenen ID
    user = next((user for user in users if user["id"] == id), None)
    if user:
        return jsonify({"message": f"User {user['name']} successfully logged in!"})  # Erfolgreiche Anmeldung
    else:
        return jsonify({"error": "User not found"}), 404  # Fehler, wenn der Nutzer nicht gefunden wird

# Route 3: /search?name=<name> - Nach Nutzernamen suchen
@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name')
    # Suche nach dem Nutzer mit dem angegebenen Namen
    user = next((user for user in users if user["name"].lower() == name.lower()), None)
    if user:
        return jsonify({"message": f"Found user: {user['name']}"})  # Benutzer gefunden
    else:
        return jsonify({"error": f"No user found with name: {name}"}), 404  # Benutzer nicht gefunden

if __name__ == '__main__':
    app.run(debug=True, port=6060)