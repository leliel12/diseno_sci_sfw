#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse

import joblib

import pandas as pd


CPUS = joblib.cpu_count()

READERS = {
    ".csv": pd.read_csv,
    ".pkl": pd.read_pickle}


def open_file(path):
    ext = os.path.splitext(path)[-1]
    reader = READERS[ext]
    return path, reader(path).describe()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="+")

    ns = parser.parse_args()

    cpus = len(ns.file)
    cpus = cpus if cpus <= CPUS else CPUS

    if cpus > 1:
        with joblib.Parallel(n_jobs=cpus) as P:
            dfs = P(joblib.delayed(open_file)(path) for path in ns.file)
    else:
        dfs = [open_file(path) for path in ns.file]

    for path, df in dfs:
        print(f"FILE: {path}")
        print(df)
        print("-" * 80)


if __name__ == "__main__":
    main()
