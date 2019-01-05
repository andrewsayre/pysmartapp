""""Tests for the ping module."""

from pysmartapp.const import LIFECYCLE_PING
from pysmartapp.ping import PingRequest

from .utilities import get_fixture


class TestPingRequest:
    """Tests for the PingRequest class."""

    @staticmethod
    def test_init():
        """Tests the init method."""
        # Arrange
        data = get_fixture('ping_request')
        # Act
        req = PingRequest(data)
        # Assert
        assert req.ping_data_raw == data['pingData']
        assert req.lifecycle == LIFECYCLE_PING
        assert req.execution_id == data['executionId']
        assert req.locale == data['locale']
        assert req.version == data['version']
        assert req.ping_challenge == '1a904d57-4fab-4b15-a11e-1c4bfe7cb502'
