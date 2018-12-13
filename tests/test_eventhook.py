"""Tests for the EventHook file."""

from pysmartapp.eventhook import EventHook


class TestEventHook:
    """Tests for the EventHook class."""

    @staticmethod
    def test_add():
        """Tests adding an event handler."""
        hook = EventHook()
        hook += TestEventHook.__handler
        assert TestEventHook.__handler in hook.handlers

    @staticmethod
    def test_remove():
        """Tests removing an event handler."""
        hook = EventHook()
        hook += TestEventHook.__handler
        hook -= TestEventHook.__handler
        assert TestEventHook.__handler not in hook.handlers

    @staticmethod
    def test_fire():
        """Tests firing an event handler."""
        hook = EventHook()
        fired = False

        def handler():
            nonlocal fired
            fired = True

        hook += handler
        hook.fire()
        assert fired

    @staticmethod
    def __handler():
        pass
