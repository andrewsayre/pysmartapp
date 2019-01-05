"""Define common test configuraiton."""

import pytest

from pysmartapp.dispatch import Dispatcher
from pysmartapp.smartapp import SmartApp, SmartAppManager


@pytest.fixture
def smartapp(event_loop) -> SmartApp:
    """Fixture for testing against the SmartApp class."""
    app = SmartApp(dispatcher=Dispatcher(loop=event_loop))
    app.name = 'SmartApp'
    app.description = 'SmartApp Description'
    app.permissions.append('l:devices')
    app.config_app_id = 'myapp'
    return app


@pytest.fixture
def manager(event_loop) -> SmartAppManager:
    """Fixture for testing against the SmartAppManager class."""
    return SmartAppManager('/path/to/app',
                           dispatcher=Dispatcher(loop=event_loop))


@pytest.fixture
def handler():
    """Fixture handler to mock in the dispatcher."""
    def target(*args, **kwargs):
        target.fired = True
        target.args = args
        target.kwargs = kwargs
    target.fired = False
    return target


@pytest.fixture
def async_handler():
    """Fixture async handler to mock in the dispatcher."""
    async def target(*args, **kwargs):
        target.fired = True
        target.args = args
        target.kwargs = kwargs
    target.fired = False
    return target
