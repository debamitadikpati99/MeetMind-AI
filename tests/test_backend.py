from backend.ai_service import analyze_meeting


def test_analyze_meeting_returns_expected_sections():
    transcript = """
    Team update: We completed the project structure and finished the dashboard prototype.
    Priya will handle the design review on Friday, and Daniel will test the login flow before the launch.
    We decided to finalize the API integration and prepare the demo for next Monday.
    """

    result = analyze_meeting(transcript)

    assert "summary" in result
    assert "decisions" in result
    assert "action_items" in result
    assert "topics" in result
    assert isinstance(result["action_items"], list)
    assert len(result["action_items"]) >= 1
