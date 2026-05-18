import json
import os
import time

REQUEST_FILE = "summary-request.json"
RESPONSE_FILE = "summary-response.json"


# Example request data sent to the microservice
request_data = {
    "report_type": "completion_summary",
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
        }
    ]
}


if os.path.exists(RESPONSE_FILE):
    os.remove(RESPONSE_FILE)


# Send request data to the microservice
with open(REQUEST_FILE, "w") as file:
    json.dump(request_data, file, indent=4)

print("Request sent.")


# Wait for the response file to be created
while not os.path.exists(RESPONSE_FILE):
    time.sleep(0.5)


# Read and display the response
with open(RESPONSE_FILE, "r") as file:
    response_data = json.load(file)

print("Response received:")
print(json.dumps(response_data, indent=4))