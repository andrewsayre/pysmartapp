"""Define tests for the Dispatch module."""

import asyncio

import pytest

from pysmartapp.dispatch import Dispatcher


class TestDispatcher:
    """Define tests for the dispatcher class."""

    @staticmethod
    @pytest.mark.asyncio
    async def test_connect(handler):
        """Tests the connect function."""
        # Arrange
        dispatcher = Dispatcher()
        # Act
        dispatcher.connect('TEST', handler)
        # Assert
        assert handler in dispatcher.signals['TEST']

    @staticmethod
    @pytest.mark.asyncio
    async def test_disconnect(handler):
        """Tests the disconnect function."""
        # Arrange
        dispatcher = Dispatcher()
        disconnect = dispatcher.connect('TEST', handler)
        # Act
        disconnect()
        # Assert
        assert handler not in dispatcher.signals['TEST']

    @staticmethod
    @pytest.mark.asyncio
    async def test_already_disconnected(handler):
        """Tests that disconnect can be called more than once."""
        # Arrange
        dispatcher = Dispatcher()
        disconnect = dispatcher.connect('TEST', handler)
        disconnect()
        # Act
        disconnect()
        # Assert
        assert handler not in dispatcher.signals['TEST']

    @staticmethod
    @pytest.mark.asyncio
    async def test_send_async_handler(async_handler):
        """Tests sending to async handlers."""
        # Arrange
        dispatcher = Dispatcher()
        dispatcher.connect('TEST', async_handler)
        # Act
        await asyncio.gather(*dispatcher.send('TEST'))
        # Assert
        assert async_handler.fired

    @staticmethod
    @pytest.mark.asyncio
    async def test_send(handler):
        """Tests sending to async handlers."""
        # Arrange
        dispatcher = Dispatcher()
        dispatcher.connect('TEST', handler)
        args = object()
        # Act
        await asyncio.gather(*dispatcher.send('TEST', args))
        # Assert
        assert handler.fired
        assert handler.args[0] == args

    @staticmethod
    @pytest.mark.asyncio
    async def test_custom_connect_and_send(handler):
        """Tests using the custom connect and send implementations."""
        # Arrange
        test_signal = 'PREFIX_TEST'
        stored_target = None

        def connect(signal, target):
            assert signal == test_signal
            nonlocal stored_target
            stored_target = target

            def disconnect():
                nonlocal stored_target
                stored_target = None
            return disconnect

        def send(signal, *args):
            assert signal == test_signal
            stored_target(*args)  # pylint:disable=not-callable

        dispatcher = Dispatcher(connect=connect, send=send,
                                signal_prefix='PREFIX_')

        # Act
        dispatcher.connect('TEST', handler)
        dispatcher.send('TEST')
        # Assert
        assert handler.fired
