import os
import os.path as osp
import requests
import random
import logging
from concurrent.futures import ThreadPoolExecutor
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
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def get_request_config(self):
        request_config = {
            'headers': random.choice(self.headers),
            # 'proxies': self.proxies
        }
        return request_config

    def get_dpc_image(self, image_name):
        image_id = image_name.split('.')[0]
        image_home_url = self.dpc_base_image_url + image_id
        resp = self.sess.get(image_home_url, **self.get_request_config())
        tree = etree.HTML(resp.text)
        image_url = 'https:' + tree.xpath('//*[@id="img_container"]/img[2]')[0].get('src')
        save_url_image(image_url, self.work_dir)
        self.logger.info(f"{image_url.split('/')[-1]} Saved.")

    def _run_single_thread(self, image_names_list):
        for image_name in image_names_list:
            self.get_dpc_image(image_name)

    def _run_mutlti_thread(self, image_names_list, num_threads=10):
        with ThreadPoolExecutor(num_threads) as executor:
            executor.map(self.get_dpc_image, image_names_list)

    def run(self, image_names_list, num_threads=1):
        if num_threads == 1:
            self._run_single_thread(image_names_list)
        else:
            self._run_mutlti_thread(image_names_list, num_threads=num_threads)


