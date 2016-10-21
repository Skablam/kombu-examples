from kombu import Connection, Exchange, Queue
from kombu.mixins import ConsumerMixin

rabbit_url = "amqp://localhost:5672/"


class Worker(ConsumerMixin):
    def __init__(self, connection, queues):
        self.connection = connection
        self.queues = queues

    def get_consumers(self, Consumer, channel):
        return [Consumer(queues=self.queues,
                         callbacks=[self.on_message])]

    def on_message(self, body, message):
        print('Got message: {0}'.format(body))
        message.ack()

exchange = Exchange("example-exchange", type="direct")
queues = [Queue("example-queue", exchange, routing_key="BOB")]

with Connection(rabbit_url, heartbeat=4) as conn:
    try:
        worker = Worker(conn, queues)
        worker.run()
    except:
        raise
