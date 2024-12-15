from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['nasa_english']
collection = db['users']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        collection.insert_one({"name": name, "email": email, "phone": phone})
        return jsonify({"message": "Data saved successfully!"}), 200

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
