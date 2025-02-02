import gzip
import joblib
from django.shortcuts import render

# Path to the compressed model file
COMPRESSED_MODEL_PATH = "sentiment_model.joblib.gz"

# Load the compressed model
def load_compressed_model():
    with gzip.open(COMPRESSED_MODEL_PATH, "rb") as f:
        model = joblib.load(f)
    return model

# Load the model once when the app starts
model = load_compressed_model()

# Similarly, load the label encoder
LABEL_ENCODER_PATH = "label_encoder.joblib"
label_encoder = joblib.load(LABEL_ENCODER_PATH)

def analyze_sentiment(request):
    sentiment = None
    if request.method == "POST":
        user_input = request.POST.get("comment", "")
        if user_input:
            predicted_label = model.predict([user_input])
            sentiment = label_encoder.inverse_transform(predicted_label)[0]
    
    return render(request, "sentiment/index.html", {"sentiment": sentiment})

def about(request):
    return render(request, "sentiment/about.html")

def home(request):
    return render(request, "sentiment/home.html")