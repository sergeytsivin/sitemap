from __future__ import unicode_literals

from django.core.management.base import BaseCommand
import pika


class Command(BaseCommand):
    help = 'Consume some messages'

    def handle(self, *args, **options):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')

        def callback(ch, method, properties, body):
            print('received a message: %s' % body)

        channel.basic_consume(callback, queue='hello', no_ack=True)
        self.stdout.write('Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
