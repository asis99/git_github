from flask import Flask, jsonify, render_template, request
import json
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/api')
def api():
    with open('data.json') as f:
        return jsonify(json.load(f))

@app.route('/todo')
def todo():
    return render_template('todo.html')

 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

