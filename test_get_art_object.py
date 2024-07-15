import requests
import pytest
from pydantic import ValidationError
from config import BASE_URL, logger
from models import ArtObject


def test_get_art_object_by_id():
    object_id = 436121  # Пример существующего ID
    response = requests.get(f"{BASE_URL}/objects/{object_id}")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    logger.info(f"Request URL: {response.url}")
    logger.info(f"Response: {response.json()}")

    try:
        art_object = ArtObject(**response.json())
        logger.info(f"Art object validated successfully: {art_object}")
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        pytest.fail(f"Validation error: {e}")


def test_get_nonexistent_art_object():
    object_id = 999999999  # Пример несуществующего ID
    response = requests.get(f"{BASE_URL}/objects/{object_id}")

    assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    logger.info(f"Request URL: {response.url}")
    logger.info(f"Response: {response.json()}")


if __name__ == "__main__":
    pytest.main()
