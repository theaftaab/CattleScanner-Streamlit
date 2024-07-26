import logging
from PIL import Image
import base64
from flask import Flask, request, jsonify
import os

import CattleScanner
from CattleScanner.Cattle_inference import CattleRumination
from CattleScanner.Cattle_inference import CattleWeight

# model_prediction = ModelPrediction()

app = Flask(__name__)

current_version = "v1"

path = os.path.dirname(CattleScanner.__file__)

@app.route('/{}/'.format(current_version), methods=['GET'])
def home():
    return "Serviceup and running!!!"


@app.route('/{}/image_classification'.format(current_version), methods=['POST'])
def image_classification():
    data = request.json
    file = request.files['image']

    img = Image.open(file.stream)

    data = file.stream.read()
    # data = base64.encodebytes(data)
    data = base64.b64encode(data).decode()
    if len(data) == 0:
        return jsonify([])

    weight_model = CattleWeight(cwd=path)
    weight = weight_model.predict(side_img, rear_img)

    inf_data = model_prediction.predict(data)
    return jsonify(inf_data)


if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
