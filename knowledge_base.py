PET_CARE_KNOWLEDGE = [
    {
        "keyword": "feed",
        "tip": "Feeding tasks are usually high priority because pets need consistent meals."
    },
    {
        "keyword": "walk",
        "tip": "Walks support exercise and routine, especially for dogs."
    },
    {
        "keyword": "vet",
        "tip": "Vet-related tasks should be treated as high priority, but the system should not provide medical advice."
    },
    {
        "keyword": "groom",
        "tip": "Grooming tasks are usually recurring and can be scheduled weekly."
    },
    {
        "keyword": "litter",
        "tip": "Litter box cleaning is important for hygiene and should be scheduled regularly."
    }
]


def retrieve_pet_care_context(user_input: str) -> list[str]:
    """Retrieve relevant pet care guidance based on user input."""
    request = user_input.lower()
    matches = []

    for item in PET_CARE_KNOWLEDGE:
        if item["keyword"] in request:
            matches.append(item["tip"])

    return matches