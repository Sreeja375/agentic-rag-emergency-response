def route_agents(user_input):
    tasks = []
    if any(word in user_input.lower() for word in ["accident", "bleeding", "injury"]):
        tasks.append("medical")
    if any(word in user_input.lower() for word in ["lost", "help", "harassment"]):
        tasks.append("location")
    tasks.append("communication")
    return tasks
