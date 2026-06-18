import json
import os


rules = {
    "0_safe_walkway_violation": {
        "unsafe_behavior": "Safe Walkway Violation",
        "safe_behavior": "Safe Walkway",
        "policy_section": "3.3.2",
        "severity": "MEDIUM",
        "observable_indicator": "Person outside green walkway"
    },

    "1_unauthorized_intervention": {
        "unsafe_behavior": "Unauthorized Intervention",
        "safe_behavior": "Authorized Intervention",
        "policy_section": "4.3.2",
        "severity": "HIGH",
        "observable_indicator": "Person interacting with equipment without green vest"
    },

    "2_opened_panel_cover": {
        "unsafe_behavior": "Opened Panel Cover",
        "safe_behavior": "Closed Panel Cover",
        "policy_section": "5.2.2",
        "severity": "LOW",
        "observable_indicator": "Panel cover left open"
    },

    "3_carrying_overload_with_forklift": {
        "unsafe_behavior": "Carrying Overload with Forklift",
        "safe_behavior": "Safe Carrying",
        "policy_section": "6.3.2",
        "severity": "CRITICAL",
        "observable_indicator": "Forklift carrying 3 or more blocks"
    }
}


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT_PATH = os.path.abspath(
    os.path.join(
        BASE_DIR,
        "..",
        "..",
        "config",
        "rules.json"
    )
)

with open(OUTPUT_PATH, "w") as file:
    json.dump(rules, file, indent=4)

print("rules.json created successfully!")
print(OUTPUT_PATH)