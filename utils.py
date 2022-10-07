import os
import os.path as osp
import requests
import json

def save_html(url, file_name):
    resp = requests.get(url)
    html = resp.text
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(html)

def save_url_image(url, save_dir):
    data = requests.get(url).content
    image_name = osp.basename(url)
    with open(osp.join(save_dir, image_name), 'wb') as fd:
        fd.write(data)


def get_headers(ua_file='user_agents.txt'):
    with open(ua_file, 'r') as f:
        f_lines = f.readlines()
    lines = [line.strip() for line in f_lines]
    headers = []
    for line in lines:
        user_agent = line.split(':')[1].strip()
        headers.append({
            'User-Agent': user_agent,
            'Connection': 'close'
        })
    return headers

