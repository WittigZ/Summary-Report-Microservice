import json
import os
import time

REQUEST_FILE = "summary-request.json"
RESPONSE_FILE = "summary-response.json"


# Example request for a priority summary report
request_data = {
    "report_type": "priority_summary",
    "data_type": "tasks",
    "items": [
        {
            "title": "Finish homework",
            "priority": "High",
            "category": "School",
            "completed": True
        },
        {
            "title": "Clean room",
            "priority": "Low",
            "category": "Personal",
            "completed": False
        },
        {
            "title": "Study for exam",
            "priority": "High",
            "category": "School",
            "completed": True
        },
        {
            "title": "Buy groceries",
            "priority": "Medium",
            "category": "Personal",
            "completed": False
        },
        {
            "title": "Pay bill",
            "priority": "High",
            "category": "Personal",
            "completed": False
        }
    ]
}


if os.path.exists(RESPONSE_FILE):
    os.remove(RESPONSE_FILE)


# Send priority summary request to the microservice
with open(REQUEST_FILE, "w") as file:
    json.dump(request_data, file, indent=4)

print("Priority summary request sent.")


# Wait for the response file to be created
while not os.path.exists(RESPONSE_FILE):
    time.sleep(0.5)


# Read and display the response
with open(RESPONSE_FILE, "r") as file:
    response_data = json.load(file)

print("Priority summary response received:")
print(json.dumps(response_data, indent=4))