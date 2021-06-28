from flask import Flask, render_template, request
from flask.wrappers import Response
import numpy as np
from matplotlib import pyplot as plt
import cv2
from yolov4.demo import detect_cv2
from yolov4.tool.darknet2pytorch import Darknet
import argparse

cfgfile = "./yolov4/cfg/yolov4-tiny.cfg"
weightfile = "./yolov4/yolov4-tiny.weights"


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('use_cuda', type=bool, nargs='+', help='Wheter cpu is going to be used or not')
args = parser.parse_args()

app = Flask(__name__)
camera = cv2.VideoCapture(0)
model = Darknet(cfgfile)

model.print_network()
model.load_weights(weightfile)
print('Loading weights from %s... Done!' % (weightfile))



args = parser.parse_args()
use_cuda = args.use_cuda

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/video-feed')
def video_feed():
    return Response(gen_frames(use_cuda), mimetype='multipart/x-mixed-replace; boundary=frame')


def gen_frames(use_cuda):
    while True:
        success, frame = camera.read()  # read the camera frame
        frame = np.array(frame)
        frame = detect_cv2(model, cfgfile, weightfile, frame, use_cuda)
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

if __name__ == "__main__":
    app.run()
