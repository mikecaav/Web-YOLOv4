from flask import Flask, send_file, request
import numpy as np
from matplotlib import pyplot as plt

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    image = np.fromstring(request.data, np.uint8)
    print(request.data)
    return "hola mundo!"
    

if __name__ == "__main__":
    app.run()
