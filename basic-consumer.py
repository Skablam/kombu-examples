from kombu import Connection, Exchange, Queue, Consumer

rabbit_url = "amqp://localhost:5672/"

conn = Connection(rabbit_url)

exchange = Exchange("example-exchange", type="direct")

queue = Queue(name="example-queue", exchange=exchange, routing_key="BOB")


def process_message(body, message):
    print("The body is {}".format(body))
    message.ack()


with Consumer(conn, queues=queue, callbacks=[process_message], accept=["text/plain"]):
    conn.drain_events(timeout=2)
