from datetime import datetime
from pawpal_system import Task
import logging

logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def plan_pet_tasks(user_input):
    # ✅ Handle empty input (fixes your failing test)
    if not user_input or not user_input.strip():
        logging.error("Empty user input received.")
        raise ValueError("User request cannot be empty.")

    tasks = []
    request = user_input.lower()
    today = datetime.now()

    logging.info(f"Processing user input: {user_input}")

    if "feed" in request:
        tasks.append(Task("AI Feeding", 10, "Daily", today, "08:00", priority=5))

    if "walk" in request:
        tasks.append(Task("AI Walk", 30, "Daily", today, "09:00", priority=4))

    if "vet" in request:
        tasks.append(Task("AI Vet Visit", 60, "Once", today, "14:00", priority=5))

    if "groom" in request or "brush" in request:
        tasks.append(Task("AI Grooming", 20, "Weekly", today, "11:00", priority=3))

    logging.info(f"Generated {len(tasks)} tasks.")

    return tasks