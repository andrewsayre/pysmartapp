""""Tests for the oauthcallback module."""

from pysmartapp.const import LIFECYCLE_OAUTH_CALLBACK
from pysmartapp.oauthcallback import OAuthCallbackRequest

from .utilities import get_fixture


class TestOAuthCallbackRequest:
    """Tests for the OAuthCallbackRequest class."""

    @staticmethod
    def test_init():
        """Tests the init method."""
        # Arrange
        data = get_fixture('oauth_callback_request')
        # Act
        req = OAuthCallbackRequest(data)
        # Assert
        assert req.oauth_callback_data_raw == data['oAuthCallbackData']
        assert req.lifecycle == LIFECYCLE_OAUTH_CALLBACK
        assert req.execution_id == data['executionId']
        assert req.locale == data['locale']
        assert req.version == data['version']
        assert req.installed_app_id == '8a0dcdc9-1ab4-4c60-9de7-cb78f59a1121'
        assert req.url_path == 'string'
