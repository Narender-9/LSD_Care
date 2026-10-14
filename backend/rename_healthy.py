import os

folder = r"C:\Users\lakes\OneDrive\Desktop\EPICS\LSD_Project\merged_dataset\healthy"

extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

files = [
    f for f in os.listdir(folder)
    if f.lower().endswith(extensions)
]

files.sort()

# Temporary names first to avoid name conflicts
for i, file in enumerate(files, start=1):
    old_path = os.path.join(folder, file)
    temp_name = f"temp_healthy_{i:05d}{os.path.splitext(file)[1].lower()}"
    temp_path = os.path.join(folder, temp_name)
    os.rename(old_path, temp_path)

# Final sequential names
files = [
    f for f in os.listdir(folder)
    if f.startswith("temp_healthy_")
]

files.sort()

for i, file in enumerate(files, start=1):
    old_path = os.path.join(folder, file)
    extension = os.path.splitext(file)[1]
    new_name = f"healthy_{i:05d}{extension}"
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)

print("Healthy images renamed successfully!")
print("Total healthy images:", len(files))