import tkinter as tk
import tkinter.ttk as ttk
from mp4_downloader import networkmovie
from download_youtube_to_mp3 import networkmusic
from tkinter import filedialog
import subprocess
import os
import ffmpeg 

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.master.title("Downloader")       # ウィンドウタイトル
        self.master.geometry("1200x500") # ウィンドウサイズ(幅x高さ)


        self.font = ("MSゴシック", "14")



        self.create_download_gui()
       

    def create_download_gui(self):

        # Download frame
        self.download_frame = tk.LabelFrame(root, text="Download", padx=10, pady=10)
        self.download_frame.grid(column=0, row=0, padx=10)

        # traslate mp4 to mp3
        self.trans_frame = tk.LabelFrame(root, text="変換", padx=10, pady=10)
        self.trans_frame.grid(column=0, row=1, padx=10, pady=10)

        # ラベル作成
        self.create_label()

        self.Entry_url()

        self.create_button()

        self.create_trans()


    def create_trans(self):
        # ボタンの作成
        btn_modeless = tk.Button(
            self.trans_frame, 
            text = "参照",   # ボタンの表示名
            command = self.create_modeless_dialog,    # クリックされたときに呼ばれるメソッド
            font = self.font
            )
        btn_modeless.grid(column=0,row=0,padx=10,pady=10)

        self.file_name = tk.StringVar()
        self.file_label = tk.Label(self.trans_frame, textvariable=self.file_name, font=self.font)
        self.file_label.grid(column=1, row=0, padx=10, pady=10)

        self.trans_button = tk.Button(
            self.trans_frame,
            text="変換",
            command= self.trans_mp4_to_mp3,
            font= self.font
        )
        self.trans_button.grid(column=0,row=1,padx=10,pady=10)

    def create_label(self):
        # ラベル(URL)
        self.url = ttk.Label(self.download_frame, text='url:',font=self.font, anchor=tk.W)
        self.url.grid(column=0, row=0)

        # ラベル(タイトル)
        self.lbl_title = ttk.Label(self.download_frame, text='title:',
                                    font=self.font, anchor=tk.W)
        self.lbl_title.grid(column=0, row=1)

    def Entry_url(self):

        # テキストボックス(URL入力用)
        self.entry_url = ttk.Entry(self.download_frame, width=100, font=self.font)
        self.entry_url.grid(column=1, row=0, padx=10, pady=10)

        # タイトル入力
        self.entry_title = ttk.Entry(self.download_frame, width=80, font=self.font)
        self.entry_title.grid(sticky="W", column=1, row=1, padx=10, pady=10)
        

    def create_button(self):
        # 各種ウィジェットの作成
        self.dl_movie = tk.Button(self.download_frame, text="DL TUBE", command=self.down_load_mp4,
                                  font=("MSゴシック", "14", "bold"))
        self.dl_movie.grid(column=1, row=2, pady = 10)

        self.dl_mp3 = tk.Button(self.download_frame, text="MP3 DL", command=self.down_load_mp3, 
                                font=("MSゴシック", "14", "bold"), fg='green')
        self.dl_mp3.grid(column=1, row=3, pady=10)

    def down_load_mp4(self):
        url = self.entry_url.get()
        title = self.entry_title.get()
        if len(url) > 1 :
            if len(title) > 1:
                dl = networkmovie(url, title)
                dl.download()
            else:
                dl = networkmovie(url, 'av_')
                dl.download()
        else:
            print('URL is not set.')

    def down_load_mp3(self):
        url = self.entry_url.get()
        # urlの後ろの部分を切る
        url = url.split('&list=')[0]

        title = self.entry_title.get()
        if len(url) > 1 :
            if len(title) > 1:
                dl = networkmusic(url, title)
                dl.download()
            else:
                dl = networkmusic(url, 'mp_')
                dl.download()
            self.entry_url.delete(0, tk.END)
        else:
            print('URL is not set.')

    def create_modeless_dialog(self):
        fTyp = [("動画ファイル", "*.mp4;*.webm")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        file_name = tk.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
        if len(file_name) == 0:
            self.file_name.set('選択をキャンセルしました')
        else:
            self.file_name.set(file_name)

    def trans_mp4_to_mp3(self):
        file = self.file_label["text"]
        mp3_file = file.replace("/movie_data/","/music_data/").replace(".webm",".mp3").replace(".mp4",".mp3")
        import subprocess
        subprocess.run(["ffmpeg", "-i", file, "-q:a", "0", "-map", "a", mp3_file])

# def load_video():
    
#     """ loads the video """
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         os.startfile(file_path)
#     # global text_list
#     # text_list = 'playing:' + os.path.basename(file_path)
#     # move_text()
#     # move_text('playing:' + os.path.basename(file_path))
#     status_txt.set('playing:' + os.path.basename(file_path))

# def start_winamp():
#     subprocess.Popen(rf"C:\Program Files (x86)\Winamp\winamp.exe")

# def move_text():
#     global text_x, text_y, text_list
#     status_t.place_forget()
#     status_t.place(x=text_x,y=text_y)
#     text_x -= 50
#     n = len(text_list)-1 #リストの要素数を取得
#     if text_x <=-3000: #画面左端まで文字が到達した場合
#         text_x = 0 #画面右に戻す
#         x += 1 #取り込むリストの要素をひとつずらす
#         status_txt.set(text_list) #StringVarに反映
#         if x == n: #xが要素数+1に達した場合
#             x=0 #最初にリセット
#             status_txt.set(text_list[len(text_list)-1]) #要素数の最大値の要素をStringVarに反映
#         root.after(10,move_text) #100ミリ秒ごとにスクロール


# # 
# # Tkクラス生成
# root = tk.Tk()
# # 画面サイズ
# root.geometry('1200x500')
# # 画面タイトル
# root.title('downloder player')

# status_txt = tk.StringVar()
# status_txt.set('status')
# # 状態
# # status_t = tk.Label(root, textvariable=status_txt, font=("MSゴシック", "14"))
# # status_t.place(x=10, y =10)

# # 各種ウィジェットの作成
# button = tk.Button(root, text="download to Moive", command=down_load, font=("MSゴシック", "14", "bold"), fg='red')
# button2 = tk.Button(root, text="download to MP3", command=down_load_mp3, font=("MSゴシック", "14", "bold"), fg='green')
# # 各種ウィジェットの作成
# button3 = tk.Button(root, text="open", command=load_video, font=("MSゴシック", "14", "bold"), fg="blue")

# button4 = tk.Button(root, text="Open_Winamp", command=start_winamp, font=("MSゴシック", "14", "bold"))


# button2.place(x= 350, y=120)
# button3.place(x= 100, y=180)
# button4.place(x= 350, y= 180)
# # button3.bind('event', load_video)

# # button3.pack()

# # 流れる座標
# text_x = 0
# text_y = 80
# text_list = 'status'

# # メインフレームの作成と設置
# frame_label = tk.Frame(root, bg='#000000')
# # 状態
# status_t = tk.Label(frame_label, textvariable=status_txt, bg="#000000",fg="#FFFFFF",font=("MSゴシック", "14"))
# # status_t.place(x=10, y =10)
# frame_label.place(x=140, y=230, width=800, height= 200)
# # frame_label.pack()
# status_t.place(x=0, y=80)
# # status_t.pack()


# # 表示
# root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()