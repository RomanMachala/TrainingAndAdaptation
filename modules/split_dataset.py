import csv
import librosa
import os


def split_dataset(dataset_path: str, meta: str, meta_two: str, meta_three: str):
    """
        Splits dataset into smaller subsets (2 and 3 hours)

        Params:
            dataset_path:           path of the dataset
            meta:                   meta file 
            meta_two:               meta for new subset of 2 hours
            meta_three:             meta for new subset of 3 hours
    """

    duration = 0
    with open(meta_two, 'w', newline='') as csv_file:
        meta_two = csv.writer(csv_file, delimiter='|')

        with open(meta_three, 'w', newline='') as csv_file:
            meta_three = csv.writer(csv_file, delimiter='|')

            with open(meta, 'r') as csv_file:
                content = csv.reader(csv_file, delimiter='|')

                for row in content:
                    audio, text, norm = row[0], row[1], row[2]
                    dur = librosa.get_duration(path=os.path.join(dataset_path, audio))
                    if duration < 2 * 3600:
                        meta_two.writerow([audio, text, norm])
                    if duration < 3 * 3600:
                        meta_three.writerow([audio, text, norm])
                    duration += dur    




