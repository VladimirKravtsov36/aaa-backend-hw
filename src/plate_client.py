import requests


class PlateClient:

    def __init__(self, host):
        self.host = host

    def read_plate_number(self, id):
        response = requests.get(f'{self.host}/read-number?id={id}')

        return response.json()

    def read_number(self, id):

        response = requests.get(f'{self.host}/read-number', params={'id': id})

        return response.json()

    def read_number_batch(self, ids):

        response = requests.get(f'{self.host}/read-number-batch', params={'id': ids})

        return response.json()

if __name__ == '__main__':

    client = PlateClient(host='http://127.0.0.1:8080')

    number = client.read_number(9965)
    print(number)

    number_batch = client.read_number_batch([9965, 10022])
    print(number_batch)