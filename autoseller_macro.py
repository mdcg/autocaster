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
        fmt="[autoseller] %(asctime)s - %(levelname)s : %(message)s",
        datefmt="%d/%m/%Y %I:%M:%S %p",
    )
)
logger.addHandler(handler)


def look_to_some_direction():
    """Looking randomly in any direction prevents you from being "kicked" by
    inactivity.
    """
    logger.info("Looking for some direction...")
    directions = ["up", "down", "right", "left"]
    pyautogui.hotkey("ctrl", random.choice(directions))


def send_message():
    """Send the message you want on the trade channel.
    """
    logger.info("Sending message...")
    pyautogui.write(">>> Enter you message here <<<", interval=0.25) 
    time.sleep(random.randrange(120, 135))


def main():
    """Logic of the macro.
    """
    while True:
        look_to_some_direction()
        send_message()


if __name__ == "__main__":
    logger.info("Initializing Autoseller Macro...")
    time.sleep(10)
    try:
        main()
    except KeyboardInterrupt:
        logger.info("Finishing Autoseller Macro...")
        sys.exit(0)
