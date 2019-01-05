""""Tests for the config module."""

import pytest

from pysmartapp.config import ConfigRequest
from pysmartapp.const import LIFECYCLE_CONFIG, LIFECYCLE_CONFIG_INIT

from .utilities import get_fixture


class TestConfigRequest:
    """Tests for the ConfigRequest class."""

    @staticmethod
    def test_init():
        """Tests the init method."""
        # Arrange
        data = get_fixture('config_init_request')
        # Act
        req = ConfigRequest(data)
        # Assert
        assert req.config_data_raw == data['configurationData']
        assert req.lifecycle == LIFECYCLE_CONFIG
        assert req.execution_id == data['executionId']
        assert req.locale == data['locale']
        assert req.version == data['version']
        assert req.installed_app_id == \
            data['configurationData']['installedAppId']
        assert req.phase == LIFECYCLE_CONFIG_INIT
        assert req.page_id == ''
        assert req.previous_page_id == ''

    @staticmethod
    @pytest.mark.asyncio
    async def test_process_invalid():
        """Tests the process method for an invalid phase"""
        # Arrange
        data = get_fixture('config_init_request')
        data['configurationData']['phase'] = "UNKNOWN"
        # Act
        req = ConfigRequest(data)
        # Assert
        with pytest.raises(ValueError):
            await req.process(None, validate_signature=False)
