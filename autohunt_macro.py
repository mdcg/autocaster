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


async def eat_food():
    while True:
        logger.info("Feeding...")
        await asyncio.sleep(60)
        pyautogui.hotkey("ctrl", "4")
        pyautogui.hotkey("ctrl", "4")
        pyautogui.hotkey("ctrl", "4")
        pyautogui.hotkey("ctrl", "4")
        logger.info("Task 'eat_food' finished! Waiting for 60 seconds...")


async def use_pot():
    while True:
        logger.info("Using pot...")
        await asyncio.sleep(178)
        pyautogui.press("f5")
        await asyncio.sleep(2)
        pyautogui.press("f5")
        logger.info("Using pot...")


async def cast_spell():
    while True:
        logger.info("Healing...")
        await asyncio.sleep(15)
        pyautogui.press("f9")
        logger.info("Task 'cast_spell' finished! Waiting for 30 seconds...")

async def cast_exori():
    while True:
        logger.info("Exori!")
        await asyncio.sleep(70)
        pyautogui.press("f8")
        logger.info("Task 'cast_spell' finished! Waiting for 30 seconds...")


async def attack():
    # while True:
    logger.info("Attack!")
    pyautogui.hotkey("ctrl", random.choice(("q", "e")))
    await asyncio.sleep(5)
    pyautogui.press("esc")
    logger.info("Task 'attack' finished! Waiting for 3 seconds...")


async def walk():
    while True:
        logger.info("Walk...")
        # await asyncio.sleep(5)
        await random_walk(random_direction())
        await random_walk(random_direction())
        await random_walk(random_direction())
        await random_walk(random_direction())
        logger.info("Task 'random_walk' finished! Waiting for 5 seconds...")


def random_direction():
    return random.choice((
        ("down", "left"),
        ("down", "right"),
        ("up", "right"),
        ("up", "left"),
    ))

async def random_walk(sides):
    await attack()
    times = random.randrange(30, 70)
    logger.info(f"Walking for {times} times")
    for _ in range(0, times):
        side = random.choice(sides)
        pyautogui.press(side)

    await attack()

async def main():
    eat_task = asyncio.create_task(eat_food())
    castspell_task = asyncio.create_task(cast_spell())
    random_walk_task = asyncio.create_task(walk())
    # attack_task = asyncio.create_task(attack())
    exori = asyncio.create_task(cast_exori())
    pot = asyncio.create_task(use_pot())
    await eat_task
    await castspell_task
    await exori
    await pot
    # await attack_task
    await random_walk_task

    while True:
        time.sleep(1000)


if __name__ == "__main__":
    try:
        logger.info("Initializing Autohunt Macro...")
        time.sleep(5)
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Finishing Autohunt Macro...")
        sys.exit(0)
