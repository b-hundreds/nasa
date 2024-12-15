import gspread
import json
import os
from google.oauth2.service_account import Credentials
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lấy thông tin xác thực từ biến môi trường
json_creds = os.getenv("GOOGLE_SHEET_CREDENTIALS")
creds_dict = json.loads(json_creds)

# Tạo credentials từ biến môi trường
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)

# Mở Google Sheet
sheet = client.open("nasa_infor").sheet1

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
