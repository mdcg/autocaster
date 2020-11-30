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


def eat_food():
    """Simple function to feed.
    """
    logger.info("Feeding...")
    for _ in range(0, 5):
        pyautogui.hotkey("ctrl", "4")


def cast_spell():
    """Evoke magic to make rune.
    """
    logger.info("Creating rune...")
    # pyautogui.press("f12")
    pyautogui.press("f9")


def look_to_some_direction():
    """Looking randomly in any direction prevents you from being "kicked" by
    inactivity.
    """
    logger.info("Looking for some direction...")
    pyautogui.press("right")
    time.sleep(1)
    pyautogui.press("left")
    directions = ["up", "down", "right", "left"]
    pyautogui.hotkey("ctrl", random.choice(directions))


def main():
    """Logic of the macro.
    """
    while True:
        look_to_some_direction()
        eat_food()
        cast_spell()
        # Slightly varying the time between one cast and another helps to make
        # it harder to detect macros.
        # time.sleep(random.randrange(222, 233))
        time.sleep(random.randrange(285, 292))


if __name__ == "__main__":
    logger.info("Initializing Autocaster Macro...")
    time.sleep(10)
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Finishing Autocaster Macro...")
        sys.exit(0)
