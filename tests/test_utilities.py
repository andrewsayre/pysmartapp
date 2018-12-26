"""Tests for the utilities module."""

import pytest

from pysmartapp import utilities


def test_create_request_invalid():
    """Tests the create_request method."""
    # Arrange
    data = {'lifecycle': 'UNKNOWN'}
    # Act/Assert
    with pytest.raises(ValueError):
        utilities.create_request(data)
