"""
    This script contains logic to produce the evlauation dataset.
"""

__author__  = "Roman Machala"

import os
import csv
import shutil


def rename_eval(dataset_path: str, meta:str):
    """
        Renames files in evaluation dataset to simpler form

        Params:
            dataset_path:       path of the dataset
            meta:               name of meta file from get_trans
    """
    with open(meta, 'r') as meta:
        content = csv.reader(meta, delimiter='|')
        count = 0
        with open("eval.csv", "w") as eval:
            for row in content:
                audio, text, norm = row[0], row[1], row[2]
                new_name = f"sample_0{count}.wav"
                eval.write(f"{new_name}|{text}|{norm}\n")
                count += 1
                shutil.move(os.path.join(dataset_path, audio), os.path.join(dataset_path, new_name))