import pika
import sys
import os
import json


def main():
    connection = pika.BlockingConnection()
    channel = connection.channel()

    channel.queue_declare(queue='counter')

    def callback(ch, method, properties, body):
        receivedObj = json.loads(body)
        if "selectedFace" in receivedObj:
            print('fid')
            from app import faceId
            print(faceId)
            faceId = receivedObj["selectedFace"]

    channel.basic_consume(
        queue='counter', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


# if __name__ == '__main__':
try:
    main()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
