from .task import SlackNotificationTask
from .connector import SlackConnector  # Register the connector on import

__all__ = ["SlackNotificationTask", "SlackConnector"]