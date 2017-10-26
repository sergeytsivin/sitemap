from __future__ import unicode_literals

from django.core.management.base import BaseCommand
import pika


class Command(BaseCommand):
    help = 'Produce some messages'

    def handle(self, *args, **options):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='', routing_key='hello', body='Hello, I\'m producer')
        connection.close()
        self.stdout.write('Done')
