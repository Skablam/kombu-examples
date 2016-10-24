kombu-examples
=====

This repository contains examples of using Python 3 and Kombu to interact with RabbitMQ. I created it to contain code
used in the following articles I have written:
* [Talking to RabbitMQ with Python and Kombu](https://medium.com/@Skablam/talking-to-rabbitmq-with-python-and-kombu-6cbee93b1298#.vrt5fuwmw)
* [Building Robust RabbitMQ Consumers with Python and Kombu: Part 1](https://medium.com/@Skablam/building-robust-rabbitmq-consumers-with-python-and-kombu-part-1-ccd660d17271#.l2n1mtxyi)
* [Building Robust RabbitMQ Consumers with Python and Kombu: Part 2](https://medium.com/@Skablam/building-robust-rabbitmq-consumers-with-python-and-kombu-part-2-e9505f56e12e#.wp8lsoqqf)

Pre-requisites
--

For these example to run it is assumed that RabbitMQ is installed and running locally on port 5672.

Quick start
--

Run:

```
pip install -r requirements.txt
```

Run the basic producer to add a message to a queue called "example-queue":

```
python basic-producer.py
```

Then run the basic consumer that will print out the message to the terminal:

```
python basic-consumer.py
```
