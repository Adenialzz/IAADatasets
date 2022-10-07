import os
import os.path as osp
import requests
import random
from lxml import etree

from utils import save_url_image, get_headers

class DPCImageCrawler:
    def __init__(self, work_dir, **kwargs):
        self.work_dir = work_dir
        if not osp.exists(self.work_dir):
            os.mkdir(self.work_dir)
        self.dpc_base_image_url = 'https://www.dpchallenge.com/image.php?IMAGE_ID='
        self.headers = get_headers(kwargs.get('ua_file', 'misc/user_agents.txt'))
        self.sess = requests.session()

    def get_request_config(self):
        request_config = {
            'headers': random.choice(self.headers),
            # 'proxies': self.proxies
        }
        return request_config

    def run(self, image_names_list):
        for image_name in image_names_list:
            image_id = image_name.split('.')[0]
            image_home_url = self.dpc_base_image_url + image_id
            resp = self.sess.get(image_home_url, **self.get_request_config())
            tree = etree.HTML(resp.text)
            image_url = 'https:' + tree.xpath('//*[@id="img_container"]/img[2]')[0].get('src')
            save_url_image(image_url, self.work_dir)



