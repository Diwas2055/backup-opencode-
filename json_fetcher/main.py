import asyncio
import logging
import sys
from typing import Final

import httpx
from pydantic import BaseModel, Field, ValidationError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

API_URL: Final[str] = "https://jsonplaceholder.typicode.com/posts/1"


class Post(BaseModel):
    """Pydantic model for a Post from JSONPlaceholder."""

    user_id: int = Field(alias="userId")
    id: int
    title: str
    body: str


async def fetch_post(url: str) -> Post | None:
    """
    Fetch a post from the given URL and validate it using Pydantic.

    Args:
        url: The API endpoint URL.

    Returns:
        A Post object if successful, None otherwise.
    """
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.get(url)
            response.raise_for_status()

            # Parse and validate the response
            data = response.json()
            post = Post.model_validate(data)

            logger.info("Successfully fetched and validated post ID: %d", post.id)
            return post

        except httpx.HTTPStatusError as exc:
            logger.error(
                "HTTP error occurred while fetching post: %s - %s",
                exc.response.status_code,
                exc.response.text,
            )
        except httpx.RequestError as exc:
            logger.error(
                "An error occurred while requesting %s: %s", exc.request.url, exc
            )
        except ValidationError as exc:
            logger.error("Data validation error: %s", exc)
        except Exception:
            logger.exception("An unexpected error occurred")

    return None


async def main() -> None:
    """Main entry point for the script."""
    logger.info("Starting fetch from %s", API_URL)
    post = await fetch_post(API_URL)

    if post:
        print("\n--- Fetched Post Data ---")
        print(f"ID:      {post.id}")
        print(f"User ID: {post.user_id}")
        print(f"Title:   {post.title}")
        print(f"Body:    {post.body}")
        print("-------------------------\n")
    else:
        print("Failed to fetch or validate post data.")
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Script interrupted by user")
        sys.exit(0)
