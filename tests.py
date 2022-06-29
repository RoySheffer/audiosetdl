# importing pafy
import pafy

# url of video
url = "https://www.youtube.com/watch?v=BaW_jenozKc"

# getting video
video = pafy.new(url)

# getting video ID
value = video.videoid

# printing the value
print("Video ID : " + value)



import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])

exit()
from download_audioset import download_yt_video
ytid, ts_start, ts_end, output_dir, ffmpeg_path, ffprobe_path =  "--56QUhyDQM", 20.0, 30.0, r"C:\Roy\Msc\audiosetdl\data\vggsound", r"C:\ffmpeg\bin\ffmpeg.exe", r"C:\ffmpeg\bin\ffprobe.exe"
download_yt_video(ytid, ts_start, ts_end, output_dir, ffmpeg_path, ffprobe_path, audio_sample_rate=16000, audio_format="wav")

# youtube-dl --rm-cache-dir
# data --ffmpeg C:\ffmpeg\bin\ffmpeg.exe --ffprobe C:\ffmpeg\bin\ffprobe.exe --audio-sample-rate 16000 --audio-format wav
