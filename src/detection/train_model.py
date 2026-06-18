import tensorflow as tf
import os

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.models import Model


DATASET_PATH = "data/extracted_frames"

IMG_SIZE = (224, 224)

BATCH_SIZE = 16

EPOCHS = 10


train_dataset = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

val_dataset = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)


class_names = train_dataset.class_names

print("\nClasses:\n")

for c in class_names:
    print(c)


base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)

base_model.trainable = False


x = base_model.output

x = GlobalAveragePooling2D()(x)

predictions = Dense(
    len(class_names),
    activation="softmax"
)(x)

model = Model(
    inputs=base_model.input,
    outputs=predictions
)


model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


history = model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=EPOCHS
)


os.makedirs(
    "outputs/models",
    exist_ok=True
)

model.save(
    "outputs/models/factory_compliance_model.keras"
)

print("\nMODEL SAVED SUCCESSFULLY")