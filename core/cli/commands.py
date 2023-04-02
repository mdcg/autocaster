import asyncio
import time
from json.decoder import JSONDecodeError
from sys import exit

import click
from pydantic import ValidationError

from core import logger
from core.processor.flow_creator import create_commands_flow
from core.processor.task_runner import run_tasks
from core.reader.json_reader import extract_json_payload


@click.command()
@click.option("--filename", help="Macro commands filename.")
def run(filename):
    try:
        payload = extract_json_payload(filename)
    except FileNotFoundError:
        logger.error(f"'{filename}' not found.")
        exit(1)

    except JSONDecodeError as err:
        logger.error(str(err))
        exit(1)

    try:
        flow = create_commands_flow(payload)
    except ValidationError as err:
        logger.error(str(err))
        exit(1)

    logger.info("Running macros in 10 seconds...")
    time.sleep(10)
    asyncio.run(run_tasks(flow))
