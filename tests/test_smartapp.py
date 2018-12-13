"""Tests for the SmartApp file."""

from pysmartapp.smartapp import SmartApp
from .utilities import get_json


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
    def test_ping():
        """Tests the ping lifecycle event."""
        # Arrange
        request = get_json("ping_request.json")
        expected_response = get_json("ping_response.json")
        app = SmartApp("Test Name", "Test Description", [])
        # Act
        response = app.handle_request(request)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_on_ping():
        """Tests the ping event handler."""
        # Arrange
        request = get_json("ping_request.json")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(ping_data, data, app):
            nonlocal fired
            fired = True
            assert request['pingData'] == ping_data
            assert request == data
            assert app == smartapp
        smartapp.on_ping += handler
        # Act
        smartapp.handle_request(request)
        # Assert
        assert fired

    @staticmethod
    def test_config_init():
        """Tests the configuration initialization lifecycle event."""
        # Arrange
        request = get_json("config_init_request.json")
        expected_response = get_json("config_init_response.json")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_config_page():
        """Tests the configuration initialization page event."""
        # Arrange
        request = get_json("config_page_request.json")
        expected_response = get_json("config_page_response.json")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_on_config():
        """Tests the config event handler."""
        # Arrange
        request = get_json("config_init_request.json")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(config_data, data, app):
            nonlocal fired
            fired = True
            assert request['configurationData'] == config_data
            assert request == data
            assert app == smartapp
        smartapp.on_config += handler
        # Act
        smartapp.handle_request(request)
        # Assert
        assert fired

    @staticmethod
    def test_install():
        """Tests the install lifecycle event."""
        # Arrange
        request = get_json("install_request.json")
        expected_response = get_json("install_response.json")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request)
        # Assert
        assert response == expected_response
        assert app.auth_token == '580aff1f-f0f1-44e0-94d4-e68bf9c2e768'
        assert app.refresh_token == 'ad58374e-9d6a-4457-8488-a05aa8337ab3'

    @staticmethod
    def test_on_install():
        """Tests the install event handler."""
        # Arrange
        request = get_json("install_request.json")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(install_data, data, app):
            nonlocal fired
            fired = True
            assert request['installData'] == install_data
            assert request == data
            assert app == smartapp
        smartapp.on_install += handler
        # Act
        smartapp.handle_request(request)
        # Assert
        assert fired

    @staticmethod
    def test_update():
        """Tests the update lifecycle event."""
        # Arrange
        request = get_json("update_request.json")
        expected_response = get_json("update_response.json")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request)
        # Assert
        assert response == expected_response
        assert app.auth_token == '4ebd8d9f-53b0-483f-a989-4bde30ca83c0'
        assert app.refresh_token == '6e3bbf5f-b68d-4250-bbc9-f7151016a77f'

    @staticmethod
    def test_on_update():
        """Tests the update event handler."""
        # Arrange
        request = get_json("update_request.json")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(update_data, data, app):
            nonlocal fired
            fired = True
            assert request['updateData'] == update_data
            assert request == data
            assert app == smartapp
        smartapp.on_update += handler
        # Act
        smartapp.handle_request(request)
        # Assert
        assert fired

    @staticmethod
    def test_event():
        """Tests the event lifecycle event."""
        # Arrange
        request = get_json("event_request.json")
        expected_response = get_json("event_response.json")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_on_event():
        """Tests the event event handler."""
        # Arrange
        request = get_json("event_request.json")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(event_data, data, app):
            nonlocal fired
            fired = True
            assert request['eventData'] == event_data
            assert request == data
            assert app == smartapp
        smartapp.on_event += handler
        # Act
        smartapp.handle_request(request)
        # Assert
        assert fired

    @staticmethod
    def test_oauth_callback():
        """Tests the oauth_callback lifecycle event."""
        # Arrange
        request = get_json("oauth_callback_request.json")
        expected_response = get_json("oauth_callback_response.json")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_on_oauth_callback():
        """Tests the oauth_callback event handler."""
        # Arrange
        request = get_json("oauth_callback_request.json")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(oauth_callback, data, app):
            nonlocal fired
            fired = True
            assert request['oAuthCallbackData'] == oauth_callback
            assert request == data
            assert app == smartapp
        smartapp.on_oauth_callback += handler
        # Act
        smartapp.handle_request(request)
        # Assert
        assert fired

    @staticmethod
    def test_uninstall():
        """Tests the uninstall lifecycle event."""
        # Arrange
        request = get_json("uninstall_request.json")
        expected_response = get_json("uninstall_response.json")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_on_uninstall():
        """Tests the uninstall event handler."""
        # Arrange
        request = get_json("uninstall_request.json")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(uninstall_data, data, app):
            nonlocal fired
            fired = True
            assert request['uninstallData'] == uninstall_data
            assert request == data
            assert app == smartapp
        smartapp.on_uninstall += handler
        # Act
        smartapp.handle_request(request)
        # Assert
        assert fired
