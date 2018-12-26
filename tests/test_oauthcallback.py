""""Tests for the oauthcallback module."""

from pysmartapp.consts import LIFECYCLE_OAUTH_CALLBACK
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
        assert req.installed_app_id == '08153c4d-d0c1-4657-91ea-4f1ee535f030'
        assert req.url_path == 'string'
