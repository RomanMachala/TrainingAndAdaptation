"""
    Thiis script produces datasets used to evaluate and train a selected model - VITS
"""

__author__  = "Roman Machala"

from modules.get_eval_audios import get_eval_audios
from modules.get_train_audios import get_train_dataset
from modules.resample import resample_audios
from modules.split_dataset import split_dataset
from modules.get_trans import get_trans
from modules.rename_eval import rename_eval
import os

# training dataset
orig_dataset = 'hi_fi_tts_v0/hi_fi_tts_v0/audio/92_clean'
train_output_path = 'training_dataset' # output path of selected audios

# eval dataset
eval_output_path = 'evaluation_dataset'

# output of resampled datasets
resampled_eval_dataset = "reference"
resampled_train_dataset = os.path.join("datset", "wavs")

# meta files
meta_four = os.path.join("dataset", "meta_four.csv")
meta_three = os.path.join("dataset", "meta_three.csv")
meta_two = os.path.join("dataset", "meta_two.csv")


if __name__ == "__main__":
    try:
        get_train_dataset(orig_dataset, train_output_path)
        get_eval_audios(orig_dataset, eval_output_path)
        resample_audios(train_output_path, resampled_train_dataset, 22050)
        resample_audios(eval_output_path, resampled_eval_dataset, 16000)
        get_trans("hi_fi_tts_v0/hi_fi_tts_v0/92_manifest_clean_train.json", resampled_train_dataset, "meta_four.csv")
        get_trans("hi_fi_tts_v0/hi_fi_tts_v0/92_manifest_clean_train.json", resampled_eval_dataset, "temp.csv")
        rename_eval(resampled_eval_dataset, "temp.csv")
        split_dataset(resampled_train_dataset, meta_four, meta_three, meta_two)
    except Exception as e:
        print(e)