from aiokafka import AIOKafkaProducer
import asyncio
import logging
import requests

from base import Handler, App
from config import Config


class Producer(Handler):
    def __init__(self):
        self.producer = AIOKafkaProducer(bootstrap_servers=Config.KAFKA)

    async def start(self):
        await self.producer.start()

    async def execute(self):
        print(Config.AUTH_TOKEN)
        result = requests.get(f'{Config.API_URL}', headers={'Authorization': f'Token {Config.AUTH_TOKEN}'})
        await self.producer.send_and_wait(Config.KAFKA_TOPIC, result.text.encode())
        logging.debug(f'Send message {result.text} to Kafka with topic {Config.KAFKA_TOPIC}')

    async def stop(self):
        await self.producer.stop()


async def main():
    await App.run(Producer())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
