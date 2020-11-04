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
    pyautogui.press("f9")


def main():
    """Logic of the macro.
    """
    while True:
        eat_food()
        cast_spell()
        # Slightly varying the time between one cast and another helps to make
        # it harder to detect macros.
        time.sleep(random.randrange(239, 257))


if __name__ == "__main__":
    logger.info("Initializing Autocaster Macro...")
    time.sleep(10)
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Finishing Autocaster Macro...")
        sys.exit(0)
