import json

from confluent_kafka import Consumer

from emailApp.utils import send_email

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'emailService',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(conf)


def handle_send_email():
    consumer.subscribe(['sending_email'])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                print(f'Consumer error: {msg.error()}')
                continue

            data = json.loads(msg.value().decode('utf-8'))
            to = data['to']
            subject = data['subject']
            from_ = data['from']
            body = data['body']
            send_email(to, subject, from_, body)
            print(f'Sent email to {to}')

    except KeyboardInterrupt:
        pass

    
