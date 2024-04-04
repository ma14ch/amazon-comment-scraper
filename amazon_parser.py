#!/usr/bin/env python
# -*- coding: utf-8 -*-

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import codecs
import csv
import sys
import os
import fnmatch
import re
import requests
from bs4 import BeautifulSoup


if sys.version_info[0] >= 3:
    import html


def get_review_filesnames(input_dir):
    for root, dirnames, filenames in os.walk(input_dir):
        for filename in fnmatch.filter(filenames, '*.html'):
            print(filename)
            yield os.path.join(root, filename)



def main():
    # sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
    parser = argparse.ArgumentParser(
        description='Amazon review parser')
    parser.add_argument('-d', '--dir', help='Directory with the data for parsing', required=True)
    parser.add_argument('-o', '--outfile', help='Output file path for saving the reviews in csv format', required=True)

    args = parser.parse_args()

    reviews = dict()

    with codecs.open(args.outfile, 'w', encoding='utf8') as out:
        writer = csv.writer(out, lineterminator='\n')
        reviews = []
        for filepath in get_review_filesnames(args.dir):
            #print(args.dir)
            with codecs.open(filepath, mode='r', encoding='utf8') as file:
                soup = BeautifulSoup(file.read(),'html.parser')
                for review in soup.find_all('div', {'data-hook': 'review'}):
                    if review != None: 
                        
                        title = review.find('a', {'data-hook': 'review-title'})
                        if title!=None: title=title.text.strip()
                        text = review.find('span', {'data-hook': 'review-body'})
                        if text!=None : text=text.text.strip()
                        rating = review.find('i', {'data-hook': 'review-star-rating'})
                        if rating!=None : rating=rating.text.strip()

                        # Find all the images in the review and download them
                        image_urls = [img['src'] for img in review.find_all('Customer image')]
                        images = []
                        for image_url in image_urls:
                            response = requests.get(image_url)
                            filename = image_url.split('/')[-1]
                            with open(filename, 'wb') as f:
                                f.write(response.content)
                            images.append(filename)
                        reviews.append({'title': title, 'text': text, 'rating': rating, 'images': images})


    with open('reviews.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'text', 'rating','images']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for review in reviews:
            writer.writerow(review)
                


if __name__ == '__main__':
    main()