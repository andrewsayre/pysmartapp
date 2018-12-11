"""Sample web server utilizing the API package."""

from flask import Flask, request, jsonify
from pysmartapp.smartapp import SmartApp

APP = Flask(__name__)

SMARTAPP = SmartApp(
    "HomeAssistant",
    "SmartApp that pushes devices updates to HomeAssistant",
    ["l:devices", "r:devices:*", "l:scenes"]
)


@APP.route("/", methods=["POST"])
def webhook():
    """Handle lifecycle requests."""
    content = request.get_json()
    response = SMARTAPP.process_request(content)
    if response is not None:
        return jsonify(response.to_dict())
    return "501 Not Implemented", 501


if __name__ == "__main__":
    APP.run(port=8321)
