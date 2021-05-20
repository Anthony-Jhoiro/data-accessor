from ftplib import FTP
from dotenv import load_dotenv
import os
import sys
import requests

load_dotenv()

def download_file(source, dest):
    ftp = FTP(os.getenv('CARD_IP'))

    ftp.login(user=os.getenv('CARD_USER'), passwd=os.getenv('CARD_PASSWORD'))

    # Move into sd directory
    ftp.cwd('sd')

    with open(f'{dest}', 'wb') as fp:
        ftp.retrbinary(f'RETR {source}', fp.write)

    ftp.close()


def parse_csv(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            datum = line.split(',')

            data.append({
                "date": datum[0],
                "pressure": datum[1],
                "temperature": datum[5:],
                "hygrometry": datum[2],
                "brightness": datum
            })



def send_data(data):
    requests.post(os.environ("SERVER_URL") + '/api/v0/record', data)

if __name__ == '__main__':
    if len(sys.argv != 3):
        raise ValueError("Please provide 2 arguments (source filename and destination filename).")

    source = sys.argv[1]
    dest = sys.argv[2]

    download_file(source, dest)

    data = parse_csv(dest)
    send_data(data)
