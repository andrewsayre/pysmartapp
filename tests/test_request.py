"""Tests for the requests module."""

import pytest

from pysmartapp.request import EmptyDataResponse, Request, Response

from .utilities import get_fixture


class TestResponse:
    """Tests for the Response class."""

    @staticmethod
    def test_to_data():
        """Tests the to_data method."""
        resp = Response()
        with pytest.raises(NotImplementedError):
            resp.to_data()


class TestEmptyDataResponse:
    """Tests for the EmptyDataResponse class."""

    @staticmethod
    def test_init():
        """Tests the init method."""
        resp = EmptyDataResponse('tag')
        assert resp.name == 'tag'

    @staticmethod
    def test_to_data():
        """Tests the to_data method."""
        resp = EmptyDataResponse('tag')
        result = resp.to_data()
        assert result == {'tag': {}}

    @staticmethod
    def test_name():
        """Tests the name setter."""
        resp = EmptyDataResponse('tag')
        resp.name = 'tag2'
        assert resp.name == 'tag2'


class TestRequest:
    """Tests for the Request class."""

    @staticmethod
    @pytest.mark.asyncio
    async def test_process_raises():
        """Tests the to_data method."""
        # Arrange
        data = get_fixture('ping_request')
        resp = Request(data)
        # Act/Assert
        with pytest.raises(NotImplementedError):
            await resp.process(None, validate_signature=False)
