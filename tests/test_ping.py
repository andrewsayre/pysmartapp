"""Tests for the ping module."""

from pysmartapp.ping import PingRequest, PingResponse


class TestPingRequest:
    """Tests for the PingRequest class."""

    @staticmethod
    def test_challenge():
        """Tests the challenge is set properly."""
        challenge = "TEST"
        request = PingRequest({'pingData': {'challenge': challenge}})
        assert request.challenge == challenge


class TestPingResponse:
    """Tests for the PingResponse class."""

    @staticmethod
    def test_challenge():
        """Tests the challenge is set properly."""
        challenge = "TEST"
        response = PingResponse(challenge)
        assert response.challenge == challenge

    @staticmethod
    def test_to_dict():
        """Tests the dictionary is returned properly."""
        challenge = "TEST"
        response = PingResponse(challenge)
        assert response.to_dict() == {'pingData': {'challenge': challenge}}
