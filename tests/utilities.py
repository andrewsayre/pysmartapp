"""Testing utilities."""
import json


def get_fixture(file: str, ext: str = 'json'):
    """Load a fixtures file."""
    file_name = F"tests/fixtures/{file}.{ext}"
    with open(file_name, encoding="utf-8") as open_file:
        if ext == 'json':
            return json.load(open_file)
        return open_file.read()


def get_dispatch_handler(smartapp):
    """Get a handler to mock in the dispatcher."""
    async def handler(req, resp, app):
        handler.fired = True
        assert app == smartapp
    handler.fired = False
    return handler
