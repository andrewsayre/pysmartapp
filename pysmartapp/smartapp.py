"""Define a SmartApp."""

import logging
from typing import Dict, Sequence

from .consts import LIFECYCLE_PING
from .errors import SmartAppNotRegisteredError
from .eventhook import EventHook
from .utilities import create_request

_LOGGER = logging.getLogger(__name__)


class SmartApp:
    """Define the SmartApp class."""

    def __init__(self, name: str, description: str,
                 permissions: Sequence[str], config_app_id: str = 'app',
                 path: str = '/', public_key=None, app_id: str = None):
        """Initialize the SmartApp class."""
        self._name = name
        self._description = description
        self._permissions = permissions
        self._config_app_id = config_app_id
        self._path = path
        self._public_key = public_key
        self._app_id = app_id
        self.on_ping = EventHook()
        self.on_config = EventHook()
        self.on_install = EventHook()
        self.on_update = EventHook()
        self.on_event = EventHook()
        self.on_oauth_callback = EventHook()
        self.on_uninstall = EventHook()

    def handle_request(self, data: dict, headers: dict = None,
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
    def config_app_id(self):
        """Get the id for the SmartApp to use in the config."""
        return self._config_app_id

    @property
    def path(self) -> str:
        """Get the path the SmartApp is installed at."""
        return self._path

    @path.setter
    def path(self, value: str):
        """Set the path the SmartApp is installed at."""
        self._path = value

    @property
    def public_key(self):
        """Get the public key of the SmartApp used to verify events."""
        return self._public_key

    @public_key.setter
    def public_key(self, value: str):
        """Set the public key of the SmartApp used to verify events."""
        self._public_key = value

    @property
    def app_id(self):
        """Get the unique id of the SmartApp."""
        return self._app_id

    @app_id.setter
    def app_id(self, value):
        """Set the unique id of the SmartApp."""
        self._app_id = value


class SmartAppManager:
    """Service to support multiple SmartApps at the same end-point."""

    def __init__(self):
        """Create a new instance of the manager."""
        self._smartapps: Dict[str, SmartApp] = {}
        self._installed_apps: Dict[str, SmartApp] = {}
        self.on_ping = EventHook()
        self.on_config = EventHook()
        self.on_install = EventHook()
        self.on_update = EventHook()
        self.on_event = EventHook()
        self.on_oauth_callback = EventHook()
        self.on_uninstall = EventHook()

    def handle_request(self, data: dict, headers: dict = None,
                       validate_signature: bool = True) -> dict:
        """Process a lifecycle event."""
        req = create_request(data)
        # Always process ping lifecycle events.
        if req.lifecycle == LIFECYCLE_PING:
            resp = req.process(self, headers, validate_signature)
        else:
            smartapp = self._installed_apps.get(req.installed_app_id)
            if not smartapp:
                raise SmartAppNotRegisteredError(req.installed_app_id)
            resp = req.process(smartapp, headers, validate_signature)

        if req.installed_app_id:
            _LOGGER.debug("%s: %s received for installed app %s.",
                          req.execution_id, req.lifecycle,
                          req.installed_app_id)
        else:
            _LOGGER.debug("%s: %s received.",
                          req.execution_id, req.lifecycle)
        return resp.to_data()

    def register(self, smartapp: SmartApp):
        """Register a SmartApp with one or more installed apps."""
        if smartapp.app_id is None:
            raise ValueError('smartapp must have an app_id.')
        if smartapp.app_id in self._smartapps:
            raise ValueError('smartapp already registered.')
        self._smartapps[smartapp.app_id] = smartapp
        smartapp.on_config += self.on_config.fire
        smartapp.on_install += self.on_install.fire
        smartapp.on_update += self.on_update.fire
        smartapp.on_event += self.on_event.fire
        smartapp.on_oauth_callback += self.on_oauth_callback.fire
        smartapp.on_uninstall += self.on_uninstall.fire

    def unregister(self, smartapp: SmartApp):
        """Unregister the specified installed app id."""
        if smartapp.app_id is None:
            raise ValueError('smartapp must have an app_id.')
        if smartapp.app_id not in self._smartapps:
            raise ValueError('smartapp was not previously registered.')
        self._smartapps.pop(smartapp.app_id, None)
        smartapp.on_config -= self.on_config.fire
        smartapp.on_install -= self.on_install.fire
        smartapp.on_update -= self.on_update.fire
        smartapp.on_event -= self.on_event.fire
        smartapp.on_oauth_callback -= self.on_oauth_callback.fire
        smartapp.on_uninstall -= self.on_uninstall.fire

    def map_installed_apps(self, app_id: str, *installed_app_ids: str):
        """Map an installed app to a SmartApp handler."""
        smartapp = self._smartapps[app_id]
        for installed_app_id in installed_app_ids:
            self._installed_apps[installed_app_id] = smartapp

    def unmap_installed_apps(self, *installed_app_ids: str):
        """Remove mappings of installed app to SmartApp handler."""
        for installed_app_id in installed_app_ids:
            self._installed_apps.pop(installed_app_id, None)

    @property
    def smartapps(self) -> Dict[str, SmartApp]:
        """Get registered SmartApps."""
        return self._smartapps

    @property
    def installed_apps(self) -> Dict[str, SmartApp]:
        """Get installed app ids mapped to SmartApps."""
        return self._installed_apps
