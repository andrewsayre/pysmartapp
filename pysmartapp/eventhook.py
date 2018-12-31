"""Define the event hook module."""


class EventHook:
    """Define the EventHook subscriber bag."""

    def __init__(self):
        """Initialize a new instance of the EventHook class."""
        self.__handlers = []

    def __iadd__(self, handler):
        """Add an event handler."""
        if handler not in self.__handlers:
            self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        """Remove an event handler."""
        if handler in self.__handlers:
            self.__handlers.remove(handler)
        return self

    def fire(self, *args, **keywargs):
        """Invoke the event handlers."""
        for handler in self.__handlers:
            handler(*args, **keywargs)

    @property
    def handlers(self):
        """Get the bound handlers."""
        return self.__handlers
