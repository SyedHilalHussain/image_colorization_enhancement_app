from flask import Flask, request, jsonify, send_file
import os
import json
from colorizer import Colorizer


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/api', methods=['POST'])
def colorize():
    if request.method == 'POST':
        f = request.files['file']
        colored_img = Colorizer(f,base64_res=False)
        return send_file(colored_img, mimetype='image/PNG')

@app.route('/api_b64', methods=['POST'])
def colorize_b64():
    if request.method == 'POST':
        f = request.files['file']
        base64_colored_img = Colorizer(f,base64_res=True)
        return json.dumps([f"{base64_colored_img}"])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)