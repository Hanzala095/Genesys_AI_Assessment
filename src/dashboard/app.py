import streamlit as st
import tensorflow as tf
import numpy as np
import json
import sqlite3
import pandas as pd
from datetime import datetime
from PIL import Image


MODEL_PATH = "outputs/models/factory_compliance_model.keras"
RULES_PATH = "config/rules.json"
DB_PATH = "database/compliance.db"


@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


model = load_model()
def log_prediction(
    predicted_class,
    severity,
    policy_section,
    confidence,
    image_path
):

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO violations
    (
        timestamp,
        predicted_class,
        severity,
        policy_section,
        confidence,
        image_path
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        str(datetime.now()),
        predicted_class,
        severity,
        policy_section,
        confidence,
        image_path
    ))

    conn.commit()
    conn.close()

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
DISPLAY_NAMES = {
    "0_safe_walkway_violation": "Safe Walkway Violation",
    "1_unauthorized_intervention": "Unauthorized Intervention",
    "2_opened_panel_cover": "Opened Panel Cover",
    "3_carrying_overload_with_forklift": "Forklift Overload",
    "4_safe_walkway": "Safe Walkway",
    "5_authorized_intervention": "Authorized Intervention",
    "6_closed_panel_cover": "Closed Panel Cover",
    "7_safe_carrying": "Safe Carrying"
}

st.title("Factory Compliance Monitoring System")
st.caption(
    "Policy-Grounded AI System for Occupational Health & Safety Compliance Monitoring"
)

uploaded_file = st.file_uploader(
    "Upload Factory Image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    img = image.convert("RGB")
    img = img.resize((224, 224))

    img = np.array(img)
    img = img / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    predicted_index = np.argmax(prediction)

    predicted_class = CLASS_NAMES[predicted_index]

    confidence = float(
        prediction[0][predicted_index] * 100
    )

    st.subheader("Prediction")

    st.write(
    f"Behavior: {DISPLAY_NAMES[predicted_class]}"
    )

    st.write(
        f"Confidence: {confidence:.2f}%"
    )

    if predicted_class in rules:

        st.subheader("Policy Information")

        severity = rules[predicted_class]["severity"]

        if severity == "CRITICAL":
          st.error(f"Severity: {severity}")

        elif severity == "HIGH":
          st.warning(f"Severity: {severity}")

        elif severity == "SAFE":
          st.success(f"Severity: {severity}")

        else:
          st.info(f"Severity: {severity}")

        st.write(
            f"Policy Section: {rules[predicted_class]['policy_section']}"
        )

        st.write(
            f"Indicator: {rules[predicted_class]['observable_indicator']}"
        )
        log_prediction(
    predicted_class,
    rules[predicted_class]["severity"],
    rules[predicted_class]["policy_section"],
    confidence,
    uploaded_file.name
)

st.success("Detection logged successfully.")


st.subheader("Dashboard Statistics")

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM violations"
)

total_records = cursor.fetchone()[0]

cursor.execute(
    "SELECT COUNT(*) FROM violations WHERE severity='CRITICAL'"
)

critical_count = cursor.fetchone()[0]

cursor.execute(
    "SELECT COUNT(*) FROM violations WHERE severity='HIGH'"
)

high_count = cursor.fetchone()[0]

cursor.execute(
    "SELECT COUNT(*) FROM violations WHERE severity='SAFE'"
)

safe_count = cursor.fetchone()[0]

conn.close()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", total_records)
col2.metric("Critical", critical_count)
col3.metric("High", high_count)
col4.metric("Safe", safe_count)

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM violations ORDER BY id DESC"
)

rows = cursor.fetchall()

conn.close()

df = pd.DataFrame(
    rows,
    columns=[
        "ID",
        "Timestamp",
        "Class",
        "Severity",
        "Policy Section",
        "Confidence",
        "Image"
    ]
)

st.dataframe(
    df,
    use_container_width=True
)