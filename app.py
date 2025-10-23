from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify(message="Hello!"), 200

if __name__ == '__main__':
    app.run(debug=True)