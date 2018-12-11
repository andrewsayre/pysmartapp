"""Define the configuration module."""

from typing import Optional, Sequence
from .lifecycle import LifecycleRequest, LifecycleResponse

CONFIG_INITIALIZE = 'INITIALIZE'
CONFIG_PAGE = 'PAGE'


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


class ConfigurationResponse(LifecycleResponse):
    """Define a configuration response."""

    def to_dict(self):
        """Get a data structure representing the response."""
        return {'configurationData': self._to_dict_phase()}

    def _to_dict_phase(self):
        raise NotImplementedError


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

    def _to_dict_phase(self):
        return {
            'initialize': {
                'name': self.name,
                'description': self.description,
                'id': self.app_id,
                'permissions': self.permissions,
                'firstPageId': "1"
                }
            }
