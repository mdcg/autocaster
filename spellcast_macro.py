import logging
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
    logger.info("Initializing spellcast macro...")
    while True:
        time.sleep(10)
        eat_food()
        cast_spell()
        time.sleep(300)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Finishing spellcast macro...")
        sys.exit(0)
