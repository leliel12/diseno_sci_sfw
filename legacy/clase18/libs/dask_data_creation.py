import gzip
import json
import os
import random
import shutil
from contextlib import closing

import pandas as pd


def generate_sample_data():
    random.seed(42)
    files = {}
    for month in range(1, 13):
        lines = []
        for suffix_id in range(1000):
            lines.append({
                'id': month * 1000 + suffix_id,
                'duration': random.randint(1, 100),
                'month': month
            })
        files[month] = lines
    return files


def generate_dask_bag_files():
    base_path = 'db_data'
    if os.path.exists(base_path):
        print('Removing old data')
        shutil.rmtree(base_path)
    print('Generating dask bag data sample...')
    os.mkdir(base_path)
    files = generate_sample_data()
    for month, lines in files.items():
        filename = os.path.join(base_path, 'month_{}.json.gz'.format(month))
        with closing(gzip.open(filename, 'wt')) as f:
            f.write('\n'.join(map(json.dumps, lines)))


def generate_dask_dataframe_files():
    base_path = 'dd_data'
    if os.path.exists(base_path):
        print('Removing old data')
        shutil.rmtree(base_path)

    print('Generating dask dataframe data sample...')
    os.mkdir(base_path)
    files = generate_sample_data()
    for month, lines in files.items():
        filename = os.path.join(base_path, 'month_{}.csv.gz'.format(month))
        df = pd.DataFrame(lines)
        df.to_csv(filename, compression='gzip', index=False)


def generate_presentation_data():
    generate_dask_dataframe_files()
    generate_dask_bag_files()


if __name__ == '__main__':
    generate_presentation_data()
