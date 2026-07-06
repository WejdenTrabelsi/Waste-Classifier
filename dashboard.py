"""
Streamlit dashboard for the  waste classifier.

Run:
    streamlit run dashboard.py
"""

from pathlib import Path
import streamlit as st
from fastai.vision.all import load_learner, PILImage

from recommendations import get_recommendation

MODEL_PATH = Path("data/model/waste_classifier.pkl")

st.set_page_config(page_title=" Waste Classifier", page_icon="♻️")
st.title("♻️ Waste Classifier")
st.write("Upload a photo of a waste item to identify its type and get an equipment recommendation.")

@st.cache_resource
def get_learner():
    return load_learner(MODEL_PATH)

learn = get_learner()

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = PILImage.create(uploaded_file)
    st.image(img.to_thumb(300, 300), caption="Uploaded image")

    pred_class, pred_idx, probs = learn.predict(img)
    confidence = float(probs[pred_idx])

    st.subheader(f"Prediction: **{pred_class}**")
    st.progress(confidence)
    st.write(f"Confidence: {confidence:.1%}")

    rec = get_recommendation(str(pred_class))
    st.markdown("### Recommended equipment")
    st.write(f"**{rec['label_fr']}** → {rec['machine']}")
    st.write(f"Reduction: {rec['reduction']}")
    st.caption(rec["note"])
