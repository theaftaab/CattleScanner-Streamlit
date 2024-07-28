import os
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

st.title("Cattle Weight Prediction")

side_image_uploaded = st.file_uploader("Upload Side Image (jpg, jpeg, png)")
rear_image_uploaded = st.file_uploader("Upload Rear Image (jpg, jpeg, png)")

if side_image_uploaded is not None and rear_image_uploaded is not None:
    side_img_path = save_uploaded_file(side_image_uploaded, "Side.jpg")
    rear_img_path = save_uploaded_file(rear_image_uploaded, "Rear.jpg")

    st.image([side_img_path, rear_img_path], caption=["Side Image", "Rear Image"], width=350)
    predicted_weight = predict_weight(side_img_path, rear_img_path)

    if predicted_weight is not None:
        st.success("Prediction Complete!")
        st.write(f"Predicted Weight: {predicted_weight} kg")
else:
    st.warning("Please upload both side and rear images.")
