""""Tests for the event module."""

from pysmartapp.event import EventRequest, Event
from pysmartapp.consts import LIFECYCLE_EVENT, EVENT_TYPE_DEVICE

from .utilities import get_fixture


class TestEventRequest:
    """Tests for the EventRequest class."""

    @staticmethod
    def test_init():
        """Tests the init method."""
        # Arrange
        data = get_fixture('event_request')
        # Act
        req = EventRequest(data)
        # Assert
        assert req.event_data_raw == data['eventData']
        assert req.lifecycle == LIFECYCLE_EVENT
        assert req.execution_id == data['executionId']
        assert req.locale == data['locale']
        assert req.version == data['version']
        assert req.installed_app_id == 'd692699d-e7a6-400d-a0b7-d5be96e7a564'
        assert req.location_id == 'e675a3d9-2499-406c-86dc-8a492a886494'
        assert req.installed_app_config == {}
        assert req.settings == data['settings']
        assert req.auth_token == 'f01894ce-013a-434a-b51e-f82126fd72e4'
        assert len(req.events) == 1


class TestEvent:
    """Tests for the Event class."""

    @staticmethod
    def test_init():
        """Tests the init method."""
        # Arrange
        data = get_fixture('event_request')['eventData']['events'][0]
        # Act
        evt = Event(data)
        # Assert
        assert evt.event_type == EVENT_TYPE_DEVICE
        assert evt.subscription_name == 'motion_sensors'
        assert evt.event_id == '736e3903-001c-4d40-b408-ff40d162a06b'
        assert evt.location_id == '499e28ba-b33b-49c9-a5a1-cce40e41f8a6'
        assert evt.device_id == '6f5ea629-4c05-4a90-a244-cc129b0a80c3'
        assert evt.component_id == 'main'
        assert evt.capability == 'motionSensor'
        assert evt.attribute == 'motion'
        assert evt.value == 'active'
        assert evt.state_change
