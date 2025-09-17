import json
import allure

def log_response(response, title="Response"):
    """Attach and print response details for debugging."""
    try:
        body = response.json()
    except Exception:
        body = response.text
    debug_info = {
        "status_code": response.status_code,
        "url": response.url,
        "body": body
    }
    pretty = json.dumps(debug_info, indent=2, ensure_ascii=False)
    print(f"\n--- {title} ---\n{pretty}\n")
    allure.attach(pretty, name=title, attachment_type=allure.attachment_type.JSON)

def log_request_payload(payload, title="Request Payload"):
    """Attach and print request payload for debugging."""
    pretty = json.dumps(payload, indent=2, ensure_ascii=False)
    print(f"\n--- {title} ---\n{pretty}\n")
    allure.attach(pretty, name=title, attachment_type=allure.attachment_type.JSON)