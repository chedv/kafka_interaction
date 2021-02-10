from time import time
from abc import ABC, abstractmethod
import logging

from config import Config


class Handler(ABC):
    @abstractmethod
    async def execute(self):
        pass

    @abstractmethod
    async def start(self):
        pass

    @abstractmethod
    async def stop(self):
        pass


class App:
    @staticmethod
    async def run(handler: Handler):
        await handler.start()
        curr_time = time()

        if Config.DEBUG:
            logging.root.setLevel(logging.DEBUG)
        logging.info(f'Process was started')

        while True:
            try:
                if curr_time <= time() - Config.WORK_DELAY:
                    await handler.execute()
                    curr_time = time()
            except Exception as e:
                logging.info(f'Process was stopped due to the exception: {e}')
                await handler.stop()
                break
