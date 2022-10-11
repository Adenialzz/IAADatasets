import os
import os.path as osp
import requests
import random
import logging
from concurrent.futures import ThreadPoolExecutor
from utils import get_headers

class BaseCrawler:
    def __init__(self, work_dir, **kwargs):
        self.work_dir = work_dir
        if not osp.exists(self.work_dir):
            os.mkdir(self.work_dir)
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

    def process_one_item(self, items_list):
        raise NotImplementedError

    def _run_single_thread(self, image_names_list):
        for image_name in image_names_list:
            self.process_one_item(image_name)

    def _run_mutlti_thread(self, image_names_list, num_threads=10):
        with ThreadPoolExecutor(num_threads) as executor:
            executor.map(self.process_one_item, image_names_list)

    def run(self, image_names_list, num_threads=1):
        if num_threads == 1:
            self._run_single_thread(image_names_list)
        else:
            self._run_mutlti_thread(image_names_list, num_threads=num_threads)


