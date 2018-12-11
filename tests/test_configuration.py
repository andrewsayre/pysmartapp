"""Tests for the configuration module."""

import pytest


from pysmartapp.configuration import \
    ConfigurationRequest, ConfigurationInitializeResponse, \
    ConfigurationResponse


class TestConfigurationRequest:
    """Tests for the TestConfigurationRequest class."""

    @staticmethod
    def test_initialize():
        """Tests class initializes properly."""
        # Arrange
        data = {
            'installedAppId': "Installed App",
            'phase': 'Phase',
            'pageId': 'PageId',
            'previousPageId': 'PreviousPageId'
        }
        # Act
        request = ConfigurationRequest({'configurationData': data})
        # Assert
        assert request.installed_app_id == data['installedAppId']
        assert request.phase == data['phase']
        assert request.page_id == data['pageId']
        assert request.previous_page_id == data['previousPageId']


class TestConfigurationInitializeResponse:
    """Tests for the TestConfigurationInitializeResponse class."""

    @staticmethod
    def test_initialize():
        """Tests class initializes properly."""
        # Arrange
        name = "SmartApp"
        description = "SmartApp Description"
        permissions = ['test']
        app_id = "myapp"
        # Act
        response = ConfigurationInitializeResponse(
            name, description, permissions, app_id)
        # Assert

        assert response.name == name
        assert response.description == description
        assert response.permissions == permissions
        assert response.app_id == app_id

    @staticmethod
    def test_to_dict():
        """Tests the dictionary is returned properly."""
        response = ConfigurationInitializeResponse(
            "name", "description", ["perms"], "myapp")

        assert response.to_dict() == {
            'configurationData': {
                'initialize': {
                    'name': 'name',
                    'description': 'description',
                    'id': 'myapp',
                    'permissions': ['perms'],
                    'firstPageId': '1'
                }
            }
        }


class TestConfigurationResponse:
    """Tests the ConfigurationResponse class."""

    @staticmethod
    def test_to_dict_phase():
        """Tests method not implemented."""
        response = ConfigurationResponse()
        with pytest.raises(NotImplementedError):
            response.to_dict()
