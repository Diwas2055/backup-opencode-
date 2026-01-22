import pytest
import respx
from httpx import Response
from main import fetch_post, Post


@respx.mock
@pytest.mark.asyncio
async def test_fetch_post_success():
    # Arrange
    url = "https://jsonplaceholder.typicode.com/posts/1"
    mock_data = {"userId": 1, "id": 1, "title": "Test Title", "body": "Test Body"}
    respx.get(url).mock(return_value=Response(200, json=mock_data))

    # Act
    post = await fetch_post(url)

    # Assert
    assert post is not None
    assert post.id == 1
    assert post.user_id == 1
    assert post.title == "Test Title"
    assert post.body == "Test Body"


@respx.mock
@pytest.mark.asyncio
async def test_fetch_post_not_found():
    # Arrange
    url = "https://jsonplaceholder.typicode.com/posts/999"
    respx.get(url).mock(return_value=Response(404))

    # Act
    post = await fetch_post(url)

    # Assert
    assert post is None


@respx.mock
@pytest.mark.asyncio
async def test_fetch_post_invalid_data():
    # Arrange
    url = "https://jsonplaceholder.typicode.com/posts/1"
    # Missing required 'title' field
    mock_data = {"userId": 1, "id": 1, "body": "Test Body"}
    respx.get(url).mock(return_value=Response(200, json=mock_data))

    # Act
    post = await fetch_post(url)

    # Assert
    assert post is None
