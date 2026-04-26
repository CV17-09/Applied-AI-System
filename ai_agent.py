def plan_pet_tasks(user_input):
    tasks = []

    user_input = user_input.lower()

    if "feed" in user_input:
        tasks.append({"task": "Feed pet", "priority": "high"})
    
    if "walk" in user_input:
        tasks.append({"task": "Walk pet", "priority": "medium"})
    
    if "vet" in user_input:
        tasks.append({"task": "Schedule vet visit", "priority": "high"})
    
    return tasks