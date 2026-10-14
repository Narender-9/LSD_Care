import cv2
import os
import shutil

# Main merged dataset
dataset = r"C:\Users\lakes\OneDrive\Desktop\EPICS\LSD_Project\merged_dataset"

# Blur threshold
threshold = 80

total_images = 0
blurry_count = 0
error_count = 0

# Check both classes
for class_name in ["healthy", "infected"]:

    folder = os.path.join(dataset, class_name)

    # Folder to store blurry images
    blurry_folder = os.path.join(folder, "Blurry_Images")
    os.makedirs(blurry_folder, exist_ok=True)

    print("\n================================")
    print("Checking:", class_name)
    print("================================")

    for file in os.listdir(folder):

        # Skip the blurry-image folder
        if file == "Blurry_Images":
            continue

        if not file.lower().endswith(
            (".png", ".jpg", ".jpeg", ".bmp", ".webp")
        ):
            continue

        total_images += 1

        path = os.path.join(folder, file)

        try:

            img = cv2.imread(path)

            if img is None:
                print(f"Cannot read: {file}")
                error_count += 1
                continue

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            score = cv2.Laplacian(
                gray,
                cv2.CV_64F
            ).var()

            if score < threshold:

                print(
                    f"Blurry: {file} | "
                    f"Score: {score:.2f}"
                )

                shutil.move(
                    path,
                    os.path.join(blurry_folder, file)
                )

                blurry_count += 1

        except Exception as e:

            print(f"Error: {file} -> {e}")
            error_count += 1


print("\n========== FINAL REPORT ==========")
print(f"Total Images Checked : {total_images}")
print(f"Blurry Images Found  : {blurry_count}")
print(f"Errors               : {error_count}")
print("==================================")