"""Tests for the SmartApp file."""

from pysmartapp.smartapp import SmartApp

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
