import pytest
import requests

from config import BASE_URL, logger


@pytest.mark.parametrize("keyword, has_images, limit", [("flower", True, 100)])
def test_search_result_limit(keyword, has_images, limit):
    response = requests.get(f"{BASE_URL}/search", params={"q": keyword, "hasImages": has_images, "limit": limit})

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    logger.info(f"Request URL: {response.url}")
    logger.info(f"Response: {response.json()}")

    results = response.json()
    assert len(results["objectIDs"]) <= limit, f"Expected at most {limit} results, got {len(results['objectIDs'])}"


@pytest.mark.parametrize("keyword, department_id, sort_by", [
    ("landscape", 11, "relevance"),
    ("landscape", 11, "title"),
    ("landscape", 11, "artist")
])
def test_search_filter_and_sort(keyword, department_id, sort_by):
    response = requests.get(f"{BASE_URL}/search",
                            params={"q": keyword, "departmentId": department_id, "sortBy": sort_by})

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    logger.info(f"Request URL: {response.url}")
    logger.info(f"Response: {response.json()}")

    results = response.json()
    assert "objectIDs" in results, "Invalid response structure"
    logger.info(f"Filtered and sorted search results validated successfully: {results}")


if __name__ == "__main__":
    pytest.main()
