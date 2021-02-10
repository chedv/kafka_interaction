import os


class Config:
    DEBUG = os.environ.get('DEBUG', True)

    WORK_DELAY = os.environ.get('TIME_DELAY', 30)

    API_URL = os.environ.get('API_URL')

    AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

    KAFKA = os.environ.get('KAFKA', '127.0.0.1:9092')

    KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC', 'gps-tracks')
