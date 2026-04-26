from ai_agent import plan_pet_tasks


TEST_CASES = [
    {
        "input": "Buddy needs feeding and a walk",
        "expected": ["AI Feeding", "AI Walk"],
    },
    {
        "input": "Milo needs litter cleaning and food",
        "expected": ["AI Litter Cleaning", "AI Feeding"],
    },
    {
        "input": "My dog needs grooming and a vet visit",
        "expected": ["AI Grooming", "AI Vet Visit"],
    },
    {
        "input": "My pet needs attention",
        "expected": [],
    },
    {
        "input": "",
        "expected_error": ValueError,
    },
]


def run_evaluation():
    passed = 0
    total = len(TEST_CASES)

    print("\nApplied AI System Evaluation\n")

    for i, case in enumerate(TEST_CASES, start=1):
        try:
            result = plan_pet_tasks(case["input"], return_steps=True)
            task_names = [task.description for task in result["tasks"]]
            expected = case.get("expected", [])

            success = all(item in task_names for item in expected)

            if success:
                passed += 1
                status = "PASS"
            else:
                status = "FAIL"

            print(f"Test {i}: {status}")
            print(f"Input: {case['input']}")
            print(f"Expected: {expected}")
            print(f"Actual: {task_names}")
            print(f"Confidence: {result['confidence']:.2f}")
            print("-" * 40)

        except Exception as error:
            if "expected_error" in case and isinstance(error, case["expected_error"]):
                passed += 1
                print(f"Test {i}: PASS")
                print("Input: Empty input")
                print(f"Expected error: {case['expected_error'].__name__}")
                print("-" * 40)
            else:
                print(f"Test {i}: FAIL")
                print(f"Unexpected error: {error}")
                print("-" * 40)

    print(f"\nSummary: {passed} out of {total} tests passed.")


if __name__ == "__main__":
    run_evaluation()