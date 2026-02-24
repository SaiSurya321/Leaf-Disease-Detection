import streamlit as st
from PIL import Image
import numpy as np

# Title
st.title("🍃 Leaf Disease Detection")

# Upload image
uploaded_file = st.file_uploader(""D:/PROJECT SPRING 2025/Datasets/Banana/BananaLSD/TrainingSet/cordana/8_aug.jpeg", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Leaf', use_column_width=True)
    
    # Button to simulate disease prediction
    if st.button("Predict Disease"):
        # Here you would integrate your ML model
        # Simulating a prediction result
        predicted_disease = "Powdery Mildew"
        confidence = "95%"
        
        st.success(f"🌱 **Disease Detected:** {predicted_disease}")
        st.info(f"🔍 **Confidence:** {confidence}")
