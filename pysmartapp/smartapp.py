"""Define a SmartApp."""

from typing import Sequence, Optional
from . import lifecycle, ping, configuration as config


class SmartApp:
    """Define the SmartApp class."""

    def __init__(self, name: str, description: str,
                 permissions: Sequence[str], app_id: str = 'app',):
        """Initialize the SmartApp class."""
        self._name = name
        self._description = description
        self._permissions = permissions
        self._app_id = app_id

    def process_request(self, entity: dict) -> \
            Optional[lifecycle.LifecycleResponse]:
        """Get the response object for the request entity."""
        lifecycle_event = entity["lifecycle"]
        if lifecycle_event == lifecycle.LIFECYCLE_PING:
            return self.ping(ping.PingRequest(entity))
        if lifecycle_event == lifecycle.LIFECYCLE_CONFIG:
            return self.configuration(config.ConfigurationRequest(entity))
        return None

    def ping(self, request: ping.PingRequest) -> ping.PingResponse:
        """Process a ping lifecycle event."""
        # pylint: disable=no-self-use
        return ping.PingResponse(request.challenge)

    def configuration(self, request: config.ConfigurationRequest) \
            -> Optional[config.ConfigurationResponse]:
        """Process a configuration lifecycle event."""
        if request.phase == config.CONFIG_INITIALIZE:
            return config.ConfigurationInitializeResponse(
                self._name,
                self._description,
                self._permissions,
                self._app_id)
        return None

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
