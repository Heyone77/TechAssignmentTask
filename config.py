import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Базовый URL API
BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1"