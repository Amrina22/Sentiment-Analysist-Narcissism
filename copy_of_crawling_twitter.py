# -*- coding: utf-8 -*-
"""Copy of crawling twitter.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17VFSkWRZpvGrk7kmJoZEZeWDTkxNvkTK
"""

!pip install pandas
!curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
!sudo apt-get install -y nodejs

rm -rf node_modules

!sudo apt-get install build-essential

!npm install
!npm cache clean --force

!npm install tweet-harvest --save

data = 'dataset_jaemin.csv'
search_keyword = 'jaemin narcissism since:2024-06-11 until:2024-07-24'
limit = 300

!npx --yes tweet-harvest@2.6.1 -o "{data}" -s "{search_keyword}" -l {limit} --token ""

import pandas as pd

data = pd.read_csv("/content/tweets-data/dataset_jaemin.csv")

data.info()

data.head()