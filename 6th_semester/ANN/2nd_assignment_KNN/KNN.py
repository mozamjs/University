import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imutils import paths
import os

# Step 1: Gather / Load Dataset

ds_path = "/run/media/mozam/New Volume/University/6th_semester/ANN/Dataset/animals"

imagePaths = list(paths.list_images(ds_path))

print("[INFO] Total images:", len(imagePaths))

data = []
labels = []
width = 32
height = 32

for (i, imagePath) in enumerate(imagePaths):
    image = cv2.imread(imagePath)
    # Get class label from folder name
    label = imagePath.split(os.path.sep)[-2]
    # Resize image
    image = cv2.resize(image, (width, height))
    # Store image and label
    data.append(image)
    labels.append(label)

# Convert lists to NumPy arrays
data = np.array(data)
labels = np.array(labels)

print("[INFO] Data shape before flattening:", data.shape)

# Flatten images
data = data.reshape((data.shape[0], 3072))
print("[INFO] Data shape after flattening:", data.shape)

# Convert labels into numbers
le = LabelEncoder()
labels = le.fit_transform(labels)

print("[INFO] Classes:", le.classes_)

# Step 2: Split Dataset
(trainX, testX, trainY, testY) = train_test_split(
    data,
    labels,
    test_size=0.25,
    random_state=42
)

print("[INFO] Training images:", len(trainX))
print("[INFO] Testing images:", len(testX))

# Step 3: Train KNN Classifier
print("[INFO] training k-NN classifier...")

model = KNeighborsClassifier(n_neighbors=1)
model.fit(trainX, trainY)

# Step 4: Evaluate
print("[INFO] evaluating k-NN classifier...")

predictions = model.predict(testX)

print(classification_report(
    testY,
    predictions,
    target_names=le.classes_
))