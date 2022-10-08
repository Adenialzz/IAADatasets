import os
import os.path as osp
import json
import sys; sys.path.append('..')
from crawlers import DPCImageCrawler

def get_dpc_captions_images_list():
    anno_file_list = os.listdir('DPC-Captions')

    image_set = set()
    for anno_file in anno_file_list:
        if not anno_file.endswith('.json'):
            continue
        with open(osp.join('DPC-Captions', anno_file), 'r') as f:
            data = json.load(f)
        image_set |= set(data.keys())
    return image_set

def main():
    image_set = get_dpc_captions_images_list()
    crawler = DPCImageCrawler('work_dir', ua_file='../misc/user_agents.txt')
    crawler.run(image_set, num_threads=10)

if __name__ == '__main__':
    main()
