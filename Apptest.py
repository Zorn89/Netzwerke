from flask import Flask

app = Flask(__name__)


# GET route
@app.route("/")
def home():
    return "Hello, World! This is a simple API running on Mac."


@app.route("/test")
def test_func():
    return "Test!!!"


@app.route("/max")
def max_func():
    return "MAX!!!"

@app.route("/zorn")
def zorn_func():
    return "Der Zorn ist da"

# Run the app
if __name__ == "__main__":
    # Use a custom port (e.g., 8080) and bind to all interfaces
    app.run(debug=True, host="0.0.0.0", port=6060)