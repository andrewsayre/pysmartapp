"""Tests for the lifecycle module."""

import pytest


from pysmartapp.lifecycle import \
    LifecycleResponse, LifecycleRequest


class TestLifecycleRequest:
    """Tests for the LifecycleRequest class."""

    @staticmethod
    def test_init():
        """Tests the class initializes correctly."""
        # Arrange
        entity = {
            'lifecycle': 'lifecycle',
            'executionId': 'execution_id',
            'locale': 'locale',
            'version': 'version'
        }
        # Act
        request = LifecycleRequest(entity)
        # Assert
        assert request.lifecycle == 'lifecycle'
        assert request.execution_id == 'execution_id'
        assert request.locale == 'locale'
        assert request.version == 'version'


class TestLifecycleResponse:
    """Tests for the LifecycleResponse class."""

    @staticmethod
    def test_to_dict():
        """Tests method not implemented."""
        response = LifecycleResponse()
        with pytest.raises(NotImplementedError):
            response.to_dict()
