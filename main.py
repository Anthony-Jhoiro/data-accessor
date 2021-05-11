from ftplib import FTP
from dotenv import load_dotenv
import os
import sys

load_dotenv()

def download_file(source, dest):
    ftp = FTP(os.getenv('CARD_IP'))

    ftp.login(user=os.getenv('CARD_USER'), passwd=os.getenv('CARD_PASSWORD'))

    # Move into sd directory
    ftp.cwd('sd')

    with open(f'{dest}', 'wb') as fp:
        ftp.retrbinary(f'RETR {source}', fp.write)

    ftp.close()

def 


if __name__ == '__main__':
    if len(sys.argv != 3):
        raise ValueError("Please provide 2 arguments (source filename and destination filename).")

    source = sys.argv[1]
    dest = sys.argv[2]

    download_file(source, dest)