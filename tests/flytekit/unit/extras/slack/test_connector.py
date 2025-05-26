from flytekit.extend.backend.base_connector import ConnectorRegistry
from flytekit.extras.slack.connector import SlackConnector

def test_slack_connector_registered():
    found = False
    for connector in ConnectorRegistry._connectors:
        if isinstance(connector, SlackConnector):
            found = True
            break
    assert found, "SlackConnector is not registered in ConnectorRegistry"