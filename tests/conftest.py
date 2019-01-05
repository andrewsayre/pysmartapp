"""Define common test configuraiton."""

import pytest

from pysmartapp.smartapp import SmartApp, SmartAppManager


@pytest.fixture
def smartapp() -> SmartApp:
    """Fixture for testing against the SmartApp class."""
    app = SmartApp()
    app.name = 'SmartApp'
    app.description = 'SmartApp Description'
    app.permissions.append('l:devices')
    app.config_app_id = 'myapp'
    return app


@pytest.fixture
def manager() -> SmartAppManager:
    """Fixture for testing against the SmartAppManager class."""
    return SmartAppManager('/path/to/app')


@pytest.fixture
def handler():
    """Fixture handler to mock in the dispatcher."""
    def target(*args, **kwargs):
        target.args = args
        target.kwargs = kwargs
        target.fired = True
    target.fired = False
    return target


@pytest.fixture
def async_handler():
    """Fixture async handler to mock in the dispatcher."""
    async def target(*args, **kwargs):
        target.args = args
        target.kwargs = kwargs
        target.fired = True
    target.fired = False
    return target
