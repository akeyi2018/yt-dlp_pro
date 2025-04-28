import youtube_dl
import yt_dlp
import datetime
import sys
import os.path
import glob
import ffmpeg

class networkmovie:
    def __init__(self, link_info, name='AUTO'):
        self.prefix = datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')
        self.data_folder = './movie_data'
        self.music_filename = os.path.join(self.data_folder, name + self.prefix)
        self.link_info = link_info

    def download(self):
        # ydl_opts = {
        # 'outtmpl':  self.music_filename + '.%(ext)s',
        # 'retries': 10, 'verbose': True }

        ydl_opts = {
            'format':'bestvideo[ext=mp4]',
            'outtmpl': self.music_filename + '.%(ext)s',
        }

        import subprocess
        subprocess.run(["yt-dlp", self.link_info])

        # ydl = youtube_dl.YoutubeDL(ydl_opts)
        # info_dict = ydl.extract_info(self.link_info, download=True)
        # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #     ydl.download([self.link_info])
            
if __name__ == '__main__':
    # link = sys.argv[1]
    # name = sys.argv[2]
    # dl = networkmusic(link, name)
    dl = networkmovie('', name='av_')
    dl.download()
    # dl.trans_webm_mp3()