#!/bin/bash

CWD=$(pwd)

python $CWD/download_audioset.py /cs/dataset/Download/adiyoss/sheffer/audiocaps \
--ffmpeg /cs/labs/adiyoss/roysheffer/audiosetdl/ffmpeg-5.0.1-amd64-static/ffmpeg \
--ffprobe /cs/labs/adiyoss/roysheffer/audiosetdl/ffmpeg-5.0.1-amd64-static/ffprobe \
--audio-sample-rate 16000 \
--audio-format wav \
--num-workers 10 \
--dataPath /cs/labs/adiyoss/roysheffer/audiosetdl/audioset/unbalanced_train_segments.csv
