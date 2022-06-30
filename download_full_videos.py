from __future__ import unicode_literals
import youtube_dl
import os
import subprocess as sp

def clean_cache():
    cmd = ["youtube-dl", "--rm-cache-dir"]
    proc = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = proc.communicate()
    return_code = proc.returncode

clean_cache()
media_filename = "bb"
video_page_url = "https://www.youtube.com/watch?v=BaW_jenozKc"
output_dir = "C:\\Roy\Msc\\audiosetdl\\vggsound\\"
out_dir =  os.path.join(output_dir, 'full')
os.chdir(out_dir)
ydl_opts = {'outtmpl': media_filename}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_page_url])