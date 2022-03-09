
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient
from ferment_pi.main import app


@pytest.fixture
def client():
    client = TestClient(app)
    return client


@pytest.fixture
def mock_get_session(mocker):
    mock_ses = mocker.patch("ferment_pi.database.get_session")
    mock_entry = MagicMock()

    mock_entry.id = 99
    mock_entry.temperature = "20"
    mock_entry.humidity = "33"
    mock_entry.created_time = "2022-03-08T17:45:12.586682"

    (mock_ses.return_value.__enter__.return_value.query.return_value
     .order_by.return_value.first.return_value) = mock_entry
    return mock_ses
