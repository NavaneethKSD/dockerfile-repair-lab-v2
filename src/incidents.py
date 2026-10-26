"""In-memory incident store used by the API. Dummy data only."""

INCIDENTS = [
    {"id": 1, "title": "Checkout page slow", "severity": "high", "status": "open"},
    {"id": 2, "title": "Login email delayed", "severity": "low", "status": "resolved"},
]


def list_incidents():
    return INCIDENTS


def open_count():
    return sum(1 for item in INCIDENTS if item["status"] == "open")
