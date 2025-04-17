"""
    This script converts audio files in flac format to wav format and resamples them
"""

import librosa
import os
import soundfile


def resample_audios(original_dataset: str, new_dataset: str, target_sr: int):
    """
        Resamples audio and saves them.

        Params:
            original_dataset:       dataset to be resampled
            new_dataset:            new dataset
            target_sr:              target sample rate
    """
    os.makedirs(new_dataset, exist_ok=True)
    count = 0
    for audio in os.listdir(original_dataset):
        y, sr = librosa.load(os.path.join(original_dataset, audio))
        new_y = librosa.resample(y=y, orig_sr=sr, target_sr=target_sr)
        count += 1
        soundfile.write(file=os.path.join(new_dataset, audio.split(".")[0] + ".wav"), data=new_y, samplerate=target_sr)