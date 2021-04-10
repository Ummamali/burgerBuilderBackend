from flask import Flask, jsonify, request
from flask_cors import cross_origin
from time import sleep
from json import dumps, loads, load, dump




app = Flask(__name__)

prices = {
    'salad': 10,
    'bacon': 10,
    'cheese': 10,
    'meat': 10
}
orders = 0

@app.route('/prices')
@cross_origin()
def data_loader():
    sleep(1)
    return jsonify({'status':200, 'data':prices})

@app.route('/order', methods=('POST', ))
@cross_origin()
def order():
    req_json = request.get_json()
    if (req_json.get('token') == 2019):
        save_data(req_json['data'])
        return jsonify({'status': 200, 'id': orders - 1})
    else:
        return jsonify({'status': 401, 'msg': 'Unauthorized request.'})


def save_data(data):
    sleep(2)
    global orders
    with open('data.json', mode='r') as f:
        order_list = load(f)
    data['id'] = orders
    order_list.append(data)
    with open('data.json', mode='w') as f:
        dump(order_list, f, indent=2)
    orders += 1


if __name__ == "__main__":
    app.run(debug=True)