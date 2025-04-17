"""
    This script ranodmly selects audio samples up to DURATION in hours
"""

import os
import librosa
import random
import shutil

DATASET_LENGTH = 4
DURATION = DATASET_LENGTH * 3600


def get_train_dataset(dataset_path: str, output_path: str):
    """
        Gets train dataset

        Params:
            dataset_path:       path of the selected speaker
            output_path:        output path
    """

    os.makedirs(output_path, exist_ok=True)

    audio_files = list()

    # appends all audios for the selected speaker into a list
    for subdir in os.listdir(dataset_path):
        for audios in os.listdir(os.path.join(dataset_path, subdir)):
            audio_files.append(os.path.join(subdir, audios))

    random.shuffle(audio_files)
    # randomly shuffles audios
    current_dur = 0 # current count of samples
    # for all audios
    for audio in audio_files:
        dur = librosa.get_duration(path=os.path.join(dataset_path, audio))
        # get duration of audio
        if current_dur <= DURATION:
            # selects audios up to DATASET_LENGHT in hours
            subdir, file_path = os.path.split(audio)
            shutil.move(os.path.join(dataset_path, audio), os.path.join(output_path, file_path))
            current_dur += dur
        else:
            break