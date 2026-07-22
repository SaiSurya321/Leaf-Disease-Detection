import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import random

# === CONFIG ===
st.set_page_config(
    page_title="🌿 Multi-Plant Disease Detection AI",
    layout="centered",
    initial_sidebar_state="expanded"
)

# === PLANT-MODEL MAPPING ===
PLANTS = {
    'Apple': {
        'model_path': 'models/best_model_fold_apple4.keras',
        'class_names': ['apple_scab', 'black_rot', 'cedar_apple_rust', 'healthy']
    },
    'Banana': {
        'model_path': 'models/best_model_fold_banana5.keras',
        'class_names': ['cordana', 'pestalotiopsis', 'healthy', 'sigatoka']
    },
    'Corn': {
        'model_path': 'models/best_model_fold_corn2.keras',
        'class_names' : ['Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot','Corn_(maize)___Northern_Leaf_Blight','Corn_(maize)___healthy','Corn_(maize)___Common_rust_']

    },
    'Cotton': {
        'model_path': 'models/best_model_fold_cotton4.keras',
        'class_names':['Aphids','Army_worm','Bacterial_Blight','Healthy','Powdery_Mildew','Target_spot']
    },
    'Grape': {
        'model_path': 'models/best_model_fold_grape1.keras',
        'class_names': ['black_rot', 'esca', 'leaf_blight', 'healthy']
    },
    'Potato': {
        'model_path': 'models/best_model_fold_potato5.keras',
        'class_names': ['healthy', 'late_blight', 'early_blight']
    },
    'Tomato': {
        'model_path': 'models/best_model_fold_tomato2.keras',
        'class_names': ['bacterial_spot', 'early_blight', 'late_blight', 'healthy']
    },
}

# === STYLING ===
st.markdown("""
    <style>
    body {
        background-color: #f4f9f4;
    }
    .main {
        background-color: #f0fdf4;
    }
    h1, h2, h3 {
        color: #2e4a34;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #34a853;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.75em 1em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0f9d58;
        transform: scale(1.02);
    }
    .stFileUploader {
        border: 2px dashed #a1cba1;
        border-radius: 8px;
        padding: 1em;
    }
    </style>
""", unsafe_allow_html=True)

# === WELCOME ===
st.title("🌱 Multi-Plant Leaf Disease Detector")
st.caption("🔍 AI-powered detection for 7 crop diseases (Apple, Banana, Corn, Cotton, Grape, Potato, Tomato)")
st.markdown("---")

# === PLANT SELECTOR ===
selected_plants = st.multiselect(
    "🌾 Choose one or more plants:",
    list(PLANTS.keys()),
    help="You can select multiple plant types. Upload one image per plant."
)

# === RANDOM FUN FACTS ===
FUN_FACTS = [
    "🍎 Apple scab can drastically reduce fruit quality if not managed early!",
    "🍌 Did you know? Sigatoka disease thrives in humid banana-growing regions.",
    "🌽 Corn rust can spread rapidly in warm, wet weather.",
    "🍇 Grapevine leaf blight causes distinct brown patches on leaves.",
    "🥔 Potato late blight was responsible for the Great Irish Famine!",
    "🍅 Tomatoes love sun, but late blight doesn’t—they clash.",
    "🧵 Cotton bacterial blight can reduce yield by 20% if left untreated!"
]

# === PREDICTION FUNCTION ===
def predict_image(img, model, class_names, image_size=(128, 128)):
    img = img.resize(image_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    img_array = tf.cast(img_array, tf.float32) / 255.0
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions)
    predicted_class = class_names[predicted_index]
    confidence = predictions[0][predicted_index]
    return predicted_class, confidence, predictions[0]

# === LOOP THROUGH EACH SELECTED PLANT ===
for plant in selected_plants:
    st.markdown(f"### 🌿 {plant}")
    uploaded_file = st.file_uploader(f"📸 Upload a leaf image for {plant}:", key=plant)

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption=f"{plant} Leaf", use_column_width=True)

        with st.spinner(f"🧠 Analyzing {plant} leaf for diseases..."):
            model_info = PLANTS[plant]
            model = tf.keras.models.load_model(model_info['model_path'])
            class_names = model_info['class_names']

            predicted_class, confidence, full_probs = predict_image(image, model, class_names)

        st.success(f"✅ **Prediction for {plant}:** {predicted_class}")
        st.info(f"📊 **Confidence:** {confidence:.2%}")

        st.subheader("🔬 Class Probabilities")
        prob_chart = {class_names[i]: float(full_probs[i]) for i in range(len(class_names))}
        st.bar_chart(prob_chart)

        st.markdown(f"💡 **Did you know?** {random.choice(FUN_FACTS)}")

    st.markdown("---")

# === FOOTER ===
st.caption("🌾 Built with ❤️ using Streamlit and TensorFlow")
