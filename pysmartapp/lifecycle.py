"""Define the lifecycle."""

LIFECYCLE_PING = 'PING'
LIFECYCLE_CONFIG = 'CONFIGURATION'


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
        return self._entity['executionId']

    @property
    def locale(self) -> str:
        """Get the locale."""
        return self._entity['locale']

    @property
    def version(self) -> str:
        """Get the version."""
        return self._entity['version']


class LifecycleResponse:
    """Define a lifecycle response."""

    def to_dict(self) -> dict:
        """Return a dictionary of the request."""
        raise NotImplementedError
