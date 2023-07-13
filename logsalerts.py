import requests
import json

def get_alert(id, token):
    url = f"https://api.logz.io/v2/alerts/{id}"
    headers = {
        "X-API-TOKEN": token
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()

        # a. Ensure "enabled" is True
        data["enabled"] = True

        # b. Ensure "output.recipients.emails" is an empty array
        data["output"]["recipients"]["emails"] = []

        # c. Ensure "output.recipients.notificationEndpointIds" is an empty array
        data["output"]["recipients"]["notificationEndpointIds"] = []

        # d. Update each object in "subComponents" array
        for sub_component in data["subComponents"]:
            sub_component["queryDefinition"]["shouldQueryOnAllAccounts"] = True
            sub_component["queryDefinition"]["accountIdsToQueryOn"] = []
            sub_component["output"]["columns"] = []
            sub_component["output"]["shouldUseAllFields"] = True

        return data
    else:
        return None  # Or you can handle the error case differently based on your requirements

# Example usage
alert_id = input("Enter the alert ID: ")
token = input("Enter the token: ")

result = get_alert(alert_id, token)

if result is not None:
    print(json.dumps(result, indent=2))  # Serialize the JSON data with proper indentation
else:
    print("Failed to retrieve the alert.")
