"""
This module runs a simple Flask web application.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    """Main function.

    Returns:
        response: statistic response 200
    """
    return "OK", 200

if __name__ in "__main__":
    app.run(debug=True, port=8000)
