from .base_crawler import BaseCrawler

import os.path as osp
from lxml import etree
from utils import save_url_image

class BaseDPCCrawler(BaseCrawler):
    def __init__(self, work_dir, **kwargs):
        super().__init__(work_dir, **kwargs)
        self.dpc_base_image_url = 'https://www.dpchallenge.com/image.php?IMAGE_ID='

    def process_one_item(self, items_list):
        raise NotImplementedError


class DPCImageCrawler(BaseDPCCrawler):
    def __init__(self, work_dir, **kwargs):
        super().__init__(work_dir, **kwargs)

    def process_one_item(self, image_name):
        image_id = image_name.split('.')[0]
        image_home_url = self.dpc_base_image_url + image_id
        resp = self.sess.get(image_home_url, **self.get_request_config())
        tree = etree.HTML(resp.text)
        image_url = 'https:' + tree.xpath('//*[@id="img_container"]/img[2]')[0].get('src')
        save_url_image(image_url, self.work_dir)
        self.logger.info(f"{image_id}.jpg {image_url.split('/')[-1]} Saved.")


class DPCCommentsCrawler(BaseDPCCrawler):
    def __init__(self, work_dir, **kwargs):
        super().__init__(work_dir, **kwargs)

    def process_one_item(self, image_name):
        image_id = image_name.split('.')[0]
        image_home_url = self.dpc_base_image_url + image_id
        resp = self.sess.get(image_home_url, **self.get_request_config())
        tree = etree.HTML(resp.text)
        cnt = 3
        max_comments_cnt = 1e3
        image_comments = []
        while True:
            if cnt >= max_comments_cnt:
                break

            comment_data = tree.xpath(f'/html/body/table[2]/tr/td[2]/table[3]/tr[{cnt}]/td/table/tr/td/text()')
            cnt += 1
            if len(comment_data) == 0:
                continue
            else:
                comment_data = [c.strip()+', ' for c in comment_data]
                comment = ''.join(comment_data)[: -2] # remove last ', '
                image_comments.append(comment)
        with open(osp.join(self.work_dir, f'{image_id}.txt'), 'w') as f:
            f.writelines([c+'\n' for c in image_comments])
        self.logger.info(f"Comments {image_id}.txt Saved.")


class DPCCommentsImageCrawler(BaseCrawler):
    def __init__(self, work_dir, **kwargs):
        super().__init__(work_dir, **kwargs)
        self.image_crawler = DPCImageCrawler(osp.join(self.work_dir, 'image'), **kwargs)
        self.comments_crawler = DPCImageCrawler(osp.join(self.work_dir, 'comments'), **kwargs)

    def process_one_item(self, image_name):    # TODO optimize crawling image and comments in one requests
        self.image_crawler.process_one_item(image_name)
        self.comments_crawler.process_one_item(image_name)



