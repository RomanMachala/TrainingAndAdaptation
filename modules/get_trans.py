"""
    Thuis script gets audio transcriptions for selected speaker
"""
import json
import os
import csv


def get_trans(trans_path: str, dataset_path: str, meta_file: str):
    """
        Gets transcriptions for dataset

        Params:
            trans_path:     path to original transcirption file
            dataset_path:   path to dataset
            meta_file:      path to ouptut meta file
    """
    audios = [audio for audio in os.listdir(dataset_path)]
    data = []
    with open(trans_path, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))

    with open(meta_file, 'w', newline='') as csv_file:
        meta = csv.writer(csv_file, delimiter='|')
        for line in data:
            val, audio = os.path.split(line['audio_filepath'])
            audio = audio.split(".")[0] + ".wav"
            if audio in audios:
                meta.writerow([audio, line['text_normalized'], line['text_normalized'].replace("\'", "").replace("\"", "")])

        


