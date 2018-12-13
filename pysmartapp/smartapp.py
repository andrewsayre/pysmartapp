"""Define a SmartApp."""

from typing import Sequence, Optional
import logging
from .consts import LIFECYCLE_PING, LIFECYCLE_CONFIG, \
    LIFECYCLE_CONFIG_INIT, LIFECYCLE_CONFIG_PAGE, \
    LIFECYCLE_INSTALL, LIFECYCLE_UPDATE, LIFECYCLE_EVENT, \
    LIFECYCLE_OAUTH_CALLBACK, LIFECYCLE_UNINSTALL
from .eventhook import EventHook

_LOGGER = logging.getLogger(__name__)


class SmartApp:
    """Define the SmartApp class."""

    def __init__(self, name: str, description: str,
                 permissions: Sequence[str], app_id: str = 'app',):
        """Initialize the SmartApp class."""
        self._name = name
        self._description = description
        self._permissions = permissions
        self._app_id = app_id
        self._auth_token = None
        self._refresh_token = None
        self.on_ping = EventHook()
        self.on_config = EventHook()
        self.on_install = EventHook()
        self.on_update = EventHook()
        self.on_event = EventHook()
        self.on_oauth_callback = EventHook()
        self.on_uninstall = EventHook()

    def handle_request(self, data: dict) -> Optional[dict]:
        """Process a lifecycle event."""
        event = data['lifecycle']
        if event == LIFECYCLE_PING:
            return self.ping(data)
        if event == LIFECYCLE_CONFIG:
            return self.config(data)
        if event == LIFECYCLE_INSTALL:
            return self.install(data)
        if event == LIFECYCLE_UPDATE:
            return self.update(data)
        if event == LIFECYCLE_EVENT:
            return self.event(data)
        if event == LIFECYCLE_OAUTH_CALLBACK:
            return self.oauth_callback(data)
        if event == LIFECYCLE_UNINSTALL:
            return self.uninstall(data)

    def ping(self, data: dict) -> dict:
        """Process a ping lifecycle event."""
        _LOGGER.debug("%s: PING received with challenge %s",
                      data['executionId'],
                      data['pingData']['challenge'])
        self.on_ping.fire(data['pingData'], data=data, app=self)
        return {'pingData': data['pingData']}

    def config(self, data: dict) -> dict:
        """Process a configuration lifecycle event."""
        phase = data['configurationData']['phase']
        if phase == LIFECYCLE_CONFIG_INIT:
            return self.config_init(data)
        if phase == LIFECYCLE_CONFIG_PAGE:
            return self.config_page(data)

    def config_init(self, data: dict) -> dict:
        """Process a configuration init lifecycle event."""
        _LOGGER.debug(
            "%s: CONFIGURATION INITIALIZE received for installed app %s",
            data['executionId'], data['configurationData']['installedAppId'])
        self.on_config.fire(data['configurationData'], data=data, app=self)
        return {
            'configurationData': {
                'initialize': {
                    'name': self.name,
                    'description': self.description,
                    'id': self.app_id,
                    'permissions': self.permissions,
                    'firstPageId': '1'
                }
            }
        }

    def config_page(self, data: dict) -> dict:
        """Process a configuration page lifecycle event."""
        _LOGGER.debug(
            "%s: CONFIGURATION PAGE '%s' received for installed app %s",
            data['executionId'], data['configurationData']['pageId'],
            data['configurationData']['installedAppId'])
        self.on_config.fire(data['configurationData'], data=data, app=self)
        return {
            'configurationData': {
                'page': {
                    'pageId': '1',
                    'name': 'Configuration',
                    'nextPageId': None,
                    'previousPageId': None,
                    'complete': True,
                    'sections': []
                }
            }
        }

    def install(self, data: dict) -> dict:
        """Process an install lifecycle event."""
        _LOGGER.debug(
            "%s: INSTALL received for installed app %s in location %s",
            data['executionId'],
            data['installData']['installedApp']['installedAppId'],
            data['installData']['installedApp']['locationId'])
        self._auth_token = data['installData']['authToken']
        self._refresh_token = data['installData']['refreshToken']
        self.on_install.fire(data['installData'], data=data, app=self)
        return {"installData": {}}

    def update(self, data: dict) -> dict:
        """Process an update lifecycle event."""
        _LOGGER.debug(
            "%s: UPDATE received for installed app %s in location %s",
            data['executionId'],
            data['updateData']['installedApp']['installedAppId'],
            data['updateData']['installedApp']['locationId'])
        self._auth_token = data['updateData']['authToken']
        self._refresh_token = data['updateData']['refreshToken']
        self.on_update.fire(data['updateData'], data=data, app=self)
        return {"updateData": {}}

    def event(self, data: dict) -> dict:
        """Process an event lifecycle event."""
        _LOGGER.debug(
            "%s: EVENT received for installed app %s in location %s",
            data['executionId'],
            data['eventData']['installedApp']['installedAppId'],
            data['eventData']['installedApp']['locationId'])
        self.on_event.fire(data['eventData'], data=data, app=self)
        return {"eventData": {}}

    def oauth_callback(self, data: dict) -> dict:
        """Process an event oauth_callback event."""
        _LOGGER.debug(
            "%s: OAUTH_CALLBACK received for installed app %s",
            data['executionId'], data['oAuthCallbackData']['installedAppId'])
        self.on_oauth_callback.fire(data['oAuthCallbackData'],
                                    data=data, app=self)
        return {"oAuthCallbackData": {}}

    def uninstall(self, data: dict) -> dict:
        """Process an uninstall lifecycle event."""
        _LOGGER.debug(
            "%s: UNINSTALL received for installed app %s in location %s",
            data['executionId'],
            data['uninstallData']['installedApp']['installedAppId'],
            data['uninstallData']['installedApp']['locationId'])
        self.on_uninstall.fire(data['uninstallData'], data=data, app=self)
        return {"uninstallData": {}}

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
    def auth_token(self):
        """Get the authorization token returned during installation."""
        return self._auth_token

    @property
    def refresh_token(self):
        """Get the refresh token returned during installation."""
        return self._refresh_token
