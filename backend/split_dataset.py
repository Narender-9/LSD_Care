import os
import shutil
from sklearn.model_selection import train_test_split

# ======== PROJECT PATH ========
project_path = r"C:\Users\lakes\OneDrive\Desktop\EPICS\LSD_Project"

# ======== CLEANED MERGED DATASET ========
healthy_folder = os.path.join(
    project_path, "merged_dataset", "healthy"
)

infected_folder = os.path.join(
    project_path, "merged_dataset", "infected"
)

# ======== NEW DATASET FOLDER ========
dataset_folder = os.path.join(
    project_path, "dataset_new"
)

# Create train, valid and test folders
for split in ["train", "valid", "test"]:
    for category in ["healthy", "infected"]:
        os.makedirs(
            os.path.join(dataset_folder, split, category),
            exist_ok=True
        )


def split_images(source_folder, class_name):

    images = [
        f for f in os.listdir(source_folder)
        if f.lower().endswith(
            (".png", ".jpg", ".jpeg", ".bmp", ".webp")
        )
    ]

    # 80% Train, 20% temporary
    train, temp = train_test_split(
        images,
        test_size=0.20,
        random_state=42,
        shuffle=True
    )

    # Remaining 20% -> 10% Validation + 10% Test
    valid, test = train_test_split(
        temp,
        test_size=0.50,
        random_state=42,
        shuffle=True
    )

    # Copy training images
    for img in train:

        shutil.copy2(
            os.path.join(source_folder, img),
            os.path.join(
                dataset_folder,
                "train",
                class_name,
                img
            )
        )

    # Copy validation images
    for img in valid:

        shutil.copy2(
            os.path.join(source_folder, img),
            os.path.join(
                dataset_folder,
                "valid",
                class_name,
                img
            )
        )

    # Copy test images
    for img in test:

        shutil.copy2(
            os.path.join(source_folder, img),
            os.path.join(
                dataset_folder,
                "test",
                class_name,
                img
            )
        )

    print()
    print(class_name.upper(), "DATASET")
    print("Train      :", len(train))
    print("Validation :", len(valid))
    print("Test       :", len(test))


# Split both classes
split_images(
    healthy_folder,
    "healthy"
)

split_images(
    infected_folder,
    "infected"
)

print()
print("======================================")
print("NEW DATASET SPLIT COMPLETED!")
print("======================================")
print("Dataset location:")
print(dataset_folder)