from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My wonderful store',
        'items': [
            {
            'name': 'My Item',
            'price': 7.99
            }
        ]
    }
]

#POST : is used to recieve the data
#GET: is used to send data back only

@app.route("/")
def home():
    return render_template('index.html')

#POST /store data : {'name': }
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route("/store/<string:name>")   #default GET
def get_store(name):
    #iterate over stores
    #if the name matches return that store
    #if none matches return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(stores)
    return "Store doesn't exist"

#GET /store
@app.route("/store")
def get_stores():
    return jsonify({'stores':stores})

#POST /store/<string:name>/item {name: , price: }
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found'})

#GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'item': store['items']})
    return jsonify({'message': 'No item found of this name'})



app.run(port=5000)
