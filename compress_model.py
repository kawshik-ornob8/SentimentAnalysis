import gzip

# Path to your original model file
MODEL_PATH = "sentiment_model.joblib"
COMPRESSED_MODEL_PATH = "sentiment_model.joblib.gz"

# Compress the model using gzip
with open(MODEL_PATH, "rb") as f_in:
    with gzip.open(COMPRESSED_MODEL_PATH, "wb") as f_out:
        f_out.writelines(f_in)

print(f"Model compressed and saved to {COMPRESSED_MODEL_PATH}")