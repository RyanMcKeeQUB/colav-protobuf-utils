from colav_protobuf import AgentUpdate


def gen_protobuf_agent_update(
    mission_tag: str,
    agent_tag: str,
    state: AgentUpdate.State,
    timestamp: str,
):
    """Generates a protobuf message for agent_update"""
    try:
        agent_update = AgentUpdate()
        agent_update.mission_tag = mission_tag
        agent_update.agent_tag = agent_tag
        agent_update.state = state
        agent_update.timestamp = timestamp
    except Exception as e:
        raise Exception(e)

    return agent_update
