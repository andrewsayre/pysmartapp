"""Sample web server utilizing the API package."""

import logging
from flask import Flask, request, jsonify
from pysmartapp.smartapp import SmartApp

logging.basicConfig(level=logging.DEBUG)
_LOGGER = logging.getLogger(__name__)

APP = Flask(__name__)

SMARTAPP = SmartApp(
    "HomeAssistant",
    "SmartApp that pushes devices updates to HomeAssistant",
    ["l:devices", "r:devices:*", "l:scenes"]
)
SMARTAPP.on_event += lambda events, **args: _LOGGER.debug(events['events'])


@APP.route("/", methods=["POST"])
def webhook():
    """Handle lifecycle requests."""
    content = request.get_json()
    response = SMARTAPP.handle_request(content)
    if response is not None:
        return jsonify(response)
    return "501 Not Implemented", 501


if __name__ == "__main__":
    APP.run(port=8321)
