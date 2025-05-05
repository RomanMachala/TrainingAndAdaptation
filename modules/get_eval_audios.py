"""
    This script ranodmly selects 100 samples for a selected speaker as evaluation samples
"""

__author__  = "Roman Machala"

import os
import librosa
import random
import shutil

MIN = 6 # min seconds 
MAX = 8 # max seconds
SAMPLES = 100 # samples to select


def get_eval_audios(dataset_path: str, output_path: str):
    """
        Gets eval dataset.

        Params:
            dataset_path:       path of the selected speaker
            otuput_path:        output dataset path
    """

    os.makedirs(output_path, exist_ok=True)

    audio_files = list()

    # appends all audios for the selected speaker into a list
    for subdir in os.listdir(dataset_path):
        for audios in os.listdir(os.path.join(dataset_path, subdir)):
            audio_files.append(os.path.join(subdir, audios))

    random.shuffle(audio_files)
    # randomly shuffles audios
    count = 0 # current count of samples
    # for all audios
    for audio in audio_files:
        dur = librosa.get_duration(path=os.path.join(dataset_path, audio))
        # get duration of audio
        if dur < MAX and dur > MIN and count <= SAMPLES:
            # selects only audios between MIN and MAX duration, only 100 samples
            subdir, file_path = os.path.split(audio)
            shutil.move(os.path.join(dataset_path, audio), os.path.join(output_path, file_path))
            count += 1
        if count > 100:
            break