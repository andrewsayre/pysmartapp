"""Define a SmartApp."""

from typing import Sequence, Optional
from . import lifecycle


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
        lifecycle_event = entity.get("lifecycle", None)
        if lifecycle_event == lifecycle.LIFECYCLE_PING:
            return self.ping(lifecycle.PingRequest(entity))
        if lifecycle_event == lifecycle.LIFECYCLE_CONFIG:
            return self.configuration(lifecycle.ConfigurationRequest(entity))
        return None

    def ping(self, request: lifecycle.PingRequest) -> lifecycle.PingResponse:
        """Process a ping lifecycle event."""
        # pylint: disable=no-self-use
        return lifecycle.PingResponse(request.ping_challenge)

    def configuration(self, request: lifecycle.ConfigurationRequest) \
            -> lifecycle.ConfigurationResponse:
        """Process a configuration lifecycle event."""
        if request.phase == lifecycle.CONFIG_INITIALIZE:
            return lifecycle.ConfigurationInitializeResponse(
                self._name,
                self._description,
                self._permissions,
                self._app_id)
        if request.phase == lifecycle.CONFIG_PAGE:
            pass
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
