import os
import imagehash
from PIL import Image

# Main merged dataset
dataset = r"C:\Users\lakes\OneDrive\Desktop\EPICS\LSD_Project\merged_dataset"

total_images = 0
duplicate_count = 0
error_count = 0

# Check healthy and infected separately
for class_name in ["healthy", "infected"]:

    folder = os.path.join(dataset, class_name)

    print("\n================================")
    print("Checking:", class_name)
    print("================================")

    hashes = {}

    for file in os.listdir(folder):

        if not file.lower().endswith(
            (".png", ".jpg", ".jpeg", ".bmp", ".webp")
        ):
            continue

        total_images += 1
        path = os.path.join(folder, file)

        try:
            with Image.open(path) as img:

                # Convert to RGB for consistent hashing
                img = img.convert("RGB")

                h = imagehash.average_hash(img)

            if h in hashes:

                print(f"Duplicate Found: {file}")

                os.remove(path)

                duplicate_count += 1

            else:
                hashes[h] = file

        except Exception as e:

            print(f"Error reading {file}: {e}")
            error_count += 1


print("\n========== FINAL REPORT ==========")
print(f"Total Images Checked : {total_images}")
print(f"Duplicates Removed   : {duplicate_count}")
print(f"Errors               : {error_count}")
print("==================================")