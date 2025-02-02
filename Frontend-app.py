import os
from ultralytics import YOLO

import streamlit as st

import CattleScanner
from CattleScanner.Cattle_inference import CattleWeight


def save_uploaded_file(uploaded_file, filename):
    if uploaded_file is not None:
        if not os.path.exists("uploaded_images"):
            os.makedirs("uploaded_images")
        filepath = os.path.join("uploaded_images", filename)
        with open(filepath, "wb") as f:
            f.write(uploaded_file.read())
        return filepath
    else:
        return None


def predict_weight(side_img_path, rear_img_path):
    try:
        path = os.path.dirname(CattleScanner.__file__)
        weight_model = CattleWeight(cwd=path)
        weight = weight_model.predict(side_img_path, rear_img_path)
        print(f"The weight is {weight} kg")
        return weight
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
        return None


st.title("Cattle Scanner")

side_image_uploaded = st.file_uploader("Upload Side Image (jpg, jpeg, png)")
rear_image_uploaded = st.file_uploader("Upload Rear Image (jpg, jpeg, png)")


def getClassName(model):
    class_name = None
    for box in model[0].boxes:
        class_id = int(box.cls)  # Assuming 'cls' gives the class id
        class_name = model[0].names[class_id]  # Get class name from the model's names dictionary
    return class_name


def predict_bcs(side_img_path: str):
    bcs_model = YOLO("CattleScanner/bcs.pt")

    results = bcs_model(side_img_path)
    return getClassName(results)
    # return "BCS-2.25"


def predict_breed(side_img_path):
    breed_model = YOLO("CattleScanner/breed.pt")

    results = breed_model(side_img_path)
    return getClassName(results)


def predict_horn_status(side_img_path):
    horn_model = YOLO("CattleScanner/horn.pt")

    results = horn_model(side_img_path)
    return getClassName(results)


def predict_wound_status(side_img_path):
    return "Dry Wound"


def predict_wormload(side_img_path):
    worm_model = YOLO("CattleScanner/worm.pt")
    results = worm_model(side_img_path)
    return getClassName(results)


def predict_cleft(rear_img_path):
    cleft_model = YOLO('CattleScanner/cleft.pt')
    results = cleft_model(rear_img_path)
    return getClassName(results)


def predict_breed_grade(side_img_path):
    grade_model = YOLO("CattleScanner/grade.pt")

    results = grade_model(side_img_path)
    return getClassName(results)


def predict_skin_coat(side_img_path):
    coat_model = YOLO("CattleScanner/coat.pt")
    results = coat_model(side_img_path)
    return getClassName(results)


def predict_teat_score(side_img_path):
    teat_model = YOLO("CattleScanner/teat.pt")
    results = teat_model(side_img_path)
    return getClassName(results)


def predict_udder_type(side_img_path):
    udder_model = YOLO("CattleScanner/UdderType.pt")

    results = udder_model(side_img_path)
    return getClassName(results)
    # return "Compact"


#
# if side_image_uploaded is not None and rear_image_uploaded is not None:
#     side_img_path = save_uploaded_file(side_image_uploaded, "Side.jpg")
#     rear_img_path = save_uploaded_file(rear_image_uploaded, "Rear.jpg")
#
#     st.image([side_img_path, rear_img_path], caption=["Side Image", "Rear Image"], width=350)
#     predicted_weight = predict_weight(side_img_path, rear_img_path)
#     predicted_bcs = predict_bcs(side_img_path)
#     predicted_breed = predict_breed(side_img_path)
#     predicted_horn_status = predict_horn_status(side_img_path, rear_img_path)
#     predicted_wound = predict_wound_status(side_img_path)
#     predicted_wormload = predict_wormload(side_img_path)
#     predicted_cleft = predict_cleft(side_img_path)
#     predicted_breed_grade = predict_breed_grade(side_img_path)
#     predicted_skin_coat = predict_skin_coat(side_img_path)
#     predicted_teat_score = predict_teat_score(side_img_path)
#     predicted_udder_type = predict_udder_type(side_img_path)
#     if predicted_weight is not None:
#         st.success("Prediction Complete!")
#         st.write(f"Predicted Weight: {predicted_weight} kg")
# else:
#     st.warning("Please upload both side and rear images.")
if side_image_uploaded is not None and rear_image_uploaded is not None:
    side_img_path = save_uploaded_file(side_image_uploaded, "Side.jpg")
    rear_img_path = save_uploaded_file(rear_image_uploaded, "Rear.jpg")

    st.image([side_img_path, rear_img_path], caption=["Side Image", "Rear Image"], width=350)

    predicted_weight = predict_weight(side_img_path, rear_img_path)
    predicted_bcs = predict_bcs(side_img_path)
    predicted_breed = predict_breed(side_img_path)
    predicted_horn_status = predict_horn_status(side_img_path)
    predicted_wound = predict_wound_status(side_img_path)
    predicted_wormload = predict_wormload(side_img_path)
    predicted_cleft = predict_cleft(rear_img_path)
    predicted_breed_grade = predict_breed_grade(side_img_path)
    predicted_skin_coat = predict_skin_coat(side_img_path)
    predicted_teat_score = predict_teat_score(side_img_path)
    predicted_udder_type = predict_udder_type(side_img_path)
    try:
        if predicted_weight is not None:
            st.success("Prediction Complete!")
            st.write(f"Predicted Weight: {predicted_weight} kg")
    except:
        pass
    st.success("Prediction Complete!")
    st.write(f"Predicted BCS: {predicted_bcs}")
    st.write(f"Predicted Breed: {predicted_breed}")
    st.write(f"Predicted Horn Status: {predicted_horn_status}")
    st.write(f"Predicted Wound Status: {predicted_wound}")
    st.write(f"Predicted Worm Load: {predicted_wormload}")
    st.write(f"Predicted Cleft: {predicted_cleft}")
    st.write(f"Predicted Breed Grade: {predicted_breed_grade}")
    st.write(f"Predicted Skin Coat: {predicted_skin_coat}")
    st.write(f"Predicted Teat Score: {predicted_teat_score}")
    st.write(f"Predicted Udder Type: {predicted_udder_type}")
else:
    st.warning("Please upload both side and rear images.")