import requests
import pytest
from pydantic import ValidationError
from config import BASE_URL, logger
from models import ArtObject, ArtObjectList


def test_search_art_objects():
    keyword = "sunflower"
    response = requests.get(f"{BASE_URL}/search", params={"q": keyword})

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    logger.info(f"Request URL: {response.url}")
    logger.info(f"Response: {response.json()}")

    try:
        results = ArtObjectList(**response.json())
        logger.info(f"Search results validated successfully: {results}")
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        pytest.fail(f"Validation error: {e}")

    if results.total > 0:
        object_id = results.objectIDs[0]
        response = requests.get(f"{BASE_URL}/objects/{object_id}")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        try:
            art_object = ArtObject(**response.json())
            logger.info(f"Art object validated successfully: {art_object}")
        except ValidationError as e:
            logger.error(f"Validation error: {e}")
            pytest.fail(f"Validation error: {e}")


if __name__ == "__main__":
    pytest.main()
