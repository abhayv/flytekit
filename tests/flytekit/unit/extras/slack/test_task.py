import pytest
from flytekit.extras.slack.task import SlackNotificationTask

def test_slack_notification_task_custom():
    task = SlackNotificationTask(
        name="test-slack",
        url="https://hooks.slack.com/services/T000/B000/XXXX",
        message="Workflow finished: {inputs.run_id}",
        dynamic_inputs={"run_id": str},
        show_data=True,
        show_url=True,
        description="Test Slack notification",
    )
    custom = task.get_custom(None)
    assert custom["url"].startswith("https://hooks.slack.com/services/")
    assert custom["data"]["text"] == "Workflow finished: {inputs.run_id}"
    assert custom["show_data"] is True
    assert custom["show_url"] is True
    assert custom["method"] == "POST"