import pytest


@pytest.mark.asyncio
async def test_ssl_setup(test_app, test_client):
    response = await test_client.get("/")
    assert response.status_code == 200
    assert "Hello" in response.json()["message"]
