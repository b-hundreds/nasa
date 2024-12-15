# from flask import Flask, render_template, request, jsonify
# from pymongo import MongoClient

# app = Flask(__name__)
# client = MongoClient('mongodb://localhost:27017/')
# db = client['nasa_english']
# collection = db['users']

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         data = request.get_json()
#         name = data.get('name')
#         email = data.get('email')
#         phone = data.get('phone')

#         collection.insert_one({"name": name, "email": email, "phone": phone})
#         return jsonify({"message": "Data saved successfully!"}), 200

#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Cấu hình kết nối với Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("elegant-racer-444806-d0-f89220529ff5.json", scope)
client = gspread.authorize(creds)

# Mở Google Sheet
sheet = client.open("nasa_info").sheet1  # Tên Google Sheet và sheet1 là trang đầu tiên

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        # Ghi dữ liệu vào Google Sheet
        sheet.append_row([name, email, phone])
        return jsonify({"message": "Data saved to Google Sheet!"}), 200

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
