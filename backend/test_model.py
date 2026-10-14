from tensorflow.keras.models import load_model

model = load_model("models/lsd_classifier_updated.keras")

print("Model loaded successfully!")
print("Model input shape:", model.input_shape)