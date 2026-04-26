from datetime import datetime
import logging
from pawpal_system import Task
from knowledge_base import retrieve_pet_care_context


logging.basicConfig(
    filename="system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def calculate_confidence(tasks, retrieved_context) -> float:
    if not tasks:
        return 0.2

    score = 0.5

    if retrieved_context:
        score += 0.3

    if len(tasks) >= 2:
        score += 0.2

    return min(score, 1.0)


def plan_pet_tasks(user_input: str, return_steps: bool = False):
    steps = []

    if not user_input or not user_input.strip():
        logging.error("Empty user input received.")
        raise ValueError("User request cannot be empty.")

    request = user_input.lower()
    today = datetime.now()
    tasks = []

    steps.append("Step 1: Validated user input.")
    logging.info(f"Processing user input: {user_input}")

    retrieved_context = retrieve_pet_care_context(user_input)
    steps.append(f"Step 2: Retrieved {len(retrieved_context)} relevant pet-care note(s).")

    if "feed" in request or "food" in request:
        tasks.append(Task("AI Feeding", 10, "Daily", today, "08:00", priority=5))
        steps.append("Step 3: Detected feeding need and created high-priority feeding task.")

    if "walk" in request:
        tasks.append(Task("AI Walk", 30, "Daily", today, "09:00", priority=4))
        steps.append("Step 4: Detected walking need and created exercise task.")

    if "vet" in request:
        tasks.append(Task("AI Vet Visit", 60, "Once", today, "14:00", priority=5))
        steps.append("Step 5: Detected vet-related need and created high-priority scheduling task.")

    if "groom" in request or "brush" in request:
        tasks.append(Task("AI Grooming", 20, "Weekly", today, "11:00", priority=3))
        steps.append("Step 6: Detected grooming need and created weekly grooming task.")

    if "litter" in request:
        tasks.append(Task("AI Litter Cleaning", 15, "Daily", today, "10:00", priority=4))
        steps.append("Step 7: Detected litter care need and created hygiene task.")

    if not tasks:
        steps.append("Step 8: No supported pet-care tasks were detected.")

    steps.append("Specialization: Used safe pet-care planning style and avoided medical advice.")
    logging.info(f"Generated {len(tasks)} tasks.")

    if return_steps:
        return {
            "tasks": tasks,
            "retrieved_context": retrieved_context,
            "steps": steps,
            "confidence": calculate_confidence(tasks, retrieved_context),
        }

    return tasks