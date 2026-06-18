import json


RULES_PATH = "config/rules.json"


with open(RULES_PATH, "r") as file:
    rules = json.load(file)


def get_severity(predicted_class):

    if predicted_class in rules:

        return {
            "severity":
                rules[predicted_class]["severity"],

            "policy_section":
                rules[predicted_class]["policy_section"],

            "indicator":
                rules[predicted_class]["observable_indicator"]
        }

    return {
        "severity": "UNKNOWN",
        "policy_section": "N/A",
        "indicator": "N/A"
    }


if __name__ == "__main__":

    result = get_severity(
        "1_unauthorized_intervention"
    )

    print(result)