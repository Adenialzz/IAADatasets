
## Get DPC-Captions Dataset

The [comments of DPC-Captions](https://github.com/BestiVictory/DPC-Captions) dataset is open-sourced. But Considering the copyright of images, the authors only open-source the picture number public. According to the dataset annotation file provided by the author and the crawler script in this repo, the images of the dataset can be easily obtained with the following command.

```shell

# in the current directory
git clone git@github.com:BestiVictory/DPC-Captions.git
python main.py

```
  
## Paper  
  
Xin Jin, Le Wu, Geng Zhao, Xiaodong Li, Xiaokun Zhang, Shiming Ge, Dongqing Zou, Bin Zhou, Xinghui Zhou. Aesthetic Attributes Assessment of Images. ACM Multimedia (ACMMM), Nice, France, 21-25 Oct. 2019. **[pdf-HD](http://jinxin.me/downloads/papers/031-MM2019/MM2019-HighRes.pdf)**(31.1MB)  **[pdf-LR](http://jinxin.me/downloads/papers/031-MM2019/MM2019-LowRes.pdf)**(1.11MB) **[arXiv](https://arxiv.org/abs/1907.04983)**(1907.04983)

## Citation

Please cite the ACM Multimedia paper if you use DPC-Captions in your work:

```
@inproceedings{DBLP:conf/mm/JinWZLZGZZZ19,
  author    = {Xin Jin, Le Wu, Geng Zhao, Xiaodong Li, Xiaokun Zhang, Shiming Ge, Dongqing Zou, Bin Zhou and Xinghui Zhou},
  title     = {Aesthetic Attributes Assessment of Images},
  booktitle = {Proceedings of the 27th {ACM} International Conference on Multimedia,
               {MM} 2019, Nice, France, October 21-25, 2019},
  pages     = {311--319},
  year      = {2019},
  crossref  = {DBLP:conf/mm/2019},
  url       = {https://doi.org/10.1145/3343031.3350970},
  doi       = {10.1145/3343031.3350970},
  timestamp = {Fri, 06 Dec 2019 16:44:03 +0100},
  biburl    = {https://dblp.org/rec/bib/conf/mm/JinWZLZGZZZ19},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
