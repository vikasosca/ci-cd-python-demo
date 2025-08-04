from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Define a simple route
@app.route("/")
def home():
    return "<h1>Hello from Flask App!</h1><p>Welcome to CI/CD learning.</p>"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    result = a * b
    return f"<p>{a} * {b} = {result}</p>"

# This makes it runnable locally
if __name__ == "__main__":
    app.run(debug=True)
