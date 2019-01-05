""""Tests for the update module."""

from pysmartapp.const import LIFECYCLE_UPDATE
from pysmartapp.update import UpdateRequest

from .utilities import get_fixture


class TestUpdateRequest:
    """Tests for the UpdateRequest class."""

    @staticmethod
    def test_init():
        """Tests the init method."""
        # Arrange
        data = get_fixture('update_request')
        # Act
        req = UpdateRequest(data)
        # Assert
        assert req.update_data_raw == data['updateData']
        assert req.lifecycle == LIFECYCLE_UPDATE
        assert req.execution_id == data['executionId']
        assert req.locale == data['locale']
        assert req.version == data['version']
        assert req.installed_app_id == '8a0dcdc9-1ab4-4c60-9de7-cb78f59a1121'
        assert req.location_id == 'e675a3d9-2499-406c-86dc-8a492a886494'
        assert req.installed_app_config == \
            data['updateData']['installedApp']['config']
        assert req.settings == data['settings']
        assert req.auth_token == '4ebd8d9f-53b0-483f-a989-4bde30ca83c0'
        assert req.refresh_token == '6e3bbf5f-b68d-4250-bbc9-f7151016a77f'
