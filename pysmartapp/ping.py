"""Define the ping module."""

from .lifecycle import LifecycleRequest, LifecycleResponse


class PingResponse(LifecycleResponse):
    """Define a ping response."""

    def __init__(self, challenge: str):
        """Initialize the ping response."""
        self._challenge = challenge

    def to_dict(self):
        """Return a dictionary of the ping request."""
        return {'pingData': {'challenge': self._challenge}}

    @property
    def challenge(self) -> str:
        """Get the ping challenge response."""
        return self._challenge


class PingRequest(LifecycleRequest):
    """Define a ping request."""

    @property
    def challenge(self):
        """Get the ping challenge."""
        return self._entity['pingData']['challenge']
