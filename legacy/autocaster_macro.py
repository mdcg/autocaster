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
        fmt="[autocaster] %(asctime)s - %(levelname)s : %(message)s",
        datefmt="%d/%m/%Y %I:%M:%S %p",
    )
)
logger.addHandler(handler)


async def make_rune():
    while True:
        logger.info("Creating rune...")
        pyautogui.hotkey("ctrl", "1")
        await asyncio.sleep(2)
        pyautogui.hotkey("ctrl", "1")
        await asyncio.sleep(2)
        pyautogui.hotkey("ctrl", "1")
        logger.info("Task 'make_rune' finished!")
        await asyncio.sleep(random.randrange(120, 140))


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


async def look_to_some_direction():
    logger.info("Looking for some direction...")
    pyautogui.press("right")
    await asyncio.sleep(1)
    pyautogui.press("left")
    directions = ["up", "right", "down"]
    pyautogui.hotkey("ctrl", random.choice(directions))
    await asyncio.sleep(1)
    pyautogui.hotkey("ctrl", "right")


async def main():
    eat_task = asyncio.create_task(eat_food())
    ring_task = asyncio.create_task(use_ring())
    make_rune_task = asyncio.create_task(make_rune())
    look_to_some_direction_task = asyncio.create_task(look_to_some_direction())

    await eat_task
    await ring_task
    await make_rune_task
    await look_to_some_direction_task

    while True:
        time.sleep(1000)

if __name__ == "__main__":
    try:
        logger.info("Initializing Autocaster Macro...")
        time.sleep(5)
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Finishing Autocaster Macro...")
        sys.exit(0)
