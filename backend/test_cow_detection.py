from ultralytics import YOLO

# Load pre-trained YOLO model
model = YOLO("yolo11n.pt")

# Test cow image
image_path = r"C:\Users\lakes\OneDrive\Desktop\EPICS\LSD_Project\cow_image.png"

# Run detection
results = model(image_path)

# Check whether a cow is detected
cow_found = False

for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        class_name = result.names[class_id]

        print("Detected:", class_name)

        if class_name == "cow":
            cow_found = True

if cow_found:
    print("COW DETECTED")
else:
    print("NO COW DETECTED")