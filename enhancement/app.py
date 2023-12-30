from flask import Flask, render_template, request, send_file, jsonify
import os
import subprocess
import json
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/apienhance', methods=['POST'])
def enhancement():
    if request.method == "POST":

        if 'image' not in request.files:
            return 'No file part'

        file = request.files['image']

        if file.filename == '':
            return 'No selected file'

        # Save the uploaded file to a folder (e.g., 'uploads')
        file_path = 'uploads/blurred-image.jpeg'
        file.save(file_path)

        # Run the prediction script (predict1.py) using subprocess.run
        result = subprocess.run(['python', 'predict1.py', file_path], capture_output=True, text=True)

        # Check if the subprocess was successful
        if result.returncode == 0:
            return send_file("submit/blurred-image.jpeg", mimetype='image/jpeg')
        else:
            # Optionally, you can handle errors or return an error response
            return f"Error in subprocess: {result.stderr}"

@app.route('/apienhancejson', methods=['POST'])
def enhancementjson():
    if request.method == "POST":

        if 'image' not in request.files:
            return 'No file part'

        file = request.files['image']

        if file.filename == '':
            return 'No selected file'

        # Save the uploaded file to a folder (e.g., 'uploads')
        file_path = 'uploads/blurred-image.jpeg'
        file.save(file_path)

        # Run the prediction script (predict1.py) using subprocess.run
        result = subprocess.run(['python', 'predict1.py', file_path], capture_output=True, text=True)

        # Check if the subprocess was successful
        if result.returncode == 0:
            with open('submit/blurred-image.jpeg', 'rb') as image_file:
        # Encode the image data as base64
                encodedimage = base64.b64encode(image_file.read()).decode('utf-8')

                return json.dumps([f"{encodedimage}"])
        else:
            # Optionally, you can handle errors or return an error response
            return f"Error in subprocess: {result.stderr}"

if __name__ == '__main__':
    app.run(debug=True)
