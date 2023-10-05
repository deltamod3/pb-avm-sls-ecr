import serverless_wsgi
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from utils.predict_price import get_price

# Disable CORS
@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    header['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept'
    return response


@app.route("/", methods=["POST"])
def main_page():
    json_data = request.json
    print(json_data)

    price = float(get_price(json_data))
    return {
        "price": price,
        "data": json_data,
    }


@app.route("/status", methods=["GET"])
def status():
    return jsonify({'status': 'ok'})


if __name__ == "__main__":
    app.run(debug=True)


# We need to define handler for AWS lambda function, that is defined in Dockerfile.
def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
