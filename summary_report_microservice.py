import json
import os
import time

REQUEST_FILE = "summary-request.json"
RESPONSE_FILE = "summary-response.json"


def load_request():
    with open(REQUEST_FILE, "r") as file:
        return json.load(file)


def write_response(response_data):
    with open(RESPONSE_FILE, "w") as file:
        json.dump(response_data, file, indent=4)



# Generate a summary of completed vs incomplete items
def completion_summary(data_type, items):
    completed_count = 0
    incomplete_count = 0

    for item in items:
        if item.get("completed") == True:
            completed_count += 1
        else:
            incomplete_count += 1

    return {
        "status": "success",
        "report_type": "completion_summary",
        "data_type": data_type,
        "total_items": len(items),
        "completed_items": completed_count,
        "incomplete_items": incomplete_count
    }

# Generate a report grouped by category
def category_summary(data_type, items):
    categories = {}

    for item in items:
        category = item.get("category", "Uncategorized")

        if category not in categories:
            categories[category] = 0

        categories[category] += 1

    return {
        "status": "success",
        "report_type": "category_summary",
        "data_type": data_type,
        "total_items": len(items),
        "categories": categories
    }

# Generate a report grouped by priority
def priority_summary(data_type, items):

    # Always keep priorities in this order
    priorities = {
        "High": 0,
        "Medium": 0,
        "Low": 0
    }

    # Count how many items belong to each priority
    for item in items:
        priority = item.get("priority")

        if priority in priorities:
            priorities[priority] += 1

    return {
        "status": "success",
        "report_type": "priority_summary",
        "data_type": data_type,
        "total_items": len(items),
        "priorities": priorities
    }

# Decide which report type to create
def generate_report(request_data):
    report_type = request_data.get("report_type")
    data_type = request_data.get("data_type")
    items = request_data.get("items", [])

    if report_type == "completion_summary":
        return completion_summary(data_type, items)

    elif report_type == "category_summary":
        return category_summary(data_type, items)

    elif report_type == "priority_summary":
        return priority_summary(data_type, items)

    else:
        return {
            "status": "error",
            "message": "Invalid report_type."
        }

# Main loop that waits for requests and processes them
def main():
    print("Summary Report Microservice is running...")
    print("Waiting for requests...")

    while True:
        if os.path.exists(REQUEST_FILE):
            try:
                request_data = load_request()
                response_data = generate_report(request_data)
                write_response(response_data)

                os.remove(REQUEST_FILE)

                print("Request processed successfully.")

            except Exception as error:
                error_response = {
                    "status": "error",
                    "message": str(error)
                }

                write_response(error_response)

                if os.path.exists(REQUEST_FILE):
                    os.remove(REQUEST_FILE)

        time.sleep(1)


if __name__ == "__main__":
    main()