from core.entities.flow import Flow


def create_commands_flow(payload):
    return Flow(macros=payload)
