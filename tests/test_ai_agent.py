from ai_agent import plan_pet_tasks

def test_ai_generates_tasks():
    result = plan_pet_tasks("feed and walk my dog")
    assert len(result) >= 2

def test_empty_input():
    try:
        plan_pet_tasks("")
        assert False
    except ValueError:
        assert True