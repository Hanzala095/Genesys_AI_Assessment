import tensorflow as tf
import numpy as np
import json
from PIL import Image


MODEL_PATH = "outputs/models/factory_compliance_model.keras"
RULES_PATH = "config/rules.json"


model = tf.keras.models.load_model(MODEL_PATH)

with open(RULES_PATH, "r") as file:
    rules = json.load(file)


CLASS_NAMES = [
    "0_safe_walkway_violation",
    "1_unauthorized_intervention",
    "2_opened_panel_cover",
    "3_carrying_overload_with_forklift",
    "4_safe_walkway",
    "5_authorized_intervention",
    "6_closed_panel_cover",
    "7_safe_carrying"
]


image_path = input("Enter image path: ")

img = Image.open(image_path)

img = img.convert("RGB")
img = img.resize((224, 224))

img = np.array(img)
img = img / 255.0

img = np.expand_dims(img, axis=0)

prediction = model.predict(img)

predicted_index = np.argmax(prediction)

predicted_class = CLASS_NAMES[predicted_index]

confidence = prediction[0][predicted_index] * 100


print("\n" + "=" * 50)
print("DEBUG INFORMATION")
print("=" * 50)

print("\nPrediction Vector:")
print(prediction)

print("\nPredicted Index:")
print(predicted_index)

print("\nPredicted Class:")
print(predicted_class)

print("\nConfidence:")
print(f"{confidence:.2f}%")

print("\n" + "=" * 50)

if predicted_class in rules:

    print("\nPolicy Information:")

    print(
        "Severity:",
        rules[predicted_class]["severity"]
    )

    print(
        "Policy Section:",
        rules[predicted_class]["policy_section"]
    )

    print(
        "Indicator:",
        rules[predicted_class]["observable_indicator"]
    )

else:

    print("\nSafe Class Detected")