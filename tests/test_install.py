""""Tests for the install module."""

from pysmartapp.const import LIFECYCLE_INSTALL
from pysmartapp.install import InstallRequest

from .utilities import get_fixture


class TestInstallRequest:
    """Tests for the InstallRequest class."""

    @staticmethod
    def test_init():
        """Tests the init method."""
        # Arrange
        data = get_fixture('install_request')
        # Act
        req = InstallRequest(data)
        # Assert
        assert req.install_data_raw == data['installData']
        assert req.lifecycle == LIFECYCLE_INSTALL
        assert req.execution_id == data['executionId']
        assert req.locale == data['locale']
        assert req.version == data['version']
        assert req.installed_app_id == '8a0dcdc9-1ab4-4c60-9de7-cb78f59a1121'
        assert req.location_id == 'e675a3d9-2499-406c-86dc-8a492a886494'
        assert req.installed_app_config ==\
            data['installData']['installedApp']['config']
        assert req.settings == data['settings']
        assert req.auth_token == '580aff1f-f0f1-44e0-94d4-e68bf9c2e768'
        assert req.refresh_token == 'ad58374e-9d6a-4457-8488-a05aa8337ab3'
