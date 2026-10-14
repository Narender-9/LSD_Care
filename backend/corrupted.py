from PIL import Image
import os

folder = r"C:\Users\lakes\OneDrive\Desktop\EPICS\LSD_Project\infected"

deleted = 0

for file in os.listdir(folder):
    path = os.path.join(folder, file)
    try:
        img = Image.open(path)
        img.verify()
    except:
        os.remove(path)
        deleted += 1

print(f"Deleted {deleted} corrupted images")