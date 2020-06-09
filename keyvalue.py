import argparse
import os
import tempfile
import json

def create_file(data):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    with open(storage_path, 'w') as file:
        file.write(json.load(data))



def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', type=str)
    parser.add_argument('--value', type=str)
    args = parser.parse_args()
    if args.key:
        print(args.key)


def write(*args):
    pass
parse()
