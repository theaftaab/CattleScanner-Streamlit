import logging
from PIL import Image
import base64
from flask import Flask, request, jsonify
import os

import CattleScanner
from CattleScanner.Cattle_inference import CattleRumination
from CattleScanner.Cattle_inference import CattleWeight


path = os.path.dirname(CattleScanner.__file__)

weight_model = CattleWeight(cwd=path)

# model_prediction = ModelPrediction()

app = Flask(__name__)

current_version = "v1"

@app.route('/{}/'.format(current_version), methods=['GET'])
def home():
    return "Service up and running!!!"


@app.route('/{}/image_classification'.format(current_version), methods=['POST'])
def image_classification():
    data = request.json
    rare_file = request.files['rare']
    rare_side = request.files['side']
    
    if rare_file.filename == '' or rare_file.filename == '':
        return jsonify({"error": "Both images must have a filename"}), 400

    # img1 = cv2.imdecode(np.frombuffer(file1.read(), np.uint8), cv2.IMREAD_COLOR)
    # img2 = cv2.imdecode(np.frombuffer(file2.read(), np.uint8), cv2.IMREAD_COLOR)

    # img = Image.open(file.stream)

    # data = file.stream.read()
    # # data = base64.encodebytes(data)
    # data = base64.b64encode(data).decode()
    
    if len(data) == 0:
        return jsonify([])

    weight = weight_model.predict(rare_side, rare_file)

    return jsonify({"weight": weight})


if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
