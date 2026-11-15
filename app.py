from flask import Flask, jsonify, render_template, request
import json
from pymongo import MongoClient
 
app = Flask(__name__)
client = MongoClient('mongodb+srv://vyfrost8_db_user:sTa6b4ay3WFglFWh@cluster0.ajisasq.mongodb.net')
db = client['todo_db']
collection = db['todo_items']

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.form if request.form else (request.get_json(silent=True) or {})
    item = {
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    }
    collection.insert_one(item.copy())
    return jsonify({"message": "Item stored", "item": item}), 201

 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/api')
def api():
    with open('data.json') as f:
        return jsonify(json.load(f))
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

