"""Tests for the SmartApp file."""

import asyncio

import pytest

from pysmartapp.dispatch import Dispatcher
from pysmartapp.errors import (
    SignatureVerificationError, SmartAppNotRegisteredError)
from pysmartapp.smartapp import SmartApp, SmartAppManager

from .utilities import get_dispatch_handler, get_fixture

INSTALLED_APP_ID = '8a0dcdc9-1ab4-4c60-9de7-cb78f59a1121'
APP_ID = 'f6c071aa-6ae7-463f-b0ad-8620ac23140f'


class TestSmartApp:
    """Tests for the SmartApp class."""

    @staticmethod
    def test_initialize():
        """Tests the property initialization."""
        # Arrange
        path = '/my/test/path'
        public_key = 'test'
        dispatcher = Dispatcher()
        # Act
        app = SmartApp(path=path, public_key=public_key,
                       dispatcher=dispatcher)
        # Assert
        assert app.path == path
        assert app.public_key == public_key
        assert app.dispatcher == dispatcher
        assert app.permissions == []
        assert app.config_app_id == 'app'

    @staticmethod
    def test_setters():
        """Tests the property setters."""
        # Arrange
        app = SmartApp()
        # Act
        app.app_id = "Test"
        app.config_app_id = "Test Config Id"
        app.description = "Description"
        app.name = "Name"
        # Assert
        assert app.app_id == "Test"
        assert app.config_app_id == "Test Config Id"
        assert app.description == "Description"
        assert app.name == "Name"

    @staticmethod
    @pytest.mark.asyncio
    async def test_ping(smartapp):
        """Tests the ping lifecycle event."""
        # Arrange
        request = get_fixture("ping_request")
        expected_response = get_fixture("ping_response")
        handler = get_dispatch_handler(smartapp)
        smartapp.connect_ping(handler)
        # Act
        response = await smartapp.handle_request(request)
        # ensure dispatched tasks complete
        await asyncio.gather(*smartapp.dispatcher.last_sent)
        # Assert
        assert handler.fired
        assert response == expected_response

    @staticmethod
    @pytest.mark.asyncio
    async def test_config_init(smartapp):
        """Tests the configuration initialization lifecycle event."""
        # Arrange
        request = get_fixture("config_init_request")
        expected_response = get_fixture("config_init_response")
        handler = get_dispatch_handler(smartapp)
        smartapp.connect_config(handler)
        # Act
        response = await smartapp.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*smartapp.dispatcher.last_sent)
        # Assert
        assert handler.fired
        assert response == expected_response

    @staticmethod
    @pytest.mark.asyncio
    async def test_config_page(smartapp):
        """Tests the configuration initialization page event."""
        # Arrange
        request = get_fixture("config_page_request")
        expected_response = get_fixture("config_page_response")
        handler = get_dispatch_handler(smartapp)
        smartapp.connect_config(handler)
        # Act
        response = await smartapp.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*smartapp.dispatcher.last_sent)
        # Assert
        assert handler.fired
        assert response == expected_response

    @staticmethod
    @pytest.mark.asyncio
    async def test_install(smartapp):
        """Tests the install lifecycle event."""
        # Arrange
        request = get_fixture("install_request")
        expected_response = get_fixture("install_response")
        handler = get_dispatch_handler(smartapp)
        smartapp.connect_install(handler)
        # Act
        response = await smartapp.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*smartapp.dispatcher.last_sent)
        # Assert
        assert handler.fired
        assert response == expected_response

    @staticmethod
    @pytest.mark.asyncio
    async def test_update(smartapp):
        """Tests the update lifecycle event."""
        # Arrange
        request = get_fixture("update_request")
        expected_response = get_fixture("update_response")
        handler = get_dispatch_handler(smartapp)
        smartapp.connect_update(handler)
        # Act
        response = await smartapp.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*smartapp.dispatcher.last_sent)
        # Assert
        assert handler.fired
        assert response == expected_response

    @staticmethod
    @pytest.mark.asyncio
    async def test_event(smartapp):
        """Tests the event lifecycle event."""
        # Arrange
        request = get_fixture("event_request")
        expected_response = get_fixture("event_response")
        handler = get_dispatch_handler(smartapp)
        smartapp.connect_event(handler)
        # Act
        response = await smartapp.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*smartapp.dispatcher.last_sent)
        # Assert
        assert handler.fired
        assert response == expected_response

    @staticmethod
    @pytest.mark.asyncio
    async def test_oauth_callback(smartapp):
        """Tests the oauth_callback lifecycle event."""
        # Arrange
        request = get_fixture("oauth_callback_request")
        expected_response = get_fixture("oauth_callback_response")
        handler = get_dispatch_handler(smartapp)
        smartapp.connect_oauth_callback(handler)
        # Act
        response = await smartapp.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*smartapp.dispatcher.last_sent)
        # Assert
        assert handler.fired
        assert response == expected_response

    @staticmethod
    @pytest.mark.asyncio
    async def test_uninstall(smartapp):
        """Tests the uninstall lifecycle event."""
        # Arrange
        request = get_fixture("uninstall_request")
        expected_response = get_fixture("uninstall_response")
        handler = get_dispatch_handler(smartapp)
        smartapp.connect_uninstall(handler)
        # Act
        response = await smartapp.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*smartapp.dispatcher.last_sent)
        # Assert
        assert handler.fired
        assert response == expected_response

    @staticmethod
    @pytest.mark.asyncio
    async def test_handle_request_sig_verification():
        """Tests handle_request with sig verification."""
        # Arrange
        public_key = get_fixture('public_key', 'pem')
        data = get_fixture('config_init_sig_pass_request')
        smartapp = SmartApp(public_key=public_key)
        # Act
        resp = await smartapp.handle_request(
            data['body'], data['headers'], True)
        # Assert
        assert resp

    @staticmethod
    @pytest.mark.asyncio
    async def test_handle_request_sig_verification_missing_headers():
        """Tests handle_request with sig verification."""
        # Arrange
        public_key = get_fixture('public_key', 'pem')
        data = get_fixture('config_init_sig_pass_request')
        smartapp = SmartApp(public_key=public_key)
        # Act/Assert
        with pytest.raises(SignatureVerificationError):
            await smartapp.handle_request(data['body'], [], True)

    @staticmethod
    @pytest.mark.asyncio
    async def test_handle_request_sig_verification_fails():
        """Tests handle_request with sig verification."""
        # Arrange
        public_key = get_fixture('public_key', 'pem')
        data = get_fixture('config_init_sig_fail_request')
        smartapp = SmartApp(public_key=public_key)
        # Act/Assert
        with pytest.raises(SignatureVerificationError):
            await smartapp.handle_request(data['body'], data['headers'], True)


