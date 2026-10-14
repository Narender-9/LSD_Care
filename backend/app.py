from fastapi import FastAPI, File, UploadFile, HTTPException
from tensorflow.keras.models import load_model
from ultralytics import YOLO
from PIL import Image, UnidentifiedImageError
import numpy as np
import io


# Create FastAPI application
app = FastAPI(
    title="Lumpy Skin Disease Detection API",
    version="1.0.0"
)


# Load trained LSD model
model = load_model("models/lsd_classifier_updated.keras")

# Load YOLO model for cow detection
cow_model = YOLO("yolo11n.pt")


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Lumpy Skin Disease Detection API is running"
    }


# Prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Check whether a file was uploaded
    if not file:
        raise HTTPException(
            status_code=400,
            detail="No file uploaded"
        )

    # Check file type
    allowed_types = [
        "image/jpeg",
        "image/png",
        "image/jpg"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Please upload a JPG, JPEG, or PNG image"
        )

    try:
        # Read uploaded image
        image_data = await file.read()

        # Check empty file
        if not image_data:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty"
            )

        # Open image
        img = Image.open(
            io.BytesIO(image_data)
        ).convert("RGB")

    except UnidentifiedImageError:
        raise HTTPException(
            status_code=400,
            detail="Invalid or corrupted image file"
        )

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to process the uploaded image"
        )


    # --------------------------------------------------
    # STEP 1: CHECK WHETHER IMAGE CONTAINS A COW
    # --------------------------------------------------

    # Run YOLO cow detection
    yolo_results = cow_model(img, verbose=False)

    cow_found = False

    for result in yolo_results:

        for box in result.boxes:

            class_id = int(box.cls[0])
            class_name = result.names[class_id]

            if class_name.lower() == "cow":
                cow_found = True
                break

        if cow_found:
            break


    # If no cow is detected, stop here
    if not cow_found:
        return {
            "prediction": "Invalid Image",
            "confidence": 0,
            "message": "Please upload a clear image of a cow for Lumpy Skin Disease detection."
        }


    # --------------------------------------------------
    # STEP 2: LUMPY SKIN DISEASE PREDICTION
    # --------------------------------------------------

    # Resize image for EfficientNetB0
    img = img.resize((224, 224))

    # Convert image to NumPy array
    img_array = np.array(img)

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Make LSD prediction
    prediction = model.predict(
        img_array,
        verbose=0
    )[0][0]


    # Determine result
    if prediction > 0.5:

        result = "Infected"
        confidence = prediction * 100
        message = "Lumpy Skin Disease detected"

    else:

        result = "Healthy"
        confidence = (1 - prediction) * 100
        message = "No signs of Lumpy Skin Disease detected"


    # Return prediction
    return {
        "prediction": result,
        "confidence": round(float(confidence), 2),
        "message": message
    }