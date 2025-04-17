# Training and adaptation of slected model using CoquiTTS system
This document and attached files, datasets, etc. were created as a part of a Bachelor's Thesis of Roman Machala - Comparison and analaysis of speech synthesizers.

**The training was done through GoogleColab; hence it is recommended and training scripts are designed to be ran through GoogleColab**

In this section the CoquiTTS systems is utilized for both training and adaptation of already existing synthesizer.

## Getting data
The data can be get by downloading the dataset at https://www.openslr.org/109/ and running:
```
    wget https://www.openslr.org/resources/109/hi_fi_tts_v0.tar.gz

    tar -ztvf downloaded_dataset.tar.gz

    python get_audios.py
```

Several directories are made with training dataset and evalaution dataset used in this experiment. 
**All audios are picked randomly!**

Make sure to check the directories name are matching names in used scripts.

## Model selection
The selected model is VITS. The VITS model is a end-to-end model capable of synthesizing natural and intelligible speech directly from text input. Originally the VITS model was trained on LJSpeech dataset for a single speaker or a multi-speaker version was trained on a VCTK corpus, both available at: https://github.com/coqui-ai/TTS/blob/dev/TTS/.models.json.

For this experiment I have chosen the single speaker version and try to adapt this version on a different speaker using limited data and fixed training parameters.
## Data preparation
The obvious choice for a single speaker dataset would be the LJSpeech dataset, but since the original model was trained on it, I have chosen a Hi-Fi Multi-Speaker High-Quality TTS dataset, available at: https://www.openslr.org/109/. From this dataset a specific speaker was chosen (speaker ID = 92) and random samples were selected up to four hours of data length.

From this four-hour long dataset a subsets of three and two hours were extracted. These subsets would then serve as training datasets. The figure below shows the number of samples for each dataset and its' corresponding metadata file located in **dataset/meta_X.csv**, where X is the lenght of the dataset.

Subset | num_of_samples | lenght [hours] | metadata file
:-| :-: | :-: | :-
subset_4 | 5178 | 4 | meta_four.csv
subset_3 | 3849 | 3 | meta_three.csv
subset_2 | 2616 | 2 | meta_two.csv

The overall structure of the dataset should be as followed:
```
dataset/
|---	wavs/
|			|---	audio_sample_01.wav
|			|---	audio_sample_02.wav
|			|--- 	audio_sample_03.wav
|			...
|---	meta_two.csv
|--- 	meta_three.csv
|---	meta_four.csv
```

With the metadata.csv file structure being:
```
audio_sample_01|transcription|normalized_transcription
audio_sample_02|transcription|normalized_transcription
audio_sample_03|transcription|normalized_transcription
...
```

## Training parameters
Before starting the training using the attached training script. Be sure to adjust the ***config.json*** file to your needs, especially the paths needed for the training, such as dataset path.

In order to train different models, others than VITS, you can download any model at: https://github.com/coqui-ai/TTS/blob/dev/TTS/.models.json with attached config.json file aswell. All you need is correctly set those paths and start training. If you want to train from scratch, the config file is all you need. If you want to adapt the mode, the ***--restore_path*** is required with a path to the model.

```
# Starts the training with attached config.json file
# Restores from model.pth
python path/to/training/script.py --config_path config.json --restore_path model.pth


# For training from scratch:
python path/to/training/script.py --config_path config.json
```

All scripts used to adapt the VITS model are attached with this file, as well as outputs of training, samples generated using default and adapted VITS models.

For further details please reade the CoquiTTS documentation, available at: https://docs.coqui.ai/en/latest/, where all parameters are explained in details.


