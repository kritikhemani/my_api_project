from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return jsonify({"message": "Hello, world!"}), 200

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"you sent": data}), 201

if __name__ == '__main__':
    app.run(debug=True)