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
    time.sleep(1)


def main():
    """Logic of the macro.
    """
    while True:
        eat_food()
        cast_spell()
        cast_spell()
        time.sleep(250)


if __name__ == "__main__":
    logger.info("Initializing spellcast macro...")
    time.sleep(10)
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Finishing spellcast macro...")
        sys.exit(0)
