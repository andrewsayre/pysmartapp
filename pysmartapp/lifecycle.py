"""Define the lifecycle."""

from typing import Optional, Sequence

LIFECYCLE_PING = 'PING'
LIFECYCLE_CONFIG = 'CONFIGURATION'
CONFIG_INITIALIZE = 'INITIALIZE'
CONFIG_PAGE = 'PAGE'


class LifecycleRequest:
    """Define the Lifecycle class."""

    def __init__(self, entity: dict):
        """Initialize a new instance of lifecycle."""
        self._entity = entity

    @property
    def lifecycle(self) -> str:
        """Get the lifecycle type."""
        return self._entity['lifecycle']

    @property
    def execution_id(self) -> str:
        """Get the execution id."""
        return self._entity['execution_id']

    @property
    def locale(self) -> str:
        """Get the locale."""
        return self._entity['locale']

    @property
    def version(self) -> str:
        """Get the version."""
        return self._entity['version']


class PingRequest(LifecycleRequest):
    """Define a ping request."""

    @property
    def ping_challenge(self):
        """Get the ping challenge."""
        return self._entity['pingData']['challenge']


class ConfigurationRequest(LifecycleRequest):
    """Define a configuration request."""

    @property
    def installed_app_id(self):
        """Get the InstalledApp ID."""
        return self._entity['configurationData']['installedAppId']

    @property
    def phase(self):
        """Get the configuration phase."""
        return self._entity['configurationData']['phase']

    @property
    def page_id(self) -> Optional[str]:
        """Get the page id."""
        return self._entity['configurationData']['pageId']

    @property
    def previous_page_id(self) -> Optional[str]:
        """Get the previous page id."""
        return self._entity['configurationData']['previousPageId']


class LifecycleResponse:
    """Define a lifecycle response."""

    def to_dict(self) -> dict:
        """Return a dictionary of the request."""
        raise NotImplementedError


class PingResponse(LifecycleResponse):
    """Define a ping response."""

    def __init__(self, challenge: str):
        """Initialize the ping response."""
        self._challenge = challenge

    def to_dict(self):
        """Return a dictionary of the ping request."""
        return {'pingData': {'challenge': self._challenge}}


class ConfigurationResponse(LifecycleResponse):
    """Define a configuration response."""

    pass


class ConfigurationInitializeResponse(ConfigurationResponse):
    """Define a response to configuration initialization."""

    def __init__(self, name: str, description: str,
                 permissions: Sequence[str], app_id: str = 'app'):
        """Initialize the configuration initialization response."""
        self._name = name
        self._description = description
        self._permissions = permissions
        self._app_id = app_id

    @property
    def name(self):
        """Get the install name of the SmartApp."""
        return self._name

    @property
    def description(self):
        """Get the description of the SmartApp."""
        return self._description

    @property
    def permissions(self):
        """Get the permissions of the SmartApp."""
        return self._permissions

    @property
    def app_id(self):
        """Get the app id of the SmartApp."""
        return self._app_id

    def to_dict(self):
        """Return a dictionary of the response."""
        return {
            'configurationData': {
                'initialize': {
                    'name': self.name,
                    'description': self.description,
                    'id': self.app_id,
                    'permissions': self.permissions,
                    'firstPageId': "1"
                }
            }
        }
