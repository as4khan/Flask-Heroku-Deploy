from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def get_fruits():
    try:
        api_url = "https://www.fruityvice.com/api/fruit/all"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()

        fruits = response.json()
        return jsonify({"data": fruits})
    except Exception as error:
        return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))