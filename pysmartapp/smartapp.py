"""Define a SmartApp."""

import logging
from typing import Sequence

from .eventhook import EventHook
from .utilities import create_request

_LOGGER = logging.getLogger(__name__)


class SmartApp:
    """Define the SmartApp class."""

    def __init__(self, name: str, description: str,
                 permissions: Sequence[str], app_id: str = 'app',
                 path: str = '/', public_key=None):
        """Initialize the SmartApp class."""
        self._name = name
        self._description = description
        self._permissions = permissions
        self._app_id = app_id
        self._path = path
        self._public_key = public_key
        self.on_ping = EventHook()
        self.on_config = EventHook()
        self.on_install = EventHook()
        self.on_update = EventHook()
        self.on_event = EventHook()
        self.on_oauth_callback = EventHook()
        self.on_uninstall = EventHook()

    def handle_request(self, data: dict, headers: list = None,
                       validate_signature: bool = True) -> dict:
        """Process a lifecycle event."""
        req = create_request(data)
        resp = req.process(self, headers, validate_signature)

        if req.installed_app_id:
            _LOGGER.debug("%s: %s received for installed app %s.",
                          req.execution_id, req.lifecycle,
                          req.installed_app_id)
        else:
            _LOGGER.debug("%s: %s received.",
                          req.execution_id, req.lifecycle)

        return resp.to_data()

    @property
    def name(self) -> str:
        """Get the name of the SmartApp."""
        return self._name

    @property
    def description(self) -> str:
        """Get the description of the SmartApp."""
        return self._description

    @property
    def permissions(self) -> Sequence[str]:
        """Get the install permissions of the SmartApp."""
        return self._permissions

    @property
    def app_id(self):
        """Get the app id of the SmartApp."""
        return self._app_id

    @property
    def path(self) -> str:
        """Get the path the SmartApp is installed at."""
        return self._path

    @property
    def public_key(self):
        """Get the public key of the SmartApp used to verify events."""
        return self._public_key
