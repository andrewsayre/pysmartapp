"""Tests for the SmartApp file."""

import pytest

from pysmartapp.errors import SignatureVerificationError
from pysmartapp.smartapp import SmartApp

from .utilities import get_fixture


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
        request = get_fixture("ping_request")
        expected_response = get_fixture("ping_response")
        app = SmartApp("Test Name", "Test Description", [])
        # Act
        response = app.handle_request(request)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_on_ping():
        """Tests the ping event handler."""
        # Arrange
        request = get_fixture("ping_request")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(req, resp, app):
            nonlocal fired
            fired = True
            assert app == smartapp
        smartapp.on_ping += handler
        # Act
        smartapp.handle_request(request, None, False)
        # Assert
        assert fired

    @staticmethod
    def test_config_init():
        """Tests the configuration initialization lifecycle event."""
        # Arrange
        request = get_fixture("config_init_request")
        expected_response = get_fixture("config_init_response")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request, None, False)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_config_page():
        """Tests the configuration initialization page event."""
        # Arrange
        request = get_fixture("config_page_request")
        expected_response = get_fixture("config_page_response")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request, None, False)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_on_config():
        """Tests the config event handler."""
        # Arrange
        request = get_fixture("config_init_request")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(req, resp, app):
            nonlocal fired
            fired = True
            assert app == smartapp
        smartapp.on_config += handler
        # Act
        smartapp.handle_request(request, None, False)
        # Assert
        assert fired

    @staticmethod
    def test_install():
        """Tests the install lifecycle event."""
        # Arrange
        request = get_fixture("install_request")
        expected_response = get_fixture("install_response")
        smartapp = SmartApp("SmartApp", "SmartApp Description",
                            ['l:devices'], "myapp")
        # Act
        response = smartapp.handle_request(request, None, False)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_on_install():
        """Tests the install event handler."""
        # Arrange
        request = get_fixture("install_request")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(req, resp, app):
            nonlocal fired
            fired = True
            assert req.auth_token == '580aff1f-f0f1-44e0-94d4-e68bf9c2e768'
            assert req.refresh_token == 'ad58374e-9d6a-4457-8488-a05aa8337ab3'
            assert app == smartapp
        smartapp.on_install += handler
        # Act
        smartapp.handle_request(request, None, False)
        # Assert
        assert fired

    @staticmethod
    def test_update():
        """Tests the update lifecycle event."""
        # Arrange
        request = get_fixture("update_request")
        expected_response = get_fixture("update_response")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request, None, False)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_on_update():
        """Tests the update event handler."""
        # Arrange
        request = get_fixture("update_request")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(req, resp, app):
            nonlocal fired
            fired = True
            assert req.auth_token == '4ebd8d9f-53b0-483f-a989-4bde30ca83c0'
            assert req.refresh_token == '6e3bbf5f-b68d-4250-bbc9-f7151016a77f'
            assert app == smartapp
        smartapp.on_update += handler
        # Act
        smartapp.handle_request(request, None, False)
        # Assert
        assert fired

    @staticmethod
    def test_event():
        """Tests the event lifecycle event."""
        # Arrange
        request = get_fixture("event_request")
        expected_response = get_fixture("event_response")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request, None, False)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_on_event():
        """Tests the event event handler."""
        # Arrange
        request = get_fixture("event_request")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(req, resp, app):
            nonlocal fired
            fired = True
            assert app == smartapp
        smartapp.on_event += handler
        # Act
        smartapp.handle_request(request, None, False)
        # Assert
        assert fired

    @staticmethod
    def test_oauth_callback():
        """Tests the oauth_callback lifecycle event."""
        # Arrange
        request = get_fixture("oauth_callback_request")
        expected_response = get_fixture("oauth_callback_response")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request, None, False)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_on_oauth_callback():
        """Tests the oauth_callback event handler."""
        # Arrange
        request = get_fixture("oauth_callback_request")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(req, resp, app):
            nonlocal fired
            fired = True
            assert app == smartapp
        smartapp.on_oauth_callback += handler
        # Act
        smartapp.handle_request(request, None, False)
        # Assert
        assert fired

    @staticmethod
    def test_uninstall():
        """Tests the uninstall lifecycle event."""
        # Arrange
        request = get_fixture("uninstall_request")
        expected_response = get_fixture("uninstall_response")
        app = SmartApp("SmartApp", "SmartApp Description",
                       ['l:devices'], "myapp")
        # Act
        response = app.handle_request(request, None, False)
        # Assert
        assert response == expected_response

    @staticmethod
    def test_on_uninstall():
        """Tests the uninstall event handler."""
        # Arrange
        request = get_fixture("uninstall_request")
        smartapp = SmartApp("Test Name", "Test Description", [])
        fired = False

        def handler(req, resp, app):
            nonlocal fired
            fired = True
            assert app == smartapp
        smartapp.on_uninstall += handler
        # Act
        smartapp.handle_request(request, None, False)
        # Assert
        assert fired

    @staticmethod
    def test_handle_request_sig_verification():
        """Tests handle_request with sig verification."""
        # Arrange
        public_key = get_fixture('public_key', 'pem')
        data = get_fixture('config_init_sig_pass_request')
        smartapp = SmartApp("Test Name", "Test Description", [],
                            public_key=public_key)
        # Act
        resp = smartapp.handle_request(data['body'], data['headers'], True)
        # Assert
        assert resp

    @staticmethod
    def test_handle_request_sig_verification_missing_headers():
        """Tests handle_request with sig verification."""
        # Arrange
        public_key = get_fixture('public_key', 'pem')
        data = get_fixture('config_init_sig_pass_request')
        smartapp = SmartApp("Test Name", "Test Description", [],
                            public_key=public_key)
        # Act/Assert
        with pytest.raises(SignatureVerificationError):
            smartapp.handle_request(data['body'], [], True)

    @staticmethod
    def test_handle_request_sig_verification_fails():
        """Tests handle_request with sig verification."""
        # Arrange
        public_key = get_fixture('public_key', 'pem')
        data = get_fixture('config_init_sig_fail_request')
        smartapp = SmartApp("Test Name", "Test Description", [],
                            public_key=public_key)
        # Act/Assert
        with pytest.raises(SignatureVerificationError):
            smartapp.handle_request(data['body'], data['headers'], True)
