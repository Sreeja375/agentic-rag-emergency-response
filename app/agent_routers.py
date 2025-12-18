"""
Agent Router
-------------
Decides which AI agents should be triggered
based on the user's emergency input.
"""

from typing import List


def route_agents(user_input: str) -> List[str]:
    """
    Routes emergency queries to relevant agents.

    Parameters:
        user_input (str): Emergency situation described by user

    Returns:
        List[str]: List of agent names to be executed
    """

    if not user_input:
        return ["communication"]

    text = user_input.lower()
    agents = []

    # 🩺 Medical emergencies
    medical_keywords = [
        "accident", "injury", "bleeding", "burn",
        "fracture", "unconscious", "pain", "fever"
    ]

    # 📍 Safety / location emergencies
    location_keywords = [
        "help", "lost", "harassment", "danger",
        "threat", "attack", "unsafe"
    ]

    if any(word in text for word in medical_keywords):
        agents.append("medical")

    if any(word in text for word in location_keywords):
        agents.append("location")

    # 📞 Always notify communication agent
    agents.append("communication")

    return agents
