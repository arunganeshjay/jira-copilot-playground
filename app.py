from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200


@app.route("/add", methods=["POST"])
def add():
    """Add two numbers."""
    data = request.get_json()
    a, b = _parse_numbers(data)
    return jsonify({"operation": "addition", "a": a, "b": b, "result": a + b}), 200


@app.route("/subtract", methods=["POST"])
def subtract():
    """Subtract two numbers."""
    data = request.get_json()
    a, b = _parse_numbers(data)
    return jsonify({"operation": "subtraction", "a": a, "b": b, "result": a - b}), 200


@app.route("/multiply", methods=["POST"])
def multiply():
    """Multiply two numbers."""
    data = request.get_json()
    a, b = _parse_numbers(data)
    return jsonify({"operation": "multiplication", "a": a, "b": b, "result": a * b}), 200


@app.route("/divide", methods=["POST"])
def divide():
    """Divide two numbers."""
    data = request.get_json()
    a, b = _parse_numbers(data)
    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    return jsonify({"operation": "division", "a": a, "b": b, "result": a / b}), 200


def _parse_numbers(data):
    """Extract and validate two numbers from the request payload."""
    if data is None:
        raise ValueError("Request body must be JSON")
    a = data.get("a")
    b = data.get("b")
    if a is None or b is None:
        raise ValueError("Both 'a' and 'b' are required")
    return float(a), float(b)


@app.errorhandler(ValueError)
def handle_value_error(error):
    return jsonify({"error": str(error)}), 400


@app.errorhandler(400)
def handle_bad_request(error):
    return jsonify({"error": "Bad request"}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)
