import os, glob
from pydub import AudioSegment
from pathlib import PurePath
import traceback as tb

# dataDir = r"C:\Roy\Msc\audiosetdl\vggsound"

data_dirs = []

# data_dirs += [r"/cs/dataset/Download/adiyoss/sheffer/vggsound"]

data_dirs += [r"/cs/dataset/Download/adiyoss/sheffer/audiocaps/train"]
data_dirs += [r"/cs/dataset/Download/adiyoss/sheffer/audiocaps/val"]
data_dirs += [r"/cs/dataset/Download/adiyoss/sheffer/audiocaps/test"]

for dataDir in data_dirs:
    flacDir = os.path.join(dataDir, 'audio')
    flacs = glob.glob(os.path.join(flacDir, '*.wav'))

    resultsDir = os.path.join(dataDir, 'wav')
    if not os.path.exists(resultsDir):
        os.makedirs(resultsDir)

    for flac in flacs:
        filename = os.path.basename(flac).split('.')[0]
        file_path = PurePath(flac)
        wav_name = os.path.join(resultsDir, f'{filename}.wav')
        if os.path.exists(wav_name):
            # print(f"{wav_name} Already exist")
            continue
        try:
            flac_tmp_audio_data = AudioSegment.from_file(file_path, file_path.suffix[1:])
            flac_tmp_audio_data.export(wav_name, format="wav")
        except Exception as e:
            err_msg = '{}: \nError while processing aduio: {}; {} {}'.format(file_path, e, tb.format_exc(), "\n-----------------------------------------------------------------------\n")
            print(err_msg)
            if not os.path.exists(flac):
                continue
            os.remove(flac)
            continue