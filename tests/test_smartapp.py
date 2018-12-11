"""Tests for the SmartApp file."""

from pysmartapp.smartapp import SmartApp
from pysmartapp.ping import PingResponse
from pysmartapp.lifecycle import LIFECYCLE_PING, LIFECYCLE_CONFIG
from pysmartapp.configuration import ConfigurationInitializeResponse


class TestSmartApp:
    """Tests for the SmartApp class."""

    @staticmethod
    def test_initialize():
        """Tests the property initialization."""
        # Arrange
        name = "Test Name"
        description = "Test Description"
        perms = ["Perm1"]
        app_id = "MyApp"
        # Act
        app = SmartApp(name, description, perms, app_id)
        # Assert
        assert app.name == name
        assert app.description == description
        assert app.permissions == perms
        assert app.app_id == app_id

    @staticmethod
    def test_process_unknown():
        """Tests an unknown lifecycle event."""
        # Arrange
        app = SmartApp("Test", "Test", ["perms"])
        entity = {'lifecycle': "Unknown"}
        # Act
        response = app.process_request(entity)
        # Assert
        assert response is None

    @staticmethod
    def test_ping():
        """Tests the ping event."""
        # Arrange
        app = SmartApp("Test", "Test", ["perms"])
        challenge = "TEST"
        entity = {'lifecycle': LIFECYCLE_PING,
                  'pingData': {'challenge': challenge}}
        # Act
        response = app.process_request(entity)
        # Assert
        assert isinstance(response, PingResponse)
        assert response.challenge == challenge

    @staticmethod
    def test_configuraiton_unknown():
        """Tests an unknown configuration phase."""
        # Arrange
        app = SmartApp("Test", "Test Desc", ["perms"], "myapp")
        entity = {
            'lifecycle': LIFECYCLE_CONFIG,
            'configurationData': {
                'phase': 'OTHER',
            }
        }
        # Act
        response = app.process_request(entity)
        # Assert
        assert response is None

    @staticmethod
    def test_configuration_init():
        """Tests the configuration init event"""
        # Arrange
        app = SmartApp("Test", "Test Desc", ["perms"], "myapp")
        entity = {
            'lifecycle': LIFECYCLE_CONFIG,
            'configurationData': {
                'installedAppId': '8a0dcdc9-1ab4-4c60-9de7-cb78f59a1121',
                'phase': 'INITIALIZE',
                'pageId': '',
                'previousPageId': ''
            }
        }
        # Act
        response = app.process_request(entity)
        # Assert
        assert isinstance(response, ConfigurationInitializeResponse)
        assert response.app_id == app.app_id
        assert response.name == app.name
        assert response.description == app.description
        assert response.permissions == app.permissions
