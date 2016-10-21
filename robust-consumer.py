from kombu import Connection, Exchange, Queue, Consumer
import socket


rabbit_url = "amqp://localhost:5672/"

conn = Connection(rabbit_url, heartbeat=10)

exchange = Exchange("example-exchange", type="direct")

queue = Queue(name="example-queue", exchange=exchange, routing_key="BOB")


def process_message(body, message):
    print("The body is {}".format(body))
    message.ack()

consumer = Consumer(conn, queues=queue, callbacks=[process_message], accept=["text/plain"])
consumer.consume()


def establish_connection():
    revived_connection = conn.clone()
    revived_connection.ensure_connection(max_retries=3)
    channel = revived_connection.channel()
    consumer.revive(channel)
    consumer.consume()
    return revived_connection


def consume():
    new_conn = establish_connection()
    while True:
        try:
            new_conn.drain_events(timeout=2)
        except socket.timeout:
            new_conn.heartbeat_check()


def run():
    while True:
        try:
            consume()
        except conn.connection_errors:
            print("connection revived")

run()
