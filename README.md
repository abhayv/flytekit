<p align="center">
    <img src="https://raw.githubusercontent.com/flyteorg/static-resources/main/common/flyte_circle_gradient_1_4x4.png" alt="Flyte Logo" width="100">
</p>
<h1 align="center">
    Flytekit Python
</h1>
<p align="center">
    Flytekit Python is the Python SDK built on top of Flyte
</p>
<h3 align="center">
    <a href="plugins/README.md">Plugins</a>
    <span> · </span>
    <a href="https://docs.flyte.org/en/latest/api/flytekit/contributing.html">Contribution Guide</a>
</h3>

[![PyPI version fury.io](https://badge.fury.io/py/flytekit.svg)](https://pypi.python.org/pypi/flytekit/)
[![PyPI download day](https://img.shields.io/pypi/dd/flytekit.svg)](https://pypi.python.org/pypi/flytekit/)
[![PyPI download month](https://img.shields.io/pypi/dm/flytekit.svg)](https://pypi.python.org/pypi/flytekit/)
[![PyPI total download](https://static.pepy.tech/badge/flytekit)](https://static.pepy.tech/badge/flytekit)
[![PyPI format](https://img.shields.io/pypi/format/flytekit.svg)](https://pypi.python.org/pypi/flytekit/)
[![PyPI implementation](https://img.shields.io/pypi/implementation/flytekit.svg)](https://pypi.python.org/pypi/flytekit/)
[![Codecov](https://img.shields.io/codecov/c/github/flyteorg/flytekit?style=plastic)](https://app.codecov.io/gh/flyteorg/flytekit)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/flytekit.svg)](https://pypi.python.org/pypi/flytekit/)
[![Docs](https://readthedocs.org/projects/flytekit/badge/?version=latest&style=plastic)](https://flytekit.rtfd.io)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Slack](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://slack.flyte.org)

Flytekit Python is the Python Library for easily authoring, testing, deploying, and interacting with Flyte tasks, workflows, and launch plans.

If you haven't explored Flyte yet, please refer to:
 - [Flyte homepage](https://flyte.org)
 - [Flyte core repository](https://github.com/flyteorg/flyte)

## 🚀 Quick Start

Flytekit is the core extensible library to author Flyte workflows and tasks and interact with Flyte backend services.

### Installation

```bash
pip install flytekit
```

### A Simple Example

```python
from flytekit import task, workflow

@task(cache=True, cache_version="1", retries=3)
def sum(x: int, y: int) -> int:
    return x + y

@task(cache=True, cache_version="1", retries=3)
def square(z: int) -> int:
    return z*z

@workflow
def my_workflow(x: int, y: int) -> int:
    return sum(x=square(z=x), y=square(z=y))
```

---

## 🔔 Workflow Notifications (Email, PagerDuty, Slack Webhook)

Flyte supports sending notifications when workflows succeed, fail, or abort. You can configure notifications via Email, PagerDuty, or (NEW) directly to Slack channels with a webhook.

### Email or PagerDuty Notifications

```python
from flytekit.core.notification import Email, PagerDuty
from flytekit.models.core.execution import WorkflowExecutionPhase

email_notif = Email(
    phases=[WorkflowExecutionPhase.SUCCEEDED],
    recipients_email=["your-team@email.com"]
)
pagerduty_notif = PagerDuty(
    phases=[WorkflowExecutionPhase.FAILED],
    recipients_email=["your-pagerduty@email.com"]
)
```

### Slack Webhook Notifications

To send workflow notifications directly to a Slack channel using a [Slack Incoming Webhook](https://api.slack.com/messaging/webhooks):

```python
from flytekit.core.notification_slack_webhook import SlackWebhookNotification
from flytekit.models.core.execution import WorkflowExecutionPhase

slack_notif = SlackWebhookNotification(
    phases=[WorkflowExecutionPhase.SUCCEEDED, WorkflowExecutionPhase.FAILED],
    webhook_url="https://hooks.slack.com/services/your/webhook/url",
    message="Flyte workflow has completed with phase: {phase}",
    channel="#your-channel"  # Optional: target channel, if your webhook supports it
)
```

Then, add your notification(s) to your workflow's launch plan:

```python
from flytekit import LaunchPlan

my_lp = LaunchPlan.get_or_create(
    workflow=my_workflow,
    notifications=[slack_notif, email_notif]
)
```

Notifications will be triggered when the workflow reaches the specified phases.

## 📦 Resources
- [Learn Flytekit by example](https://docs.flyte.org/en/latest/user_guide/quickstart_guide.html)
- [Flytekit API documentation](https://docs.flyte.org/en/latest/api/flytekit/docs_index.html)


## 📖 How to Contribute to Flytekit
You can find the detailed contribution guide [here](https://docs.flyte.org/en/latest/api/flytekit/contributing.html). Plugins' contribution guide is included as well.

## Code Structure
Please see the [contributor's guide](https://docs.flyte.org/en/latest/api/flytekit/contributing.html) for a quick summary of how this code is structured.

## 🐞 File an Issue
Refer to the [issues](https://github.com/flyteorg/flyte/issues) section in the contribution guide if you'd like to file an issue.

## 🔌 Flytekit Plugins
Refer to [plugins/README.md](plugins/README.md) for a list of available plugins.
There may be plugins outside of this list, but the core maintainers maintain this list.
