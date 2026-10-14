# Real-Time Lumpy Skin Disease Identification in Cows Using AI

## Project Overview

This project uses Artificial Intelligence and Computer Vision to identify Lumpy Skin Disease (LSD) in cows from images.

The system uses an EfficientNetB0 deep learning model to classify cow images into two classes:

- Healthy
- Infected

The trained model is integrated with a FastAPI backend that accepts an image and returns the predicted class, confidence score, and detection message.

## Technology Stack

- Python
- TensorFlow / Keras
- EfficientNetB0
- NumPy
- OpenCV
- Pillow
- FastAPI
- Uvicorn
- Jupyter Notebook

## Dataset

The project combines multiple datasets containing healthy and infected cow images.

The dataset was cleaned using:

- Corrupted image detection
- Duplicate image removal
- Blurry image detection
- Image renaming
- Train/validation/test splitting

## Dataset Split

The cleaned dataset was divided into:

- Training set
- Validation set
- Test set

## Deep Learning Model

EfficientNetB0 with ImageNet pretrained weights was used as the base model.

The classification architecture contains:

- EfficientNetB0
- Global Average Pooling
- Dense layer with ReLU activation
- Dropout
- Sigmoid output layer

The model performs binary classification:

`Healthy` vs `Infected`

## Model Input

Image size:

224 × 224 × 3

## Model Output

The model produces a probability that is converted into:

- Healthy
- Infected

with a confidence score.

## Backend API

FastAPI is used to provide the prediction service.

### API Endpoints

`GET /`

Checks whether the API is running.

`POST /predict`

Accepts an image and returns the prediction.

Example response:

```json
{
    "prediction": "Infected",
    "confidence": 92.83,
    "message": "Lumpy Skin Disease detected"
}