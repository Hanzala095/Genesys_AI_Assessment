from logger import log_detection


log_detection(
    predicted_class="3_carrying_overload_with_forklift",
    severity="CRITICAL",
    policy_section="6.3.2",
    confidence=97.5,
    image_path="test.jpg"
)