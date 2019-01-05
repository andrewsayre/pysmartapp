""""Tests for the uninstall module."""

from pysmartapp.const import LIFECYCLE_UNINSTALL
from pysmartapp.uninstall import UninstallRequest

from .utilities import get_fixture


class TestUninstallRequest:
    """Tests for the UninstallRequest class."""

    @staticmethod
    def test_init():
        """Tests the init method."""
        # Arrange
        data = get_fixture('uninstall_request')
        # Act
        req = UninstallRequest(data)
        # Assert
        assert req.uninstall_data_raw == data['uninstallData']
        assert req.lifecycle == LIFECYCLE_UNINSTALL
        assert req.execution_id == data['executionId']
        assert req.locale == data['locale']
        assert req.version == data['version']
        assert req.installed_app_id == '8a0dcdc9-1ab4-4c60-9de7-cb78f59a1121'
        assert req.location_id == 'e675a3d9-2499-406c-86dc-8a492a886494'
        assert req.installed_app_config == \
            data['uninstallData']['installedApp']['config']
        assert req.settings == data['settings']
