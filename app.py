from io import BytesIO

from flask import Flask, jsonify, request
from PIL import Image
from pyzbar.pyzbar import decode

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello_world():
    if "file" not in request.files:
        return jsonify({"error": "No image part"}), 400

    file = request.files["file"]

    # If user does not select a file, browser also
    # submits an empty part without filename
    if file.filename == "":
        return jsonify({"error": "No selected image"}), 400

    img_data = BytesIO(file.read())
    img = Image.open(img_data)
    decoded_objects = decode(img)

    results = []
    for obj in decoded_objects:
        results.append(obj.data.decode("utf-8"))

    return jsonify(results), 200
