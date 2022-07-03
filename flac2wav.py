import os, glob
from pydub import AudioSegment
from pathlib import PurePath
import traceback as tb

# dataDir = r"C:\Roy\Msc\audiosetdl\vggsound"
dataDir = r"/cs/dataset/Download/adiyoss/sheffer/vggsound"


flacDir = os.path.join(dataDir, 'audio')
flacs = glob.glob(os.path.join(flacDir, '*.wav'))

resultsDir = flacDir = os.path.join(dataDir, 'wav')
if not os.path.exists(resultsDir):
    os.makedirs(resultsDir)

for flac in flacs:
    filename = os.path.basename(flac).split('.')[0]
    file_path = PurePath(flac)
    wav_name = os.path.join(resultsDir, f'{filename}.wav')
    if os.path.exists(wav_name):
        print(f"{wav_name} Already exist")
        continue
    try:
        flac_tmp_audio_data = AudioSegment.from_file(file_path, file_path.suffix[1:])
        flac_tmp_audio_data.exportwav_name(wav_name, format="wav")
    except Exception as e:
        err_msg = '{} Error while processing video: {}; {} {}'.format(file_path, e, tb.format_exc(), "\n-----------------------------------------------------------------------\n")
        print(err_msg)
        continue