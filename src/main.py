from argparse import ArgumentParser
from parse_url import parse_url
from pathlib import Path
import requests
from itertools import count
from shutil import copyfileobj
import os


def main(url1, url2, out_dir):
    image_url = parse_url(url1, url2)
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    file_ext = image_url[-4:]
    for i in count(1, 1):
        try:
            r = requests.get(image_url.format(i), stream=True)
            if r.status_code == 200:
                img_file = os.path.join(out_dir, str(i) + file_ext)
                with open(img_file, 'wb') as f:
                    r.raw.decode_content = True
                    copyfileobj(r.raw, f)
            else:
                print('image ' + str(i) + ' not found')
                break
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        else:
            print('done image ' + str(i))


if __name__ == "__main__":
    parser = ArgumentParser(description='Scrape related images from a website given two image urls.')
    parser.add_argument('url1', metavar='URL1', type=str, help='full image url of a website')
    parser.add_argument('url2', metavar='URL2', type=str, help='second full image url from the same website')
    parser.add_argument('directory', metavar="DIR", type=str, help='directory to store scraped images')

    args = parser.parse_args()

    main(url1=args.url1, url2=args.url2, out_dir=args.directory)