from aiokafka import AIOKafkaConsumer
import asyncio

from base import Handler, App
from config import Config


class Consumer(Handler):
    def __init__(self):
        self.consumer = AIOKafkaConsumer(Config.KAFKA_TOPIC, bootstrap_servers=Config.KAFKA)

    async def start(self):
        await self.consumer.start()

    async def execute(self):
        async for msg in self.consumer:
            print(f"Message {msg.value} was consumed from Kafka with topic {msg.topic}")

    async def stop(self):
        await self.consumer.stop()


async def main():
    await App.run(Consumer())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
