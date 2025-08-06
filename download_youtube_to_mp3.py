import datetime
import os.path
import yt_dlp

class networkmusic:
    def __init__(self, link_info, name='AUTO'):
        self.prefix = datetime.datetime.now().strftime('_%Y_%m_%d_%H_%M_%S')
        self.data_folder = './music_data'
        self.music_filename = os.path.join(self.data_folder, name + self.prefix)
        self.link_info = link_info
        
    def my_hook(self,d):
        if d['status'] == 'downloading':
            yield "downloading... "
        if d['status'] == 'finished':
            filename=d['filename']
            yield filename

    def download(self):
        ydl_opts = {
        'format': 'bestaudio',
        'outtmpl':  self.music_filename + '.%(ext)s',
        # 'quiet': True,
        'no_warnings': True,
        'progress_hooks':[self.my_hook],
        'postprocessors': [
            {'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'},
            {'key': 'FFmpegMetadata'},
        ],
        }
        # ydl = youtube_dl.YoutubeDL(ydl_opts)
        # info_dict = ydl.extract_info(self.link_info, download=True)
        # return info_dict
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link_info])
            
if __name__ == '__main__':
    # link = sys.argv[1]
    # name = sys.argv[2]
    # dl = networkmusic(link, name)
    dl = networkmusic('https://www.youtube.com/watch?v=qqpOm9MzIcI&list=LL&index=6&t=789s&ab_channel=Hq-Audio', name='hotel_carifornia')
    res = dl.download()
    # dl.trans_webm_mp3()