class TestSmartAppManager:
    """Tests for the SmartAppManager class."""

    @staticmethod
    @pytest.mark.asyncio
    async def test_handle_request_ping_not_registered(manager):
        """Tests the ping lifecycle event with no registered apps."""
        # Arrange
        request = get_fixture("ping_request")
        expected_response = get_fixture("ping_response")
        handler = get_dispatch_handler(manager)
        manager.connect_ping(handler)
        # Act
        response = await manager.handle_request(request)
        # ensure dispatched tasks complete
        await asyncio.gather(*manager.dispatcher.last_sent)
        # Assert
        assert handler.fired
        assert response == expected_response

    @staticmethod
    @pytest.mark.asyncio
    async def test_handle_request_not_registered(manager: SmartAppManager):
        """Tests processing a request when no SmartApp has been registered."""
        # Arrange
        request = get_fixture("config_init_request")
        # Act
        with pytest.raises(SmartAppNotRegisteredError) as e_info:
            await manager.handle_request(request, None, False)
        # Assert
        assert e_info.value.installed_app_id == INSTALLED_APP_ID

    @staticmethod
    @pytest.mark.asyncio
    async def test_handle_request_not_app_id(manager: SmartAppManager):
        """Tests processing a request when no SmartApp has been registered."""
        # Arrange
        request = get_fixture("config_init_sig_fail_request")['body']
        # Act
        with pytest.raises(SmartAppNotRegisteredError) as e_info:
            await manager.handle_request(request, None, False)
        # Assert
        assert e_info.value.installed_app_id == INSTALLED_APP_ID

    @staticmethod
    def test_register(manager: SmartAppManager):
        """Test register"""
        public_key = '123'
        # Act
        app = manager.register(APP_ID, public_key)
        # Assert
        assert app.app_id == APP_ID
        assert app.public_key == public_key
        assert app.path == manager.path
        assert APP_ID in manager.smartapps

    @staticmethod
    def test_register_no_app_id(manager: SmartAppManager):
        """Test register with no SmartApp app id"""
        # Act
        with pytest.raises(ValueError) as e_info:
            manager.register(None, '')
        # Assert
        assert str(e_info.value) == 'smartapp must have an app_id.'

    @staticmethod
    def test_register_twice(manager: SmartAppManager):
        """Test register with the same app twice"""
        # Arrange
        public_key = '123'
        manager.register(APP_ID, public_key)
        # Act
        with pytest.raises(ValueError) as e_info:
            manager.register(APP_ID, public_key)
        # Assert
        assert str(e_info.value) == 'smartapp already registered.'

    @staticmethod
    def test_unregister(manager: SmartAppManager):
        """Test unregister"""
        # Arrange'
        manager.register(APP_ID, '123')
        # Act
        manager.unregister(APP_ID)
        # Assert
        assert APP_ID not in manager.smartapps

    @staticmethod
    def test_unregister_no_app_id(manager: SmartAppManager):
        """Test unregister with no SmartApp app id"""
        # Act
        with pytest.raises(ValueError) as e_info:
            manager.unregister(None)
        # Assert
        assert str(e_info.value) == 'smartapp must have an app_id.'

    @staticmethod
    def test_unregister_not_registered(manager: SmartAppManager):
        """Test register with the same app twice"""
        # Act
        with pytest.raises(ValueError) as e_info:
            manager.unregister(APP_ID)
        # Assert
        assert str(e_info.value) == 'smartapp was not previously registered.'

    @staticmethod
    @pytest.mark.asyncio
    async def test_on_config(manager: SmartAppManager):
        """Tests the config event handler at the manager level."""
        # Arrange
        request = get_fixture("config_init_request")
        app = manager.register(APP_ID, 'none')
        handler = get_dispatch_handler(app)
        manager.connect_config(handler)
        # Act
        await manager.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*manager.dispatcher.last_sent)
        # Assert
        assert handler.fired

    @staticmethod
    @pytest.mark.asyncio
    async def test_on_install(manager: SmartAppManager):
        """Tests the config event handler at the manager level."""
        # Arrange
        request = get_fixture("install_request")
        app = manager.register(APP_ID, 'none')
        handler = get_dispatch_handler(app)
        manager.connect_install(handler)
        # Act
        await manager.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*manager.dispatcher.last_sent)
        # Assert
        assert handler.fired

    @staticmethod
    @pytest.mark.asyncio
    async def test_on_update(manager: SmartAppManager):
        """Tests the config event handler at the manager level."""
        # Arrange
        request = get_fixture("update_request")
        app = manager.register(APP_ID, 'none')
        handler = get_dispatch_handler(app)
        manager.connect_update(handler)
        # Act
        await manager.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*manager.dispatcher.last_sent)
        # Assert
        assert handler.fired

    @staticmethod
    @pytest.mark.asyncio
    async def test_on_event(manager: SmartAppManager):
        """Tests the config event handler at the manager level."""
        # Arrange
        request = get_fixture("event_request")
        app = manager.register(APP_ID, 'none')
        handler = get_dispatch_handler(app)
        manager.connect_event(handler)
        # Act
        await manager.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*manager.dispatcher.last_sent)
        # Assert
        assert handler.fired

    @staticmethod
    @pytest.mark.asyncio
    async def test_on_oauth_callback(manager: SmartAppManager):
        """Tests the config event handler at the manager level."""
        # Arrange
        request = get_fixture("oauth_callback_request")
        app = manager.register(APP_ID, 'none')
        handler = get_dispatch_handler(app)
        manager.connect_oauth_callback(handler)
        # Act
        await manager.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*manager.dispatcher.last_sent)
        # Assert
        assert handler.fired

    @staticmethod
    @pytest.mark.asyncio
    async def test_on_uninstall(manager: SmartAppManager):
        """Tests the config event handler at the manager level."""
        # Arrange
        request = get_fixture("uninstall_request")
        app = manager.register(APP_ID, 'none')
        handler = get_dispatch_handler(app)
        manager.connect_uninstall(handler)
        # Act
        await manager.handle_request(request, None, False)
        # ensure dispatched tasks complete
        await asyncio.gather(*manager.dispatcher.last_sent)
        # Assert
        assert handler.fired
