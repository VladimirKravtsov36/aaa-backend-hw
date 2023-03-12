

from flask import Flask, request
import logging
import requests


from models.plate_reader import PlateReader
from utils import recognize_text

IMAGES_URL = 'http://51.250.83.169:7878/images'

app = Flask(__name__)
plate_reader = PlateReader.load_from_file('./model_weights/plate_reader_model.pth')

@app.route('/')
def hello():
    return '<h1><center>Hello!</center></h1>'


@app.route('/read-number')
def read_number():

    id = request.args.get('id')
    recognition_result = recognize_text(IMAGES_URL, id, reader=plate_reader)

    return recognition_result


@app.route('/read-number-batch')
def read_number_batch():

    ids = request.args.getlist('id')

    response = {'Plate numbers': []}

    for id in ids:
        recognition_result = recognize_text(IMAGES_URL, id, reader=plate_reader)

        if recognition_result[1] != 200:
            return recognition_result

        response['Plate numbers'].append(recognition_result[0])

    return response

if __name__ == '__main__':
    logging.basicConfig(
        format='[%(levelname)s] [%(asctime)s] %(message)s',
        level=logging.INFO,
    )

    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=8080, debug=True)
