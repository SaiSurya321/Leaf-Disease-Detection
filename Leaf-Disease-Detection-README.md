# 🌿 Leaf Disease Detection using CNN

A deep learning system that identifies diseases in plant leaves from a photo, built to help farmers and researchers catch crop issues early. Includes a Streamlit web app for real-time, no-code detection.

## 📖 Overview

Early detection of plant disease is critical for preventing crop loss. This project trains separate **Convolutional Neural Network (CNN)** models on leaf images for multiple crops, classifying each as healthy or infected with a specific disease. Models are evaluated with precision, recall, and F1-score, and the best-performing models are wired into a single Streamlit app for interactive use.

**Crops currently supported:** Apple, Banana, Corn, Cotton, Grape, Potato, Tomato

## 🛠️ Features

- **Multi-crop detection** — separate trained CNN models per crop, selectable in the app
- **Real-time inference** — upload a leaf image, get an instant classification
- **Performance evaluation** — precision, recall, and F1-score reported per model
- **Simple UI** — built with Streamlit, no ML background needed to use it

## 📊 Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Deep Learning | TensorFlow, Keras (CNN) |
| Image Processing | OpenCV, PIL |
| Web App | Streamlit |
| Analysis / Metrics | NumPy, Pandas, scikit-learn |

## 📁 Project Structure

```
Leaf-Disease-Detection/
├── notebooks/
│   ├── apple_disease_model.ipynb
│   ├── banana_disease_model.ipynb
│   ├── corn_disease_model.ipynb
│   ├── cotton_disease_model.ipynb
│   ├── grape_disease_model.ipynb
│   ├── potato_disease_model.ipynb
│   └── tomato_disease_model.ipynb
├── app/
│   ├── all_in_One_streamlit_app.py
│   ├── s1.py
│   └── s2.py
├── models/            # trained .keras model files (see note below)
├── requirements.txt
└── README.md
```

> Your repo currently has the training notebooks sitting in the root with their original Colab file names (e.g. `Copy_of_BANANAcode_(2)_(1).ipynb`). Rename and move them to match the structure above — it makes the repo look intentional rather than dumped from Colab. Quick way to do it locally:
> ```bash
> mkdir notebooks app
> git mv "Copy_of_BANANAcode_(2)_(1).ipynb" notebooks/banana_disease_model.ipynb
> git mv "Copy_of_Tomato_5th_(1)_(1)_(1) (1).ipynb" notebooks/tomato_disease_model.ipynb
> git mv "Copy_of_potatofold20_(1)_(1) (1).ipynb" notebooks/potato_disease_model.ipynb
> git mv "applefold20_(2).ipynb" notebooks/apple_disease_model.ipynb
> git mv "cornfold20_(2).ipynb" notebooks/corn_disease_model.ipynb
> git mv "cottonkfold_(1)_(1).ipynb" notebooks/cotton_disease_model.ipynb
> git mv "grapefold20_(1)_(1).ipynb" notebooks/grape_disease_model.ipynb
> git mv all_in_One_streamlit_app.py app/all_in_One_streamlit_app.py
> git mv s1.py app/s1.py
> git mv s2.py app/s2.py
> git commit -m "Reorganize project structure"
> ```

## 📦 Dataset

[ Confirm and link the dataset you trained on — most projects like this use the **PlantVillage** dataset (available on Kaggle). State the exact source, size, and number of classes here so anyone can reproduce your training. ]

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/SaiSurya321/Leaf-Disease-Detection.git
cd Leaf-Disease-Detection
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Model files
> Trained `.keras` model files aren't included in this repo due to GitHub's 100MB file limit.
> [ Add a download link here — e.g. a Google Drive/Hugging Face link — or a note to run the training notebooks yourself to regenerate them. ]

### 4. Run the app
```bash
streamlit run app/all_in_One_streamlit_app.py
```

## 📈 Results

| Crop | Precision | Recall | F1-score |
|---|---|---|---|
| Apple | [ ] | [ ] | [ ] |
| Banana | [ ] | [ ] | [ ] |
| Corn | [ ] | [ ] | [ ] |
| Cotton | [ ] | [ ] | [ ] |
| Grape | [ ] | [ ] | [ ] |
| Potato | [ ] | [ ] | [ ] |
| Tomato | [ ] | [ ] | [ ] |

> Pull these numbers from your notebook outputs — a results table with real metrics is one of the highest-signal things you can add for anyone reviewing this repo.

## 🖼️ Demo

[ Add a screenshot or short GIF of the Streamlit app in action, and/or a live demo link if you deploy it on Streamlit Community Cloud. ]

## 🗺️ Roadmap

- [ ] Add more crops / disease classes
- [ ] Deploy live demo on Streamlit Community Cloud
- [ ] Add unit tests for preprocessing pipeline
- [ ] Model compression for faster inference

## 📄 License

[ Add a LICENSE file — MIT is a common, permissive choice for a portfolio project. ]

## 📬 Contact

Sai Surya Vadde — [LinkedIn](https://www.linkedin.com/in/saisuryavadde116) · [vss.lpu6@gmail.com](mailto:vss.lpu6@gmail.com)
