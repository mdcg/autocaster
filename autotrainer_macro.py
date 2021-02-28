import asyncio
import logging
import random
import sys
import time

import pyautogui

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter(
        fmt="[autohunt] %(asctime)s - %(levelname)s : %(message)s",
        datefmt="%d/%m/%Y %I:%M:%S %p",
    )
)
logger.addHandler(handler)


async def cast_spell():
    while True:
        logger.info("Healing...")
        pyautogui.hotkey("ctrl", "1")
        logger.info("Task 'cast_spell' finished! Waiting for 10 seconds...")
        await asyncio.sleep(10)


async def eat_food():
    while True:
        logger.info("Feeding...")
        pyautogui.hotkey("ctrl", "2")
        pyautogui.hotkey("ctrl", "2")
        pyautogui.hotkey("ctrl", "2")
        pyautogui.hotkey("ctrl", "2")
        logger.info("Task 'eat_food' finished! Waiting for 60 seconds...")
        await asyncio.sleep(60)


async def use_ring():
    while True:
        logger.info("Using ring...")
        pyautogui.hotkey("ctrl", "3")
        logger.info("Task 'use_ring' finished! Waiting for 1210 seconds...")
        await asyncio.sleep(1210)


async def use_pot():
    while True:
        logger.info("Using pot...")
        pyautogui.hotkey("ctrl", "4")
        await asyncio.sleep(180)
        logger.info("Task 'use_pot' finished! Waiting for 180 seconds...")

async def main():
    eat_task = asyncio.create_task(eat_food())
    ring_task = asyncio.create_task(use_ring())
    # pot_task = asyncio.create_task(use_pot())
    castspell_task = asyncio.create_task(cast_spell())
    await eat_task
    await ring_task
    # await pot_task
    await castspell_task

    while True:
        time.sleep(1000)

if __name__ == "__main__":
    try:
        logger.info("Initializing Autotrainer Macro...")
        time.sleep(5)
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Finishing Autotrainer Macro...")
        sys.exit(0)
