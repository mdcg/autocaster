import asyncio

import pyautogui

from core import logger


async def execute_macro(macro):
    while True:
        logger.info(macro)
        for _ in range(0, macro.many_times):
            pyautogui.hotkey(*macro.hotkey)
            await asyncio.sleep(macro.interval_between_hotkeys)

        await asyncio.sleep(macro.sleep_time)


async def run_tasks(flow):
    tasks = []
    for macro in flow.macros:
        tasks.append(execute_macro(macro))

    await asyncio.gather(*tasks)
