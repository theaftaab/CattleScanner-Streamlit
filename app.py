import logging
import os

from flask import Flask, jsonify, request
from PIL import Image

import CattleScanner
from CattleScanner.Cattle_inference import CattleRumination, CattleWeight

path = os.path.dirname(CattleScanner.__file__)

weight_model = CattleWeight(cwd=path)

# model_prediction = ModelPrediction()

app = Flask(__name__)

current_version = "v1"


@app.route(f"/{current_version}/", methods=["GET"])
def home():
    return "Service up and running!!!"


@app.route(f"/{current_version}/weight_prediction", methods=["POST"])
def weight_prediction():
    rear_file = request.files["rear"]
    side_file = request.files["side"]

    if rear_file.filename == "" or side_file.filename == "":
        return jsonify({"error": "Both images must have a filename"}), 400

    side_img = Image.open(side_file)
    rear_img = Image.open(rear_file)

    weight = weight_model.predict(side_img, rear_img)

    return jsonify({"weight": weight})


if __name__ == "__main__":
    app.logger.setLevel(logging.INFO)
    app.run(host="0.0.0.0", port=8000)
