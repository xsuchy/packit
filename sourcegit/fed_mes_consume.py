"""
This module is meant to be imported in API
"""
import datetime
import logging

from fedora_messaging import api


logger = logging.getLogger(__name__)


class Consumerino:
    """
    A class which provides an interface to consume messages via a callback
    """
    def __init__(self, topic):
        self.topic = topic
        timestamp = datetime.datetime.now().strftime("%Y%M%d-%H%M%S")
        self.binding = {
            'exchange': 'amq.topic',  # The AMQP exchange to bind our queue to
            'queue': f'source-git-{timestamp}',
            'routing_keys': [topic],
        }

    def consume(self, callback):
        logger.info("consuming messages on queue %s, routing keys = %s",
                    self.binding["queue"], self.binding["routing_keys"])
        api.consume(callback, self.binding)
