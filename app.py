import time
import cv2
from flask import Flask, render_template, Response, request
import json
import pika
from flask_cors import CORS, cross_origin
import numpy as np

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

connection = pika.BlockingConnection()
channel = connection.channel()

channel.queue_declare(queue='counter')


@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

previous_faces_length = 0
faceId = 55


def gen(id):
    """Video streaming generator function."""
    cap = cv2.VideoCapture('f2.mp4')

    # Read until video is completed
    while(cap.isOpened()):
      # Capture frame-by-frame

        ret, img = cap.read()
        if ret == True:
            img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detect the faces
            faces = face_cascade.detectMultiScale(gray, 1.2, 4)

            # print("FACES COUNT: {}".format(len(faces)))
            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            #global faceId

            #print('FaceID: {}'.format(faceId))
            # cv2.imshow('img', img)
            # ovde treba da stoji img
            global previous_faces_length

            print('PREV FACES LEN {}'.format(previous_faces_length))
            print('FACES LEN {} '.format(len(faces)))

            if id is not None:
                previous_faces_length = 0
                print('ID: {}'.format(id))
                x, y, w, h = faces[int(id)]
                face_to_show = faces = img[-70 +
                                           y:y + h + 70, -70 + x:x + w + 70]
                frame = cv2.imencode('.jpg', face_to_show)[1].tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                time.sleep(0.1)

                # faces = faces[int(id)]
                previous_faces_length = 0
            else:
                frame = cv2.imencode('.jpg', img)[1].tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                time.sleep(0.1)

            if len(faces) != previous_faces_length:
                # XD
                if (len(faces) > 10):
                    continue
                previous_faces_length = len(faces)

                # print('Poslato za lice')
                json_payload = json.dumps({'faces': previous_faces_length})
                channel.basic_publish(exchange='',
                                      routing_key='counter',
                                      body=json_payload)
        else:
            break


@app.route('/video_feed')
@cross_origin()
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    id = request.args.get('id')

    return Response(gen(id),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
