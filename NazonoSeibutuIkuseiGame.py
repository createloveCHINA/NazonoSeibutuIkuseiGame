from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from concurrent.futures import ThreadPoolExecutor
import pygame
import Syori.SonotaSyori.SoundKanri

Thread1=ThreadPoolExecutor()
sound=Syori.SonotaSyori.SoundKanri.SoundKanri()
#テスト
import random
import time
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk



import Syori.SeibutuSyori
import Syori.SonotaSyori.Ukewatasi
import Syori.Tarn

import Syori.DataKanri.load
import Syori.DataKanri.save
import Syori.DataKanri.crea
import Syori.DataKanri.DataKanri

import sys

sys.setrecursionlimit(5000)


Seibutu = Syori.SeibutuSyori.SeibutuSyori()
ukewatasi=Syori.SonotaSyori.Ukewatasi.Ukewatasi()
Tarn=Syori.Tarn.Tarn(Seibutu)

lod=Syori.DataKanri.load.load(Tarn,Seibutu)
sav=Syori.DataKanri.save.save(Tarn,Seibutu)
cre=Syori.DataKanri.crea.crea(Tarn,Seibutu)
dat=Syori.DataKanri.DataKanri.DataKanri(Tarn,Seibutu)

#toumei=tk.Tk()
#toumei.configure(bg='blue')
#toumei.wm_attributes("-transparentcolor", "blue")

# 処理前の時刻
t1 = time.time() 
#初期描画
root=tk.Tk()
root.title("謎の生物育成ゲーム")
#ウィンドウを中心にする

root.geometry("700x700+350+0")
root.resizable(0,0)                             # 拡大縮小を禁止
root.iconbitmap('./img/Icon.ico')            # アイコン

#frame作成
frame1=ttk.Frame(master=root,width=700,height=700)
frame1.pack()


#ラジオボタンの選択結果を入れる変数

var=tk.IntVar()

#gif読み込み
TM1 = tk.PhotoImage("./img/TM_1.gif")
gif_index = 0
GameOverGif = tk.PhotoImage("./img/GameOver.gif")
GameOver_index=0


#名前入力テキストボックス
txt=tk.Entry(width=20)

#効果音読み込み

pygame.init()

KoukaonKihon={}
KoukaonKihon[0]=pygame.mixer.Sound("./sound/Medetai.wav")
KoukaonKihon[1]=pygame.mixer.Sound("./sound/Syoukai.wav")
KoukaonKihon[2]=pygame.mixer.Sound("./sound/BtnPush.wav")
KoukaonKihon[3]=pygame.mixer.Sound("./sound/Save.wav")
KoukaonKihon[4]=pygame.mixer.Sound("./sound/SetteiIcon.wav")
KoukaonKihon[5]=pygame.mixer.Sound("./sound/BatuGame.wav")
KoukaonKihon[6]=pygame.mixer.Sound("./sound/BukimiBird.wav")

KoukaonSeibutu={}
KoukaonSeibutu[0]=pygame.mixer.Sound("./sound/SeibutuClick.wav")
KoukaonSeibutu[1]=pygame.mixer.Sound("./sound/SeibutuDousa.wav")
KoukaonSeibutu[2]=pygame.mixer.Sound("./sound/SeibutuAseri.wav")


def close():
    print('終了処理')
    features[0].cancelled()
    features[1].cancelled()
    root.destroy()

def KoukaonTest():
    KoukaonKihon[0].play()

#BGMを流す
def BGM():
    
    #初期設定
    pygame.mixer.init(frequency=44100)

    #time.sleep(2)#秒流す

    '''
    #マルチスレッドの話

    print('画面表示処理')
    print(features[0].running())
    print(features[0].done())
    print('BGM処理')
    print(features[1].running())
    print(features[1].done())
    
    '''


#Title開く前の準備処理
def TitleJunbi():

    s=int(0)
    with open('./Syori/SonotaSyori/saveCheck.txt','r',encoding='utf-8')as f:
        s=int(f.read())

    if s==1:

        sound.load()

    if sound.BGMOnOff==True:
        #音楽ファイルの読み込み
        pygame.mixer.music.load("./sound/Opening.wav")
        #音量調節
        pygame.mixer.music.set_volume(sound.getBGMvol())#0.0~1.0
        print(sound.getBGMvol())

        #音楽の再生回数（無限）
        pygame.mixer.music.play(-1)
    
    Title()

#タイトル画面
def Title():

    syokika()#データすべて初期化

    #キャンバス準備
    cvTitle=tk.Canvas(frame1,bg="black",height=700,width=700)
    #キャンバス表示
    cvTitle.place(x=0,y=0)
    #Title画面
    imgTitle = tk.PhotoImage(file="./img/Title.png", width=700, height=700)
    #imgTitle =imgTitle.zoom(2,2)#画像拡大
    cvTitle.create_image(0, 0, image=imgTitle, anchor=tk.NW)#イメージ表示
    

    btnHazime=tk.Button(frame1,text='はじめから',font=("MSゴシック","16","bold"),bg='white',width=11, height=2,command=Umareru)
    btnHazime.place(x=170,y=550)
    btnTuduki=tk.Button(frame1,text='つづきから',font=("MSゴシック","16","bold"),bg='white',width=11, height=2,command=DataHyouji)
    btnTuduki.place(x=380,y=550)

    #設定アイコン画像
    #イメージ作成
    imgSettei = tk.PhotoImage(file="./img/SetteiIcon.png", width=500, height=500)
    #imgHaikei =imgHaikei.zoom(2,2)#画像拡大
    cvTitle.create_image(5, 615, image=imgSettei, anchor=tk.NW)#イメージ表示

    #Title()から設定を押したということを記す
    ukewatasi.setint(1)
    #Title()の音楽ファイルの住所を記す
    ukewatasi.setString1("./sound/Opening.wav")
    


    #クリックしたらクリックイベント判定処理へ
    cvTitle.bind('<ButtonPress-1>',ClickSyori)

    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示


def Umareru():

    syokika()#データすべて初期化  
    
    #BGM変更
    if sound.BGMOnOff==True:
        pygame.mixer.music.stop()#今流れてる曲を止める
        #音楽ファイルの読み込み
        pygame.mixer.music.load("./sound/KekkaMati.wav")
        #音量調節
        pygame.mixer.music.set_volume(sound.getBGMvol())#0.0~1.0
        #音楽の再生回数（無限）
        pygame.mixer.music.play(-1)



    #男か女か決める
    Num=random.randint(0,1)
    Seibutu.setDanjo(Num)

    #顔の形、色決める
    
    Seibutu.setface()

    label = tk.Label(frame1, image=TM1)
    
    label.place(x=0,y=0)

    t1 = time.time() 
    root.after_idle(next_frame)
    root.protocol("WM_DELETE_WINDOW",close)

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    root.mainloop()#表示

def next_frame():
        global gif_index
        try:
            # XXX: 次のフレームに移る
            TM1.configure(format="gif -index {}".format(gif_index))

            gif_index += 1
        except tk.TclError:
            gif_index = 0
            return next_frame()
        else:
            t2 = time.time()
            if not gif_index==7:#7秒たったらストップ
                #print(gif_index)
                root.after(0, next_frame) # XXX: アニメーション速度が固定多ければ多いほど遅い
            else:


                #BGM変更
                if sound.BGMOnOff==True:
                    pygame.mixer.music.stop()#今流れてる曲を止める
                    #音楽ファイルの読み込み
                    pygame.mixer.music.load("./sound/UresiHasyagi.wav")
                    #音量調節
                    pygame.mixer.music.set_volume(sound.getBGMvol())#0.0~1.0
                    #音楽の再生回数（無限）
                    pygame.mixer.music.play(-1)

                #ボタン押した音
                if sound.KoukaonOnOff==True:
                    KoukaonKihon[0].play()
                #キャンバス準備
                cvTanjo=tk.Canvas(frame1,bg="white",height=700,width=700)
                #キャンバス表示
                cvTanjo.place(x=0,y=0)

                #イメージ作成
                imgTanjo = tk.PhotoImage(file="./img/TanjouHaikei2.png", width=700, height=700)
                #imgHaikei =imgHaikei.zoom(2,2)#画像拡大
                cvTanjo.create_image(0, 0, image=imgTanjo, anchor=tk.NW)#イメージ表示

                #生物
                imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
                #imgTitle =imgTitle.zoom(2,2)#画像拡大
                cvTanjo.create_image(240, 160, image=imgSkao, anchor=tk.NW)#イメージ表示

                labelDanjo = tk.Label(frame1,text=Seibutu.Danjo,font=("MSゴシック","25","bold"),fg=Seibutu.Iro,bg='LightCyan',width=5, height=1)
                labelDanjo.place(x=290,y=390)

                #NameCheckのときのみラベルを見せるための受け渡し
                ukewatasi.setString('PaleVioletRed1','PaleVioletRed1')

                btnHanasu=tk.Button(frame1,text='次へ',font=("MSゴシック","12","bold"),bg='white',width=12, height=2,command=GetName1)
                btnHanasu.place(x=285,y=585)
    

                root.mainloop()#表示


def GetName1():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    TyuiH,TyuiF=ukewatasi.getString2()#NameCheckのときのみラベルを見せるための受け渡し
    #キャンバス準備Tsize
    cvGetName=tk.Canvas(frame1,bg="black",height=700,width=700)
    #キャンバス表示
    cvGetName.place(x=0,y=0)
    
    #Namae画面
    imgNameNyuryoku = tk.PhotoImage(file="./img/NameNyuryoku.png", width=700, height=700)
    #imgTitle =imgTitle.zoom(2,2)#画像拡大
    cvGetName.create_image(0, 0, image=imgNameNyuryoku, anchor=tk.NW)#イメージ表示
    
    #説明
    
    labelSetumei1 = tk.Label(frame1,text='★　おめでとう！　★',font=("MSゴシック","16","bold"),bg='white',width=40, height=2)
    labelSetumei1.place(x=80,y=80)
    labelSetumei2 = tk.Label(frame1,text='今ここに、生物が誕生しました。',font=("MSゴシック","16","bold"),bg='white',width=40, height=2)
    labelSetumei2.place(x=80,y=130)

    labelSetumei3_1 = tk.Label(frame1,text='性別は、',font=("MSゴシック","16","bold"),bg='white',width=8, height=2)
    labelSetumei3_1.place(x=230,y=180)
    labelSetumei3_2 = tk.Label(frame1,text=Seibutu.Danjo,font=("MSゴシック","16","bold"),bg='LightCyan',fg=Seibutu.Iro,width=5, height=2)
    labelSetumei3_2.place(x=320,y=180)
    labelSetumei3_3 = tk.Label(frame1,text='です。',font=("MSゴシック","16","bold"),bg='white',width=5, height=2)
    labelSetumei3_3.place(x=390,y=180)

    labelSetumei4 = tk.Label(frame1,text='名前を決めてあげてください。',font=("MSゴシック","16","bold"),bg='white',width=40, height=2)
    labelSetumei4.place(x=80,y=230)
    
    #名前項目
    labelName = tk.Label(frame1,text='なまえ :',font=("MSゴシック","10","bold"),bg='white',width=8, height=1)
    labelName.place(x=140,y=460)
    
    
    #名前入力テキストボックス
    txt.place(x=250,y=460)
    #注意事項
    labelTyui = tk.Label(frame1,text='※５文字以内',font=("MSゴシック","10","bold"),bg='PaleVioletRed',width=22, height=1)
    labelTyui.place(x=220,y=490)
    #注意事項2
    labelTyui2 = tk.Label(frame1,text='※入力条件と一致しませんでした',font=("MSゴシック","10","bold"),fg=TyuiF,bg=TyuiH,width=30, height=1)
    labelTyui2.place(x=220,y=520)
    #ちゃんくん
    labelKunchan = tk.Label(frame1,text=Seibutu.KunChan,font=("MSゴシック","10","bold"),bg='LightCyan',width=5, height=1)
    labelKunchan.place(x=400,y=460)

    #決定ボタン
    btnKettei=tk.Button(frame1,text='決定',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=NameCheck)
    btnKettei.place(x=470,y=458)
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def NameCheck():
    name=txt.get()
    if len(name)<6 and len(name)>0:
        
        Seibutu.setName(name)#名前保存
        #名前入力テキストボックス
        txt.delete(0,tk.END)#中身を殻にしただけ
        txt.place(x=900,y=900)#移動して隠しただけ
        NameKakunin()
        
            
    else:
        #NameCheckのときのみラベルを見せるための受け渡し
        ukewatasi.setString('red','black')
        GetName1()
def NameKakunin():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    #キャンバス準備T
    cvNameKakunin=tk.Canvas(frame1,bg="black",height=700,width=700)
    #キャンバス表示
    cvNameKakunin.place(x=0,y=0)
    
    #Namae画面
    imgNameKakunin = tk.PhotoImage(file="./img/NameKakunin.png", width=700, height=700)
    cvNameKakunin.create_image(0, 0, image=imgNameKakunin, anchor=tk.NW)#イメージ表示

    labelSetumei1 = tk.Label(frame1,text='謎の生物の名前は',font=("MSゴシック","20","bold"),bg='white',width=20, height=2)
    labelSetumei1.place(x=180,y=80)
    labelName = tk.Label(frame1,text=Seibutu.getName(),font=("MSゴシック","20","bold"),bg='LightCyan',fg=Seibutu.Iro,width=9, height=2)
    labelName.place(x=110,y=180)
    labelKakunin = tk.Label(frame1,text=Seibutu.KunChan+'に、決まりました',font=("MSゴシック","20","bold"),bg='white',width=18, height=2)
    labelKakunin.place(x=270,y=180)

    #生物
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(2,2)#画像縮小
    cvNameKakunin.create_image(305, 410, image=imgSkao, anchor=tk.NW)#イメージ表示


    btnHanasu=tk.Button(frame1,text='次へ',font=("MSゴシック","12","bold"),bg='white',width=12, height=2,command=beforIkusei)
    btnHanasu.place(x=290,y=585)

    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def beforIkusei():#Ikusei画面に行く準備

    if sound.BGMOnOff==True:
        #音楽ファイルの読み込み
        pygame.mixer.music.load("./sound/BGM.wav")
        #音量調節
        pygame.mixer.music.set_volume(sound.getBGMvol())#0.0~1.0

        #音楽の再生回数（無限）
        pygame.mixer.music.play(-1)

    Ikusei()

def Ikusei():
    Seibutu.test()

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()   
    
    #キャンバス準備
    cvIkusei=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvIkusei.place(x=0,y=0)

    #イメージ作成
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    #imgHaikei =imgHaikei.zoom(2,2)#画像拡大
    cvIkusei.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #プロフィール画面
    imgPurofeel = tk.PhotoImage(file="./img/Purofeel.png", width=300, height=400)
    cvIkusei.create_image(5, 5, image=imgPurofeel, anchor=tk.NW)#イメージ表示

    #セーブボタン画像
    #イメージ作成
    imgsave = tk.PhotoImage(file="./img/saveButton.png", width=700, height=700)
    #imgHaikei =imgHaikei.zoom(2,2)#画像拡大
    cvIkusei.create_image(590, 600, image=imgsave, anchor=tk.NW)#イメージ表示

    #設定アイコン画像
    #イメージ作成
    imgSettei = tk.PhotoImage(file="./img/SetteiIcon.png", width=500, height=500)
    #imgHaikei =imgHaikei.zoom(2,2)#画像拡大
    cvIkusei.create_image(5, 615, image=imgSettei, anchor=tk.NW)#イメージ表示

    #Homeアイコン画像
    #イメージ作成
    imgHome = tk.PhotoImage(file="./img/HomeIcon.png", width=500, height=500)
    #imgHaikei =imgHaikei.zoom(2,2)#画像拡大
    cvIkusei.create_image(130, 620, image=imgHome, anchor=tk.NW)#イメージ表示

    #Ikusei()の音楽ファイルの住所を記す
    ukewatasi.setString1("./sound/BGM.wav")

    ukewatasi.setint(0)

    Proname = tk.Label(frame1,text=Seibutu.getName(),font=("MSゴシック","12","bold"),bg='white',width=8, height=1)
    Proname.place(x=74,y=27)

    Pro1 = tk.Label(frame1,text=str(Seibutu.Nenrei)+' さい',font=("MSゴシック","12","bold"),bg='white',width=11, height=1)
    Pro1.place(x=84,y=70)
    Pro2 = tk.Label(frame1,text=Seibutu.Danjo,font=("MSゴシック","12","bold"),bg='white',width=11, height=1)
    Pro2.place(x=84,y=100)
    Pro3 = tk.Label(frame1,text=Seibutu.Seikaku,font=("MSゴシック","12","bold"),bg='white',width=11, height=1)
    Pro3.place(x=84,y=133)
    Pro4 = tk.Label(frame1,text=Seibutu.SukiTabemono,font=("MSゴシック","9","bold"),bg='white',width=15, height=1)
    Pro4.place(x=84,y=162)
    Pro5 = tk.Label(frame1,text=Seibutu.SukiNomimono,font=("MSゴシック","9","bold"),bg='white',width=15, height=1)
    Pro5.place(x=84,y=195)
    Pro6 = tk.Label(frame1,text=Seibutu.Manpukudo*'■',font=("MSゴシック","12","bold"),bg='white',width=11, height=1, anchor="w")
    Pro6.place(x=85,y=219)
    Pro7 = tk.Label(frame1,text=Seibutu.Uruoido*'■',font=("MSゴシック","12","bold"),bg='white',width=11, height=1 ,anchor="w")
    Pro7.place(x=85,y=256)

    #ボタン
    btnHanasu=tk.Button(frame1,text='1.話しかける',font=("MSゴシック","12","bold"),bg='yellow',width=12, height=2,command=Hanasikakeru1_1)
    btnHanasu.place(x=550,y=80)
    btnTaberu=tk.Button(frame1,text='2.食べさせる',font=("MSゴシック","12","bold"),bg='LightSalmon',width=12, height=2,command=TTarnCheck)
    btnTaberu.place(x=550,y=150)
    btnNomu=tk.Button(frame1,text='3.飲ませる',font=("MSゴシック","12","bold"),bg='LightSkyBlue',width=12, height=2,command=NTarnCheck)
    btnNomu.place(x=550,y=220)
    btnSukinsippu=tk.Button(frame1,text='4.ふれあう',font=("MSゴシック","12","bold"),bg='PaleVioletRed1',width=12, height=2,command=Hureau4_1)
    btnSukinsippu.place(x=550,y=290)

    if Seibutu.Nenrei>=7:
        btnKaiwa=tk.Button(frame1,text='5.会話する',font=("MSゴシック","12","bold"),bg='yellow',width=12, height=2,command=KaiwaJunbi)
        btnKaiwa.place(x=550,y=360)


    #生物


    if not Seibutu.gethand()=='a':#手
        print('a')
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvIkusei.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvIkusei.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    
    imgface = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgface =imgface.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvIkusei.create_image(Seibutu.sx, Seibutu.sy, image=imgface, anchor=tk.NW)#イメージ表示
    

    if not Seibutu.geteye()=='a':#目
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvIkusei.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getnose()=='a':#鼻
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvIkusei.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':#口
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvIkusei.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示

    
    #クリックしたらクリックイベント判定処理へ
    cvIkusei.bind('<ButtonPress-1>',ClickSyori)

    #次のときのみラベルを見せるための受け渡し
    ukewatasi.setString('white','white')

    
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示




def TTarnCheck():#食べさせる２ができるターンかチェック

    if True==Tarn.getTTarnCheck():

        Tabesaseru2_1()

    else:#拒否
        
        Kyohi('お腹がいっぱいのようだ')

def NTarnCheck():#飲ませる３ができるターンかチェック
    

    if True==Tarn.getNTarnCheck():

        Nomaseru3_1()

    else:#拒否
        
        Kyohi('喉が渇いていないようだ')

def Kyohi(kotoba):

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    #キャンバス準備
    cv=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cv.place(x=0,y=0)

    #イメージ作成
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    #imgHaikei =imgHaikei.zoom(2,2)#画像拡大
    cv.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/Hukidasi.png", width=700, height=700)
    cv.create_image(50, 25, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text=Seibutu.Name,font=("MSゴシック","18","bold"),fg=Seibutu.Iro,width=10, height=2)
    Setu1.place(x=120,y=70)
    Setu2 = tk.Label(frame1,text=Seibutu.KunChan+' は、',font=("MSゴシック","20","bold"),bg='white',width=10, height=2)
    Setu2.place(x=295,y=70)
    Setu3 = tk.Label(frame1,text=kotoba,font=("MSゴシック","20","bold"),bg='LightCyan',width=22, height=2)
    Setu3.place(x=120,y=140)

    #決定ボタン
    btnHaikei = tk.Label(frame1,text=' ',font=("MSゴシック","18","bold"),bg='PaleVioletRed1',width=6, height=2)
    btnHaikei.place(x=485,y=270)
    btnKettei=tk.Button(frame1,text='OK',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=Ikusei)
    btnKettei.place(x=500,y=285)

    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cv.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cv.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    #生物
    imgface = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgface =imgface.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cv.create_image(Seibutu.sx, Seibutu.sy, image=imgface, anchor=tk.NW)#イメージ表示
        
    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cv.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cv.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cv.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示

    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示


#5会話
def KaiwaJunbi():
    ukewatasi.setint(2)#会話ですよ
    Hanasikakeru1_1()

#話しかける処理

def Hanasikakeru1_1():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()
    
    TyuiH,TyuiF=ukewatasi.getString2()#NameCheckのときのみラベルを見せるための受け渡し
    #キャンバス準備
    cvIkusei=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvIkusei.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvIkusei.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #話しかける時の吹き出し
    imgHanasikakeru = tk.PhotoImage(file="./img/Hanasikakeru.png", width=700, height=700)
    cvIkusei.create_image(50, 180, image=imgHanasikakeru, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text='話しかける言葉を入力してください',font=("MSゴシック","14","bold"),bg='white',width=28, height=2)
    Setu1.place(x=120,y=270)
    Setu2 = tk.Label(frame1,text='※10文字以内',font=("MSゴシック","15","bold"),bg='white',width=20, height=2)
    Setu2.place(x=180,y=320)

    #言葉入力テキストボックス
    txt.place(x=245,y=410)
    #決定ボタン
    btnKettei=tk.Button(frame1,text='決定',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=KotobaCheck)
    btnKettei.place(x=470,y=402)

    #注意事項2
    labelTyui = tk.Label(frame1,text='※入力条件と一致しませんでした',font=("MSゴシック","10","bold"),fg=TyuiF,bg=TyuiH,width=30, height=1)
    labelTyui.place(x=177,y=450)

    #会話終了ボタン

    if ukewatasi.getint()==2:#５会話　だったら

            ukewatasi.setint(2)#もう一回　2(5会話)格納

            if not Seibutu.KaiwaGetCount()==0:#1回目の会話じゃなかったら

                #さっき生物が言った言葉吹き出し
                imgHukidasi = tk.PhotoImage(file="./img/SHukidasiSmall.png", width=400, height=200)
                cvIkusei.create_image(15, 0, image=imgHukidasi, anchor=tk.NW)#イメージ表示

                skotoba = tk.Label(frame1,text=Seibutu.Kotoba.kiokuSkotoba,font=("MSゴシック","15","bold"),bg='white',width=22, height=2)
                skotoba.place(x=75,y=50)

                btnKaiwa=tk.Button(frame1,text='会話終了',font=("MSゴシック","18","bold"),bg='red',width=12, height=2,command=KaiwaSaigo)
                btnKaiwa.place(x=480,y=500)


    #次のときのみラベルを見せるための受け渡し
    ukewatasi.setString('white','white')
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def KotobaCheck():
    kotoba=txt.get()
    if len(kotoba)<=10 and len(kotoba)>0:

        if ukewatasi.getint()==2:#５会話　だったら

            ukewatasi.setint(2)#もう一回　2(5会話)格納

            if Seibutu.KaiwaGetCount()==0:#1回目の会話だったら

                Seibutu.setKotoba(kotoba)#言葉保存
            
            else:#1回目じゃなかったら

                Seibutu.setKaiwaKotoba(kotoba)#生物が言った言葉に対する返事として保存

        else:
            Seibutu.setKotoba(kotoba)#言葉保存
            Tarn.setHTarn()

        #テキストボックス
        txt.delete(0,tk.END)#中身を殻にしただけ
        txt.place(x=900,y=900)#移動して隠しただけ
        Hanasikakeru1_2()        
            
    else:
        #NameCheckのときのみラベルを見せるための受け渡し
        ukewatasi.setString('red','black')
        Hanasikakeru1_1()


def Hanasikakeru1_2():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()
    
    #キャンバス準備
    cvHanasikakeru1_2=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvHanasikakeru1_2.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvHanasikakeru1_2.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/SHukidasi.png", width=700, height=700)
    cvHanasikakeru1_2.create_image(50, 20, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    if Seibutu.Nenrei>=6:

        var.set(0) #ラジオボタンを０にセット
        #判定
        imgHantei = tk.PhotoImage(file="./img/Hantei.png", width=300, height=250)
        cvHanasikakeru1_2.create_image(0, 130, image=imgHantei, anchor=tk.NW)#イメージ表示

        #ラジオボタン
        rdo1=tk.Radiobutton(frame1,value=1,text='合ってる',variable=var,font=("MSゴシック","10","bold"),bg='yellow',width=6, height=1)
        rdo1.place(x=40,y=250)
        rdo2=tk.Radiobutton(frame1,value=0,text='ふつう',variable=var,font=("MSゴシック","10","bold"),bg='LightSalmon',width=6, height=1)
        rdo2.place(x=115,y=250)
        rdo3=tk.Radiobutton(frame1,value=2,text='ちがう',variable=var,font=("MSゴシック","10","bold"),bg='LightSkyBlue',width=6, height=1)
        rdo3.place(x=190,y=250)

    henji=''

    #会話終了ボタン

    if ukewatasi.getint()==2:#５会話　だったら

            ukewatasi.setint(2)#もう一回　2(5会話)格納

            henji=Seibutu.KaiwaHenji()

            if not Seibutu.KaiwaGetCount()==0:#1回目の会話じゃなかったら

                btnKaiwa=tk.Button(frame1,text='会話終了',font=("MSゴシック","18","bold"),bg='red',width=12, height=2,command=KaiwaSaigo)
                btnKaiwa.place(x=480,y=500)
    
    else:
        henji=Seibutu.HanasikakeruHenji()

    Setu1 = tk.Label(frame1,text=henji,font=("MSゴシック","20","bold"),bg='white',width=26, height=2)
    Setu1.place(x=120,y=90)

    #決定ボタン
    btnKettei=tk.Button(frame1,text='次へ',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=HanasikakeruSaigo)
    btnKettei.place(x=500,y=167)


    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvHanasikakeru1_2.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvHanasikakeru1_2.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    #生物
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvHanasikakeru1_2.create_image(Seibutu.sx, Seibutu.sy, image=imgSkao, anchor=tk.NW)#イメージ表示

    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvHanasikakeru1_2.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvHanasikakeru1_2.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvHanasikakeru1_2.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def HanasikakeruSaigo():

    if Seibutu.Nenrei>=6: #返事に対する評価処理
       
        radio=var.get()#ラジオボタンの値ゲット
        
        if radio!=0:#判定が普通じゃなかったら
            Seibutu.HenjiHanteiSyori(radio)#返事判定処理へ
    
    if ukewatasi.getint()==2:#５会話　だったら

        Seibutu.KaiwaSetCount()

        ukewatasi.setint(2)#もう一回　2(5会話)格納

        Hanasikakeru1_1()

    else:#１話しかける　だったら

        eventkime()

def KaiwaSaigo():

    Seibutu.KaiwaSyuryo()#会話終了処理

    txt.delete(0,tk.END)#中身を殻にしただけ
    txt.place(x=900,y=900)#移動して隠しただけ

    eventkime()


#食べさせる処理

def Tabesaseru2_1():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    TyuiH,TyuiF=ukewatasi.getString2()#NameCheckのときのみラベルを見せるための受け渡し
    #キャンバス準備
    cvIkusei=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvIkusei.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvIkusei.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #食べさせる時の吹き出し
    imgTabesaseru = tk.PhotoImage(file="./img/Tabesaseru.png", width=700, height=700)
    cvIkusei.create_image(50, 180, image=imgTabesaseru, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text='何を食べさせますか',font=("MSゴシック","20","bold"),bg='white',width=16, height=2)
    Setu1.place(x=180,y=250)
    Setu2 = tk.Label(frame1,text='※１０文字以内',font=("MSゴシック","15","bold"),bg='white',width=20, height=2)
    Setu2.place(x=180,y=320)

    #食べ物入力テキストボックス
    txt.place(x=245,y=410)
    #決定ボタン
    btnKettei=tk.Button(frame1,text='決定',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=TabemonoCheck)
    btnKettei.place(x=470,y=402)

    #注意事項2
    labelTyui = tk.Label(frame1,text='※入力条件と一致しませんでした',font=("MSゴシック","10","bold"),fg=TyuiF,bg=TyuiH,width=30, height=1)
    labelTyui.place(x=177,y=450)


    #次のときのみラベルを見せるための受け渡し
    ukewatasi.setString('white','white')
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def TabemonoCheck():
    tabemono=txt.get()
    if len(tabemono)<11 and len(tabemono)>0:

        Seibutu.setTabemono(tabemono)#名前保存
        #テキストボックス
        txt.delete(0,tk.END)#中身を殻にしただけ
        txt.place(x=900,y=900)#移動して隠しただけ
        Tabesaseru2_2()

    else:
        #NameCheckのときのみラベルを見せるための受け渡し
        ukewatasi.setString('red','black')
        Tabesaseru2_1()

def Tabesaseru2_2():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    TyuiH,TyuiF=ukewatasi.getString2()#NameCheckのときのみラベルを見せるための受け渡し
    #キャンバス準備
    cvTabesaseruKotoba=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvTabesaseruKotoba.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvTabesaseruKotoba.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/TabesaseruKotoba.png", width=700, height=700)
    cvTabesaseruKotoba.create_image(50, 180, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text=Seibutu.kioku,font=("MSゴシック","18","bold"),bg='LightCyan',width=len(Seibutu.kioku)*2, height=2)
    Setu1.place(x=115,y=250)
    Setu2 = tk.Label(frame1,text='を食べさせる時に',font=("MSゴシック","18","bold"),bg='white',width=13, height=2)
    Setu2.place(x=115+len(Seibutu.kioku)*30,y=250)
    Setu3 = tk.Label(frame1,text='言う言葉を教えてあげてください',font=("MSゴシック","18","bold"),bg='white',width=30, height=2)
    Setu3.place(x=115,y=300)
    Setu4 = tk.Label(frame1,text='※10文字以内',font=("MSゴシック","12","bold"),bg='white',width=20, height=2)
    Setu4.place(x=200,y=350)

    #食べ物入力テキストボックス
    txt.place(x=245,y=410)
    #決定ボタン
    btnKettei=tk.Button(frame1,text='決定',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=TabemonoKotobaCheck)
    btnKettei.place(x=470,y=402)
    
    #注意事項2
    labelTyui = tk.Label(frame1,text='※入力条件と一致しませんでした',font=("MSゴシック","10","bold"),fg=TyuiF,bg=TyuiH,width=30, height=1)
    labelTyui.place(x=177,y=450)
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def TabemonoKotobaCheck():
    kotoba=txt.get()
    if len(kotoba)<11 and len(kotoba)>0:
        
        Seibutu.setTKotoba(kotoba)#名前保存
        
        Tarn.setTTarn()
        #テキストボックス
        txt.delete(0,tk.END)#中身を殻にしただけ
        txt.place(x=900,y=900)#移動して隠しただけ
        Tabesaseru2_3()
            
    else:
        #NameCheckのときのみラベルを見せるための受け渡し
        ukewatasi.setString('red','black')
        Tabesaseru2_2()
def Tabesaseru2_3():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()
    
    #キャンバス準備
    cvTabesaseru2_3=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvTabesaseru2_3.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvTabesaseru2_3.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/Hukidasi.png", width=700, height=700)
    cvTabesaseru2_3.create_image(50, 25, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text='あなたは',font=("MSゴシック","20","bold"),bg='white',width=6, height=2)
    Setu1.place(x=120,y=70)
    Setu2 = tk.Label(frame1,text=Seibutu.kioku,font=("MSゴシック","20","bold"),bg='LightCyan',width=len(Seibutu.kioku)*2, height=2)
    Setu2.place(x=240,y=70)
    Setu3 = tk.Label(frame1,text='を、',font=("MSゴシック","20","bold"),bg='white',width=3, height=2)
    Setu3.place(x=240+len(Seibutu.kioku)*35,y=70)
    Setu4 = tk.Label(frame1,text=Seibutu.Name,font=("MSゴシック","18","bold"),bg='white',fg=Seibutu.Iro,width=10, height=2)
    Setu4.place(x=100,y=140)
    Setu4 = tk.Label(frame1,text=Seibutu.KunChan+' に食べさせました！',font=("MSゴシック","18","bold"),bg='white',width=20, height=2)
    Setu4.place(x=275,y=140)

    #決定ボタン
    btnHaikei = tk.Label(frame1,text=' ',font=("MSゴシック","18","bold"),bg='PaleVioletRed1',width=6, height=2)
    btnHaikei.place(x=485,y=270)
    btnKettei=tk.Button(frame1,text='OK',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=Tabesaseru2_4)
    btnKettei.place(x=500,y=285)

    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvTabesaseru2_3.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvTabesaseru2_3.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    #生物
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvTabesaseru2_3.create_image(Seibutu.sx, Seibutu.sy, image=imgSkao, anchor=tk.NW)#イメージ表示

    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvTabesaseru2_3.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvTabesaseru2_3.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvTabesaseru2_3.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示

    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def Tabesaseru2_4():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()
    
    #キャンバス準備
    cvTabesaseru2_4=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvTabesaseru2_4.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvTabesaseru2_4.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/SHukidasi.png", width=700, height=700)
    cvTabesaseru2_4.create_image(50, 20, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text=Seibutu.TabesaseruHenji(),font=("MSゴシック","20","bold"),bg='white',width=26, height=2)
    Setu1.place(x=120,y=90)

    #決定ボタン
    btnKettei=tk.Button(frame1,text='次へ',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=eventkime)
    btnKettei.place(x=500,y=167)

    #生物

    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvTabesaseru2_4.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvTabesaseru2_4.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvTabesaseru2_4.create_image(Seibutu.sx, Seibutu.sy, image=imgSkao, anchor=tk.NW)#イメージ表示

    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvTabesaseru2_4.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvTabesaseru2_4.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvTabesaseru2_4.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示


#飲ませる処理

def Nomaseru3_1():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    TyuiH,TyuiF=ukewatasi.getString2()#NameCheckのときのみラベルを見せるための受け渡し
    #キャンバス準備
    cvIkusei=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvIkusei.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvIkusei.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #飲ませる時の吹き出し
    imgNomaseru = tk.PhotoImage(file="./img/Nomaseru.png", width=700, height=700)
    cvIkusei.create_image(50, 180, image=imgNomaseru, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text='何を飲ませますか',font=("MSゴシック","20","bold"),bg='white',width=16, height=2)
    Setu1.place(x=180,y=250)
    Setu2 = tk.Label(frame1,text='※１０文字以内',font=("MSゴシック","15","bold"),bg='white',width=20, height=2)
    Setu2.place(x=180,y=320)

    #飲み物入力テキストボックス
    txt.place(x=245,y=410)
    #決定ボタン
    btnKettei=tk.Button(frame1,text='決定',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=NomimonoCheck)
    btnKettei.place(x=470,y=402)

    #注意事項2
    labelTyui = tk.Label(frame1,text='※入力条件と一致しませんでした',font=("MSゴシック","10","bold"),fg=TyuiF,bg=TyuiH,width=30, height=1)
    labelTyui.place(x=177,y=450)


    #次のときのみラベルを見せるための受け渡し
    ukewatasi.setString('white','white')
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def NomimonoCheck():

    nomimono=txt.get()

    if len(nomimono)<11 and len(nomimono)>0:

        Seibutu.setNomimono(nomimono)#名前保存
        Tarn.setNTarn()
        #テキストボックス
        txt.delete(0,tk.END)#中身を殻にしただけ
        txt.place(x=900,y=900)#移動して隠しただけ
        Nomaseru3_2()

    else:
        #NameCheckのときのみラベルを見せるための受け渡し
        ukewatasi.setString('red','black')
        Nomaseru3_1()

def Nomaseru3_2():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    TyuiH,TyuiF=ukewatasi.getString2()#NameCheckのときのみラベルを見せるための受け渡し
    #キャンバス準備
    cvNomaseruKotoba=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvNomaseruKotoba.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvNomaseruKotoba.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/NomaseruKotoba.png", width=700, height=700)
    cvNomaseruKotoba.create_image(50, 180, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text=Seibutu.kioku,font=("MSゴシック","18","bold"),bg='LightCyan',width=len(Seibutu.kioku)*2, height=2)
    Setu1.place(x=115,y=250)
    Setu2 = tk.Label(frame1,text='を飲ませる時に',font=("MSゴシック","18","bold"),bg='white',width=13, height=2)
    Setu2.place(x=115+len(Seibutu.kioku)*30,y=250)
    Setu3 = tk.Label(frame1,text='言う言葉を教えてあげてください',font=("MSゴシック","18","bold"),bg='white',width=30, height=2)
    Setu3.place(x=115,y=300)
    Setu4 = tk.Label(frame1,text='※10文字以内',font=("MSゴシック","12","bold"),bg='white',width=20, height=2)
    Setu4.place(x=200,y=350)

    #飲み物入力テキストボックス
    txt.place(x=245,y=410)
    #決定ボタン
    btnKettei=tk.Button(frame1,text='決定',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=NomimonoKotobaCheck)
    btnKettei.place(x=470,y=402)
    
    #注意事項2
    labelTyui = tk.Label(frame1,text='※入力条件と一致しませんでした',font=("MSゴシック","10","bold"),fg=TyuiF,bg=TyuiH,width=30, height=1)
    labelTyui.place(x=177,y=450)
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def NomimonoKotobaCheck():
    kotoba=txt.get()
    if len(kotoba)<11 and len(kotoba)>0:

        Seibutu.setNKotoba(kotoba)#名前保存
        #テキストボックス
        txt.delete(0,tk.END)#中身を殻にしただけ
        txt.place(x=900,y=900)#移動して隠しただけ
        Nomaseru3_3()
            
    else:
        #NameCheckのときのみラベルを見せるための受け渡し
        ukewatasi.setString('red','black')
        Nomaseru3_2()
def Nomaseru3_3():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()
    
    #キャンバス準備
    cvNomaseru3_3=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvNomaseru3_3.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvNomaseru3_3.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/Hukidasi.png", width=700, height=700)
    cvNomaseru3_3.create_image(50, 25, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text='あなたは',font=("MSゴシック","20","bold"),bg='white',width=6, height=2)
    Setu1.place(x=120,y=70)
    Setu2 = tk.Label(frame1,text=Seibutu.kioku,font=("MSゴシック","20","bold"),bg='LightCyan',width=len(Seibutu.kioku)*2, height=2)
    Setu2.place(x=240,y=70)
    Setu3 = tk.Label(frame1,text='を、',font=("MSゴシック","20","bold"),bg='white',width=3, height=2)
    Setu3.place(x=240+len(Seibutu.kioku)*35,y=70)
    Setu4 = tk.Label(frame1,text=Seibutu.Name,font=("MSゴシック","18","bold"),bg='white',fg=Seibutu.Iro,width=10, height=2)
    Setu4.place(x=100,y=140)
    Setu4 = tk.Label(frame1,text=Seibutu.KunChan+' に飲ませました！',font=("MSゴシック","18","bold"),bg='white',width=20, height=2)
    Setu4.place(x=275,y=140)

    #決定ボタン
    btnHaikei = tk.Label(frame1,text=' ',font=("MSゴシック","18","bold"),bg='PaleVioletRed1',width=6, height=2)
    btnHaikei.place(x=485,y=270)
    btnKettei=tk.Button(frame1,text='OK',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=Nomaseru3_4)
    btnKettei.place(x=500,y=285)

    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvNomaseru3_3.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvNomaseru3_3.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    #生物
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvNomaseru3_3.create_image(Seibutu.sx, Seibutu.sy, image=imgSkao, anchor=tk.NW)#イメージ表示

    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvNomaseru3_3.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvNomaseru3_3.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvNomaseru3_3.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def Nomaseru3_4():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    #キャンバス準備
    cvNomaseru3_4=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvNomaseru3_4.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvNomaseru3_4.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/SHukidasi.png", width=700, height=700)
    cvNomaseru3_4.create_image(50, 20, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text=Seibutu.NomaesruHenji(),font=("MSゴシック","20","bold"),bg='white',width=26, height=2)
    Setu1.place(x=120,y=90)

    #決定ボタン
    btnKettei=tk.Button(frame1,text='次へ',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=eventkime)
    btnKettei.place(x=500,y=167)

    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvNomaseru3_4.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示

    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvNomaseru3_4.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    #生物
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvNomaseru3_4.create_image(Seibutu.sx, Seibutu.sy, image=imgSkao, anchor=tk.NW)#イメージ表示

    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvNomaseru3_4.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示

    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvNomaseru3_4.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvNomaseru3_4.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示

    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

#ふれあうの処理

def Hureau4_1():


    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    #キャンバス準備
    cvIkusei=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvIkusei.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvIkusei.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #ふれあう時の吹き出し
    imgNomaseru = tk.PhotoImage(file="./img/HureauKotoba1.png", width=700, height=700)
    cvIkusei.create_image(50, 107, image=imgNomaseru, anchor=tk.NW)#イメージ表示

    #説明文

    Setu1 = tk.Label(frame1,text='どのようにふれあいますか?',font=("MSゴシック","18","bold"),bg='white',width=21, height=2)
    Setu1.place(x=140,y=190)

    #Setu2 = tk.Label(frame1,text='1つ選択してください',font=("MSゴシック","17","bold"),bg='white',width=21, height=2)
    #Setu2.place(x=200,y=260)

    #ラジオボタン
    rdo1=tk.Radiobutton(frame1,value=0,text='なでる',variable=var,font=("MSゴシック","12","bold"),bg='yellow',width=5, height=1)
    rdo1.place(x=130,y=350)
    rdo2=tk.Radiobutton(frame1,value=1,text='ハグする',variable=var,font=("MSゴシック","12","bold"),bg='LightSalmon',width=7, height=1)
    rdo2.place(x=220,y=350)
    rdo3=tk.Radiobutton(frame1,value=2,text='だっこする',variable=var,font=("MSゴシック","12","bold"),bg='LightSkyBlue',width=9, height=1)
    rdo3.place(x=335,y=350)
    rdo4=tk.Radiobutton(frame1,value=3,text='キスする',variable=var,font=("MSゴシック","12","bold"),bg='PaleVioletRed1',width=7, height=1)
    rdo4.place(x=465,y=350)

    #決定ボタン
    btnKettei=tk.Button(frame1,text='決定',font=("MSゴシック","16","bold"),bg='lemon chiffon',width=5, height=1,command=Hureau4_2)
    btnKettei.place(x=300,y=440)

    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示
    #Seibutu.setAijou()
    #TarnKirikae()

def Hureau4_2():

    
    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    #ふれあうの更新処理
    hiragana,color=Seibutu.setAijou(var.get())

    TyuiH,TyuiF=ukewatasi.getString2()#NameCheckのときのみラベルを見せるための受け渡し

    #キャンバス準備
    cvIkusei=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvIkusei.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvIkusei.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #ふれあう時の吹き出し
    imgNomaseru = tk.PhotoImage(file="./img/HureauKotoba2.png", width=700, height=700)
    cvIkusei.create_image(50, 180, image=imgNomaseru, anchor=tk.NW)#イメージ表示

    #説明文

    Setu1 = tk.Label(frame1,text=hiragana,font=("MSゴシック","18","bold"),bg=color,width=9, height=2)
    Setu1.place(x=230,y=250)
    Setu2 = tk.Label(frame1,text='ときに',font=("MSゴシック","17","bold"),bg='white',width=6, height=2)
    Setu2.place(x=375,y=250)
    Setu3 = tk.Label(frame1,text='言う言葉を入力してください',font=("MSゴシック","17","bold"),bg='white',width=26, height=2)
    Setu3.place(x=160,y=300)
    Setu4 = tk.Label(frame1,text='※10文字以内',font=("MSゴシック","12","bold"),bg='white',width=20, height=2)
    Setu4.place(x=200,y=350)
    
    #触れ合う言葉入力テキストボックス
    txt.place(x=245,y=410)

    #決定ボタン
    btnKettei=tk.Button(frame1,text='決定',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=HureauCheck)
    btnKettei.place(x=470,y=400)


    #,command=HureauCheck()
    #注意事項2
    labelTyui = tk.Label(frame1,text='※入力条件と一致しませんでした',font=("MSゴシック","10","bold"),fg=TyuiF,bg=TyuiH,width=30, height=1)
    labelTyui.place(x=177,y=450)

    #次のときのみラベルを見せるための受け渡し
    ukewatasi.setString('white','white')
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def HureauCheck():
    kotoba=txt.get()

    if len(kotoba)<11 and len(kotoba)>0:

        Seibutu.setHkotoba(kotoba)#言葉更新

        #テキストボックス
        txt.delete(0,tk.END)#中身を殻にしただけ
        txt.place(x=900,y=900)#移動して隠しただけ
        Hureau4_3()
                     
    else:
        #NameCheckのときのみラベルを見せるための受け渡し
        ukewatasi.setString('red','black')
        Hureau4_2()

def Hureau4_3():

    
    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    #キャンバス準備
    cvIkusei=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvIkusei.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvIkusei.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/SHukidasi.png", width=700, height=700)
    cvIkusei.create_image(50, 20, image=imgHukidasi, anchor=tk.NW)#イメージ表示
        
    Setu1 = tk.Label(frame1,text=Seibutu.HureauHenji(),font=("MSゴシック","20","bold"),bg='white',width=26, height=2)
    Setu1.place(x=120,y=90)

    #決定ボタン
    btnKettei=tk.Button(frame1,text='次へ',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=eventkime)
    btnKettei.place(x=500,y=167)

    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvIkusei.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示

    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvIkusei.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    #生物
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvIkusei.create_image(Seibutu.sx, Seibutu.sy, image=imgSkao, anchor=tk.NW)#イメージ表示

    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvIkusei.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示

    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvIkusei.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvIkusei.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示

    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def eventkime():#イベントするかしないか　決めて、次の画面へ移る

    #次のときのみラベルを見せるための受け渡し
    ukewatasi.setString('white','white')

    event=Tarn.setevent()

    if event==99 or (Seibutu.Nenrei<=4):

        TarnKirikae()#イベントなし
    
    elif event==1:

        eventHanasu1_1()#話しかけてくるイベント
        
    elif event==2:

        eventTabemono2_1()#食べ物をくれるイベント
        
        
    elif event==3:

        eventNomimono3_1()#飲み物をくれるイベント
        

def TarnKirikae():

    flag=Tarn.setTarn()

    if flag==True:
        Ikusei()

    else:#ゲームオーバー
        GameOver()

#話すイベント

def eventHanasu1_1():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    #キャンバス準備
    cvevent=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvevent.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvevent.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/SHukidasi.png", width=700, height=700)
    cvevent.create_image(50, 20, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    #生物が話す言葉保存
    seibutukotoba=Seibutu.HanasuEvent()

    Setu1 = tk.Label(frame1,text=seibutukotoba,font=("MSゴシック","20","bold"),bg='white',width=26, height=2)
    Setu1.place(x=120,y=90)

    #イベントラベル
    iventL = tk.Label(frame1,text='イベント発生',font=("MSゴシック","30","bold"),bg='yellow',width=12, height=1)
    iventL.place(x=200,y=5)

    #決定ボタン
    btnKettei=tk.Button(frame1,text='次へ',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=eventHanasu1_2)
    btnKettei.place(x=500,y=167)

    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    #生物
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgSkao, anchor=tk.NW)#イメージ表示

    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示

    #次のときのみラベルを見せるための受け渡し
    ukewatasi.setString('white','white')

    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示 

def eventHanasu1_2():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    TyuiH,TyuiF=ukewatasi.getString2()#NameCheckのときのみラベルを見せるための受け渡し
    #キャンバス準備
    cvevent=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvevent.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvevent.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvevent.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #話しかける時の吹き出し
    imgHanasikakeru = tk.PhotoImage(file="./img/Hanasikakeru.png", width=700, height=700)
    cvevent.create_image(50, 180, image=imgHanasikakeru, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text=Seibutu.getName(),font=("MSゴシック","14","bold"),fg=Seibutu.Iro,bg='white',width=10, height=2)
    Setu1.place(x=135,y=260)
    Setu2 = tk.Label(frame1,text=Seibutu.KunChan+'に',font=("MSゴシック","14","bold"),bg='white',width=10, height=2)
    Setu2.place(x=240,y=260)
    Setu3 = tk.Label(frame1,text='言葉を返してあげてください',font=("MSゴシック","14","bold"),bg='white',width=24, height=2)
    Setu3.place(x=145,y=300)
    Setu4 = tk.Label(frame1,text='※10文字以内',font=("MSゴシック","14","bold"),bg='white',width=20, height=2)
    Setu4.place(x=180,y=345)

    #言葉入力テキストボックス
    txt.place(x=245,y=410)
    #決定ボタン
    btnKettei=tk.Button(frame1,text='決定',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=eventHanasuKotobaCheck)
    btnKettei.place(x=470,y=402)

    #注意事項2
    labelTyui = tk.Label(frame1,text='※入力条件と一致しませんでした',font=("MSゴシック","10","bold"),fg=TyuiF,bg=TyuiH,width=30, height=1)
    labelTyui.place(x=177,y=450)

    #さっき生物が言った言葉吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/SHukidasiSmall.png", width=400, height=200)
    cvevent.create_image(15, 0, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    skotoba = tk.Label(frame1,text=Seibutu.Kotoba.kiokuSkotoba,font=("MSゴシック","15","bold"),bg='white',width=22, height=2)
    skotoba.place(x=75,y=50)

    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def eventHanasuKotobaCheck():

    kotoba=txt.get()

    if len(kotoba)<11 and len(kotoba)>0:

        Seibutu.seteventHanasuKotoba(kotoba)#へんじ保存
        #テキストボックス
        txt.delete(0,tk.END)#中身を殻にしただけ
        txt.place(x=900,y=900)#移動して隠しただけ
        TarnKirikae()
            
    else:
        #NameCheckのときのみラベルを見せるための受け渡し
        ukewatasi.setString('red','black')
        eventHanasu1_2()
        

def eventTabemono2_1():
    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    #キャンバス準備
    cvevent=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvevent.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvevent.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/Hukidasi.png", width=700, height=700)
    cvevent.create_image(50, 10, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text=Seibutu.getName(),font=("MSゴシック","18","bold"),bg='white',fg=Seibutu.Iro,width=10, height=2)
    Setu1.place(x=100,y=45)
    Setu2 = tk.Label(frame1,text=Seibutu.KunChan+'が、',font=("MSゴシック","18","bold"),bg='white',width=10, height=2)
    Setu2.place(x=275,y=45)

    Setu3 = tk.Label(frame1,text='あなたに',font=("MSゴシック","18","bold"),bg='white',width=8, height=2)
    Setu3.place(x=100,y=100)

    tabemono=Seibutu.getTabemono()
    Setu4 = tk.Label(frame1,text=tabemono,font=("MSゴシック","18","bold"),bg='LightCyan',width=len(tabemono)*2, height=2)
    Setu4.place(x=220,y=100)

    Setu5 = tk.Label(frame1,text='を、',font=("MSゴシック","20","bold"),bg='white',width=3, height=2)
    Setu5.place(x=220+len(tabemono)*35,y=100)

    Setu6 = tk.Label(frame1,text='あげるみたいです',font=("MSゴシック","17","bold"),bg='white',width=16, height=2)
    Setu6.place(x=100,y=170)

    #イベントラベル
    iventL = tk.Label(frame1,text='イベント発生',font=("MSゴシック","30","bold"),bg='yellow',width=12, height=1)
    iventL.place(x=200,y=5)

    #決定ボタン
    btnHaikei = tk.Label(frame1,text=' ',font=("MSゴシック","18","bold"),bg='PaleVioletRed1',width=6, height=2)
    btnHaikei.place(x=485,y=255)
    btnKettei=tk.Button(frame1,text='次へ',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=eventTabemono2_2)
    btnKettei.place(x=500,y=270)

    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    #生物
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgSkao, anchor=tk.NW)#イメージ表示

    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示

    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def eventTabemono2_2():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    #キャンバス準備
    cvevent=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvevent.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvevent.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/SHukidasi.png", width=700, height=700)
    cvevent.create_image(50, 20, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    #生物が話す言葉保存
    seibutukotoba=Seibutu.getTKotoba()

    Setu1 = tk.Label(frame1,text=seibutukotoba,font=("MSゴシック","20","bold"),bg='white',width=26, height=2)
    Setu1.place(x=120,y=90)

    #決定ボタン
    btnKettei=tk.Button(frame1,text='次へ',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=eventTabemono2_3)
    btnKettei.place(x=500,y=167)

    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    #生物
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgSkao, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示 

def eventTabemono2_3():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    TyuiH,TyuiF=ukewatasi.getString2()#NameCheckのときのみラベルを見せるための受け渡し
    #キャンバス準備
    cvevent=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvevent.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvevent.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #話しかける時の吹き出し
    imgHanasikakeru = tk.PhotoImage(file="./img/Hanasikakeru.png", width=700, height=700)
    cvevent.create_image(50, 180, image=imgHanasikakeru, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text='感謝の言葉を入力してください',font=("MSゴシック","14","bold"),bg='white',width=28, height=2)
    Setu1.place(x=120,y=270)
    Setu2 = tk.Label(frame1,text='※10文字以内',font=("MSゴシック","15","bold"),bg='white',width=20, height=2)
    Setu2.place(x=180,y=320)

    #言葉入力テキストボックス
    txt.place(x=245,y=410)
    #決定ボタン
    btnKettei=tk.Button(frame1,text='決定',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=eventTKotobaCheck)
    btnKettei.place(x=470,y=402)

    #注意事項2
    labelTyui = tk.Label(frame1,text='※入力条件と一致しませんでした',font=("MSゴシック","10","bold"),fg=TyuiF,bg=TyuiH,width=30, height=1)
    labelTyui.place(x=177,y=450)


    #次のときのみラベルを見せるための受け渡し
    ukewatasi.setString('white','white')
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def eventTKotobaCheck():
    kotoba=txt.get()
    if len(kotoba)<11 and len(kotoba)>0:
 
        Seibutu.seteventTArigatoKotoba(kotoba)#言葉保存
        #テキストボックス
        txt.delete(0,tk.END)#中身を殻にしただけ
        txt.place(x=900,y=900)#移動して隠しただけ
        TarnKirikae()
            
    else:
        #NameCheckのときのみラベルを見せるための受け渡し
        ukewatasi.setString('red','black')
        eventTabemono2_3()

def eventNomimono3_1():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

     #キャンバス準備
    cvevent=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvevent.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvevent.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/Hukidasi.png", width=700, height=700)
    cvevent.create_image(50, 10, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text=Seibutu.getName(),font=("MSゴシック","18","bold"),bg='white',fg=Seibutu.Iro,width=10, height=2)
    Setu1.place(x=100,y=45)
    Setu2 = tk.Label(frame1,text=Seibutu.KunChan+'が、',font=("MSゴシック","18","bold"),bg='white',width=10, height=2)
    Setu2.place(x=275,y=45)

    Setu3 = tk.Label(frame1,text='あなたに',font=("MSゴシック","18","bold"),bg='white',width=8, height=2)
    Setu3.place(x=100,y=100)

    nomimono=Seibutu.getNomimono()

    Setu4 = tk.Label(frame1,text=nomimono,font=("MSゴシック","18","bold"),bg='LightCyan',width=len(nomimono)*2, height=2)
    Setu4.place(x=220,y=100)
    Setu5 = tk.Label(frame1,text='を、',font=("MSゴシック","20","bold"),bg='white',width=3, height=2)
    Setu5.place(x=220+len(nomimono)*35,y=100)

    Setu6 = tk.Label(frame1,text='あげるみたいです',font=("MSゴシック","17","bold"),bg='white',width=16, height=2)
    Setu6.place(x=100,y=170)

    #決定ボタン
    btnHaikei = tk.Label(frame1,text=' ',font=("MSゴシック","18","bold"),bg='PaleVioletRed1',width=6, height=2)
    btnHaikei.place(x=485,y=255)
    btnKettei=tk.Button(frame1,text='次へ',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=eventNomimono2_2)
    btnKettei.place(x=500,y=270)

    #イベントラベル
    iventL = tk.Label(frame1,text='イベント発生',font=("MSゴシック","30","bold"),bg='yellow',width=12, height=1)
    iventL.place(x=200,y=5)

    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    #生物
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgSkao, anchor=tk.NW)#イメージ表示

    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示

    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def eventNomimono2_2():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    #キャンバス準備
    cvevent=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvevent.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvevent.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/SHukidasi.png", width=700, height=700)
    cvevent.create_image(50, 20, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    #生物が話す言葉保存
    seibutukotoba=Seibutu.getNKotoba()

    Setu1 = tk.Label(frame1,text=seibutukotoba,font=("MSゴシック","20","bold"),bg='white',width=26, height=2)
    Setu1.place(x=120,y=90)

    #決定ボタン
    btnKettei=tk.Button(frame1,text='次へ',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=eventNomimono2_3)
    btnKettei.place(x=500,y=167)

    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    #生物
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgSkao, anchor=tk.NW)#イメージ表示

    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvevent.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示 

def eventNomimono2_3():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[2].play()

    TyuiH,TyuiF=ukewatasi.getString2()#NameCheckのときのみラベルを見せるための受け渡し
    #キャンバス準備
    cvevent=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvevent.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvevent.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #話しかける時の吹き出し
    imgHanasikakeru = tk.PhotoImage(file="./img/Hanasikakeru.png", width=700, height=700)
    cvevent.create_image(50, 180, image=imgHanasikakeru, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text='感謝の言葉を入力してください',font=("MSゴシック","14","bold"),bg='white',width=28, height=2)
    Setu1.place(x=120,y=270)
    Setu2 = tk.Label(frame1,text='※10文字以内',font=("MSゴシック","15","bold"),bg='white',width=20, height=2)
    Setu2.place(x=180,y=320)

    #言葉入力テキストボックス
    txt.place(x=245,y=410)
    #決定ボタン
    btnKettei=tk.Button(frame1,text='決定',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=eventNKotobaCheck)
    btnKettei.place(x=470,y=402)

    #注意事項2
    labelTyui = tk.Label(frame1,text='※入力条件と一致しませんでした',font=("MSゴシック","10","bold"),fg=TyuiF,bg=TyuiH,width=30, height=1)
    labelTyui.place(x=177,y=450)


    #次のときのみラベルを見せるための受け渡し
    ukewatasi.setString('white','white')
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def eventNKotobaCheck():
    kotoba=txt.get()
    if len(kotoba)<11 and len(kotoba)>0:

        Seibutu.seteventNArigatoKotoba(kotoba)#言葉保存
        #テキストボックス
        txt.delete(0,tk.END)#中身を殻にしただけ
        txt.place(x=900,y=900)#移動して隠しただけ
        TarnKirikae()
            
    else:
        #NameCheckのときのみラベルを見せるための受け渡し
        ukewatasi.setString('red','black')
        eventNomimono2_3()


#クリックイベント判定処理(Ikusei画面より

def ClickSyori(event):
    print('x:'+str(event.x))
    print('y:'+str(event.y))
    x=event.x
    y=event.y

    if Seibutu.sx<=x and x<=Seibutu.endsx and Seibutu.sy<= y and y<=Seibutu.endsy:#生物クリックしたら

        SeibutuClick()
    elif 600<=x and x<=678 and 625<= y and y<=681:#セーブボタンクリックしたら
        DataHyouji()
    elif 11<=x and x<=76 and 628<=y and y<=688:#設定アイコンクリックしたら
        Settei()
    elif 133<=x and x<=200 and 626<=y and y<=691:#ホームアイコンクリックしたら
        TitleSentaku()

def SeibutuClick():#生物をクリックしたときの処理

    #生物クリックの音
    if sound.KoukaonOnOff==True:
        KoukaonSeibutu[0].play()

    #キャンバス準備
    cvSeibutuClick=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvSeibutuClick.place(x=0,y=0)

    #育成背景
    imgIkuseiHaikei = tk.PhotoImage(file="./img/IkuseiHaikei.png", width=700, height=700)
    cvSeibutuClick.create_image(0, 0, image=imgIkuseiHaikei, anchor=tk.NW)#イメージ表示

    #吹き出し
    imgHukidasi = tk.PhotoImage(file="./img/SHukidasi.png", width=700, height=700)
    cvSeibutuClick.create_image(50, 20, image=imgHukidasi, anchor=tk.NW)#イメージ表示

    Setu1 = tk.Label(frame1,text=Seibutu.SeibutuClickHenji(),font=("MSゴシック","20","bold"),bg='white',width=26, height=2)
    Setu1.place(x=120,y=90)

    #決定ボタン
    btnKettei=tk.Button(frame1,text='次へ',font=("MSゴシック","12","bold"),bg='white',width=5, height=1,command=Ikusei)
    btnKettei.place(x=500,y=167)

    if not Seibutu.gethand()=='a':#手
        imghand = tk.PhotoImage(file=Seibutu.gethand(), width=700, height=700)
        imghand =imghand.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvSeibutuClick.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imghand, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getfut()=='a':#足
        imgfut = tk.PhotoImage(file=Seibutu.getfut(), width=700, height=700)
        imgfut =imgfut.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvSeibutuClick.create_image(Seibutu.futhandx, Seibutu.futhandy, image=imgfut, anchor=tk.NW)#イメージ表示
    #生物
    imgSkao = tk.PhotoImage(file=Seibutu.getface(), width=700, height=700)
    imgSkao =imgSkao.subsample(Seibutu.size,Seibutu.size)#画像縮小
    cvSeibutuClick.create_image(Seibutu.sx, Seibutu.sy, image=imgSkao, anchor=tk.NW)#イメージ表示

    if not Seibutu.geteye()=='a':
        imgeye = tk.PhotoImage(file=Seibutu.geteye(), width=700, height=700)
        imgeye =imgeye.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvSeibutuClick.create_image(Seibutu.sx, Seibutu.sy, image=imgeye, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getnose()=='a':
        imgnose = tk.PhotoImage(file=Seibutu.getnose(), width=700, height=700)
        imgnose =imgnose.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvSeibutuClick.create_image(Seibutu.sx, Seibutu.sy, image=imgnose, anchor=tk.NW)#イメージ表示
    
    if not Seibutu.getmouth()=='a':
        imgmouth = tk.PhotoImage(file=Seibutu.getmouth(), width=700, height=700)
        imgmouth =imgmouth.subsample(Seibutu.size,Seibutu.size)#画像縮小
        cvSeibutuClick.create_image(Seibutu.sx, Seibutu.sy, image=imgmouth, anchor=tk.NW)#イメージ表示
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示 


#設定アイコンクリックしたときの処理
def Settei():

    sound.Save()

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[4].play()

    #キャンバス準備
    cvSettei=tk.Canvas(frame1,bg="white",height=700,width=700)
    #キャンバス表示
    cvSettei.place(x=0,y=0)

    #設定背景
    imgSetteiHaikei = tk.PhotoImage(file="./img/SetteiHaikei.png", width=700, height=700)
    cvSettei.create_image(0, 0, image=imgSetteiHaikei, anchor=tk.NW)#イメージ表示

    #ONOFF表示


    imgOn = tk.PhotoImage(file="./img/SetteiOn.png", width=700, height=700)
    imgOff = tk.PhotoImage(file="./img/SetteiOff.png", width=700, height=700)

    #BGM
    if sound.BGMOnOff==True:#BGMがONのとき
        cvSettei.create_image(231, 170, image=imgOn, anchor=tk.NW)#イメージ表示
    elif sound.BGMOnOff==False:#BGMがOFFのとき
        cvSettei.create_image(236, 167, image=imgOff, anchor=tk.NW)#イメージ表示

    #効果音
    if sound.KoukaonOnOff==True:#効果音がONのとき
        cvSettei.create_image(231, 420, image=imgOn, anchor=tk.NW)#イメージ表示
    elif sound.KoukaonOnOff==False:#効果音がOFFのとき
        cvSettei.create_image(236, 417, image=imgOff, anchor=tk.NW)#イメージ表示

    #設定完了ボ
    btnSetteikanryou=tk.Button(frame1,text='おっけー',font=("MSゴシック","18","bold"),bg='LightSalmon',width=7, height=1,command=AfterSetteiSyori)
    btnSetteikanryou.place(x=40,y=620)

    #クリックしたらクリックイベント判定処理へ
    cvSettei.bind('<ButtonPress-1>',SetteiGamenClickSyori)

    root.mainloop()



#設定画面でクリックイベント判定
def SetteiGamenClickSyori(event):
    print('x:'+str(event.x))
    print('y:'+str(event.y))
    x=event.x
    y=event.y

    if 244<=x and x<=402 and 314<=y and y<=371:#BGM音量を大きく

        #音量調節
        hantei=sound.BGMbig()

        if hantei==True:
            pygame.mixer.music.set_volume(sound.getBGMvol())#0.0~1.0
            print('音量'+str(sound.getBGMvol)+'に設定')
        else:
            messagebox.showinfo('エラー',message='最大音量のため、これ以上音量を上げられません')#ポップアップ表示

    elif 453<=x and x<=612 and 308<=y and y<=357:#BGM音量を小さく

        #音量調節
        hantei=sound.BGMsmall()

        if hantei==True:
            pygame.mixer.music.set_volume(sound.getBGMvol())#0.0~1.0
            print('音量'+str(sound.getBGMvol)+'に設定')
        else:
            messagebox.showinfo('エラー',message='最小音量のため、これ以上音量を下げられません')#ポップアップ表示
    
    elif 250<=x and x<=366 and 204<=y and y<=265:#BBGM　ONクリック

        if sound.BGMon()==True:
            #音楽ファイルの読み込み
            pygame.mixer.music.load(ukewatasi.getString1())#Title()からの設定か、Ikusei()からの設定なのかで、音楽ファイル違う
            ukewatasi.setString1("./sound/Opening.wav")#またOFFにしてONになる時対策(getしたら初期化するようにしているから。)
            #音量調節
            pygame.mixer.music.set_volume(sound.getBGMvol())#0.0~1.0
            #音楽の再生回数（無限）
            pygame.mixer.music.play(-1)

        print('BGMOnOff状態')
        print(sound.BGMOnOff)

    elif 420<=x and x<=562 and 193<=y and y<=260:#BBGM　OFFクリック
        if sound.BGMoff()==True:
            pygame.mixer.music.stop()
        print('BGMOnOff状態')
        print(sound.BGMOnOff)
    
    elif 249<=x and x<=373 and 455<=y and y<=518:#効果音 ONクリック

        if sound.Koukaonon()==True:
            a=0
        print('KoukaonOnOff状態')
        print(sound.KoukaonOnOff)
        
    
    elif 418<=x and x<=564 and 444<=y and y<=512:#効果音　OFFクリック

        if sound.Koukaonoff()==True:
            a=0
        print('KoukaonOnOff状態')
        print(sound.KoukaonOnOff)

    Settei()

def AfterSetteiSyori():

    #Title()から設定を押した:0
    #Ikusei()空設定を押した:1
    if 1==ukewatasi.getint():
        #ボタン押した音
        if sound.KoukaonOnOff==True:
            KoukaonKihon[2].play()
        Title()
    else:
        Ikusei()

        




#ゲームオーバーの処理
def GameOver():

    t1 = time.time() 
    label = tk.Label(frame1, image=GameOverGif)
    
    label.place(x=0,y=0)
    label.bind('<ButtonPress-1>',ClickSyori)
    name = tk.Label(frame1,text=Seibutu.getName(),font=("MSゴシック","15","bold"),bg='yellow2',width=9, height=1)
    name.place(x=289,y=582)


    if sound.BGMOnOff==True:
        #音楽ファイルの読み込み
        pygame.mixer.music.load("./sound/Died.wav")
        #音量調節
        pygame.mixer.music.set_volume(0.8)#0.0~1.0

        #音楽の再生回数（1）
        pygame.mixer.music.play(1)
    
    root.after_idle(GameOverGifAnime)

    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()#表示

def GameOverGifAnime():
        global GameOver_index
        try:
            # XXX: 次のフレームに移る
            GameOverGif.configure(format="gif -index {}".format(GameOver_index))

            GameOver_index += 1
        except tk.TclError:
            GameOver_index = 0
            return GameOverGifAnime()
        else:
            
            if GameOver_index<=29:#10秒たったらストップ
                root.after(0, GameOverGifAnime) # XXX: アニメーション速度が固定多ければ多いほど遅い
            else:

                #不気味な鳥の鳴き声
                if sound.KoukaonOnOff==True:
                    KoukaonKihon[6].play()

                #キャンバス準備
                cvIkusei=tk.Canvas(frame1,bg="white",height=700,width=700)
                #キャンバス表示
                cvIkusei.place(x=0,y=0)

                #イメージ作成
                imgGameOver = tk.PhotoImage(file="./img/GameOver/GameOver_38.png", width=700, height=700)
                #imgHaikei =imgHaikei.zoom(2,2)#画像拡大
                cvIkusei.create_image(0, 0, image=imgGameOver, anchor=tk.NW)#イメージ表示

                name = tk.Label(frame1,text=Seibutu.getName(),font=("MSゴシック","15","bold"),bg='yellow2',width=9, height=1)
                name.place(x=289,y=582)                

                btn=tk.Button(frame1,text='次へ',font=("MSゴシック","20","bold"),bg='firebrick1',width=5, height=1,command=Isyo)
                btn.place(x=290,y=350)
                root.protocol("WM_DELETE_WINDOW",close)
                root.mainloop()#表示

def Isyo():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[4].play()

    #キャンバス準備
    cvIsyo=tk.Canvas(frame1,bg="dark slate blue",height=700,width=700)
    #キャンバス表示
    cvIsyo.place(x=0,y=0)

    #背景
    imgPaper = tk.PhotoImage(file="./img/Paper.png", width=700, height=700)
    cvIsyo.create_image(10, 0, image=imgPaper, anchor=tk.NW)#イメージ表示

    #遺書の内容
    Isyo = tk.Label(frame1,text='いしょ',font=("MSゴシック","30","bold"),bg='white',width=7, height=1)
    Isyo.place(x=240,y=60)
    bun1 = tk.Label(frame1,text='おかあさんへ',font=("MSゴシック","18","bold"),bg='white',width=12, height=1)
    bun1.place(x=180,y=150)
    BokuWatasi=Seibutu.getBokuWatasi()
    bun2 = tk.Label(frame1,text=BokuWatasi+'は、',font=("MSゴシック","15","bold"),bg='white',width=len(BokuWatasi)*2+2, height=1)
    bun2.place(x=170,y=200)
    Naiyo=Tarn.GameOverNaiyo
    bun3 = tk.Label(frame1,text=Naiyo,font=("MSゴシック","15","bold"),bg=Tarn.GameOverColor,width=len(Naiyo)*2, height=1)
    bun3.place(x=170+(len(BokuWatasi)*2+2)*12,y=200)
    bun4 = tk.Label(frame1,text='で、そろそろ　しにます',font=("MSゴシック","15","bold"),bg='white',width=22, height=1)
    bun4.place(x=170,y=250)
    bun5 = tk.Label(frame1,text='みじかいあいだだったけど、',font=("MSゴシック","15","bold"),bg='white',width=24, height=1)
    bun5.place(x=170,y=300)
    bun6 = tk.Label(frame1,text='そだててくれてありがとう',font=("MSゴシック","15","bold"),bg='white',width=24, height=1)
    bun6.place(x=170,y=350)
    bun7 = tk.Label(frame1,text=Seibutu.getName()+' より',font=("MSゴシック","18","bold"),bg='white',width=len(Seibutu.getName())*2+5, height=1)
    bun7.place(x=470-(len(Seibutu.getName())*2+5)*28+170,y=400)
    

    #タイトルへボタン
    btnSetteikanryou=tk.Button(frame1,text='タイトルへ',font=("MSゴシック","18","bold"),bg='firebrick1',width=12, height=1,command=BeforeTitle)
    btnSetteikanryou.place(x=230,y=500)
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()

def BeforeTitle():

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[5].play()
    TitleJunbi()



def DataHyouji():#データ表示画面

    mode=0

    if 1==ukewatasi.getint():#Title画面より
        ukewatasi.setint(1)
        mode=1

    else:#Ikusei画面より
        ukewatasi.setint(0)
        mode=0


    #ろーどできいるふぁいるの数、どれなのか　調べる

    Datahairetu=dat.getDatahairetu()#load可能ならTrue　だめならFalse
    print(Datahairetu)

    #ボタン押した音
    if sound.KoukaonOnOff==True:
        KoukaonKihon[4].play()

    #キャンバス準備
    cvload=tk.Canvas(frame1,bg="deep sky blue",height=700,width=700)
    #キャンバス表示
    cvload.place(x=0,y=0)

    #データ１
    imgdata1 = tk.PhotoImage(file="./img/dataHukidasi.png", width=700, height=700)
    cvload.create_image(50, 25, image=imgdata1, anchor=tk.NW)#イメージ表示

    data1 = tk.Label(frame1,text='ファイル1',font=("MSゴシック","18","bold"),bg='navajo white',width=10, height=1)
    data1.place(x=95,y=50)

    if Datahairetu[0]==True:#data1　loadできるなら

        nitizi,johoHairetu,kaoHairetu,futhandxy=dat.getDataJoho(1)

        #セーブした時間表示
        nitizi1 = tk.Label(frame1,text=nitizi,font=("MSゴシック","18","bold"),bg='white',width=16, height=1)
        nitizi1.place(x=255,y=50)

        #名前、性別、年齢表示
        name1 = tk.Label(frame1,text=johoHairetu[0],font=("MSゴシック","18","bold"),bg='white',width=10, height=1)
        name1.place(x=90,y=110)
        danjo1 = tk.Label(frame1,text=johoHairetu[1],font=("MSゴシック","18","bold"),bg='white',width=5, height=1)
        danjo1.place(x=250,y=110)
        nenrei1 = tk.Label(frame1,text=johoHairetu[2]+'才',font=("MSゴシック","18","bold"),bg='white',width=7, height=1)
        nenrei1.place(x=335,y=110)

        #生物の顔を表示
        if not kaoHairetu[0]=='a':#手
            imghand1 = tk.PhotoImage(file=kaoHairetu[0], width=700, height=700)
            imghand1 =imghand1.subsample(2,2)#画像縮小
            cvload.create_image(futhandxy[0]+320, futhandxy[1]-245, image=imghand1, anchor=tk.NW)#イメージ表示
    
        if not kaoHairetu[1]=='a':#足
            imgfut1 = tk.PhotoImage(file=kaoHairetu[1], width=700, height=700)
            imgfut1 =imgfut1.subsample(2,2)#画像縮小
            cvload.create_image(futhandxy[0]+320, futhandxy[1]-245, image=imgfut1, anchor=tk.NW)#イメージ表示
        #生物
        imgSkao1 = tk.PhotoImage(file=kaoHairetu[2], width=700, height=700)
        imgSkao1 =imgSkao1.subsample(2,2)#画像縮小
        cvload.create_image(470, 70, image=imgSkao1, anchor=tk.NW)#イメージ表示

        if not kaoHairetu[3]=='a':
            imgeye1 = tk.PhotoImage(file=kaoHairetu[3], width=700, height=700)
            imgeye1 =imgeye1.subsample(2,2)#画像縮小
            cvload.create_image(470, 70, image=imgeye1, anchor=tk.NW)#イメージ表示
        
        if not kaoHairetu[4]=='a':
            imgnose1 = tk.PhotoImage(file=kaoHairetu[4], width=700, height=700)
            imgnose1 =imgnose1.subsample(2,2)#画像縮小
            cvload.create_image(470, 70, image=imgnose1, anchor=tk.NW)#イメージ表示
        
        if not kaoHairetu[5]=='a':
            imgmouth1 = tk.PhotoImage(file=kaoHairetu[5], width=700, height=700)
            imgmouth1 =imgmouth1.subsample(2,2)#画像縮小
            cvload.create_image(470, 70, image=imgmouth1, anchor=tk.NW)#イメージ表示
        
        #削除ボタン
        btnKesu1=tk.Button(frame1,text='削除',font=("MSゴシック","16","bold"),bg='tomato2',width=3, height=1,command=dataSakujo1)
        btnKesu1.place(x=615,y=160)

    else:#dataなかったら
        nodata1 = tk.Label(frame1,text='データがありません',font=("MSゴシック","21","bold"),bg='white',width=18, height=1)   
        nodata1.place(x=190,y=100)
    
    if mode==0 or  Datahairetu[0]==True:#Ikusei画面から　か、　ロード可能だったら
        #決定ボタン
        btnKettei1=tk.Button(frame1,text='決定',font=("MSゴシック","18","bold"),bg='tan1',width=23, height=1,command=databtn1)
        btnKettei1.place(x=95,y=155)


    #データ２
    imgdata2 = tk.PhotoImage(file="./img/dataHukidasi.png", width=700, height=700)
    cvload.create_image(50, 225, image=imgdata2, anchor=tk.NW)#イメージ表示

    data2 = tk.Label(frame1,text='ファイル2',font=("MSゴシック","18","bold"),bg='lavender',width=10, height=1)
    data2.place(x=95,y=250)

    if Datahairetu[1]==True:#data2　loadできるなら

        nitizi,johoHairetu,kaoHairetu,futhandxy=dat.getDataJoho(2)

        #セーブした時間表示
        nitizi2 = tk.Label(frame1,text=nitizi,font=("MSゴシック","18","bold"),bg='white',width=16, height=1)
        nitizi2.place(x=255,y=250)

        #名前、性別、年齢表示
        name2 = tk.Label(frame1,text=johoHairetu[0],font=("MSゴシック","18","bold"),bg='white',width=10, height=1)
        name2.place(x=90,y=310)
        danjo2 = tk.Label(frame1,text=johoHairetu[1],font=("MSゴシック","18","bold"),bg='white',width=5, height=1)
        danjo2.place(x=250,y=310)
        nenrei2 = tk.Label(frame1,text=johoHairetu[2]+'才',font=("MSゴシック","18","bold"),bg='white',width=7, height=1)
        nenrei2.place(x=335,y=310)

        #生物の顔を表示
        if not kaoHairetu[0]=='a':#手
            imghand2 = tk.PhotoImage(file=kaoHairetu[0], width=700, height=700)
            imghand2 =imghand2.subsample(2,2)#画像縮小
            cvload.create_image(futhandxy[0]+320, futhandxy[1]-45, image=imghand2, anchor=tk.NW)#イメージ表示
    
        if not kaoHairetu[1]=='a':#足
            imgfut2 = tk.PhotoImage(file=kaoHairetu[1], width=700, height=700)
            imgfut2 =imgfut2.subsample(2,2)#画像縮小
            cvload.create_image(futhandxy[0]+320, futhandxy[1]-445, image=imgfut2, anchor=tk.NW)#イメージ表示
        #生物
        imgSkao2 = tk.PhotoImage(file=kaoHairetu[2], width=700, height=700)
        imgSkao2 =imgSkao2.subsample(2,2)#画像縮小
        cvload.create_image(470, 270, image=imgSkao2, anchor=tk.NW)#イメージ表示

        if not kaoHairetu[3]=='a':
            imgeye2 = tk.PhotoImage(file=kaoHairetu[3], width=700, height=700)
            imgeye2 =imgeye2.subsample(2,2)#画像縮小
            cvload.create_image(470, 270, image=imgeye2, anchor=tk.NW)#イメージ表示
        
        if not kaoHairetu[4]=='a':
            imgnose2 = tk.PhotoImage(file=kaoHairetu[4], width=700, height=700)
            imgnose2 =imgnose2.subsample(2,2)#画像縮小
            cvload.create_image(470, 270, image=imgnose2, anchor=tk.NW)#イメージ表示
        
        if not kaoHairetu[5]=='a':
            imgmouth2 = tk.PhotoImage(file=kaoHairetu[5], width=700, height=700)
            imgmouth2 =imgmouth2.subsample(2,2)#画像縮小
            cvload.create_image(470, 270, image=imgmouth2, anchor=tk.NW)#イメージ表示
        
        #削除ボタン
        btnKesu2=tk.Button(frame1,text='削除',font=("MSゴシック","16","bold"),bg='MediumOrchid2',width=3, height=1,command=dataSakujo2)
        btnKesu2.place(x=615,y=365)


    else:#dataなかったら

        nodata2 = tk.Label(frame1,text='データがありません',font=("MSゴシック","21","bold"),bg='white',width=18, height=1)
        nodata2.place(x=190,y=300)
    
    if mode==0 or  Datahairetu[1]==True:#Ikusei画面から　か、　ロード可能だったら
        #決定ボタン
        btnKettei2=tk.Button(frame1,text='決定',font=("MSゴシック","18","bold"),bg='MediumPurple1',width=23, height=1,command=databtn2)
        btnKettei2.place(x=95,y=355)

    #データ３
    imgdata3 = tk.PhotoImage(file="./img/dataHukidasi.png", width=700, height=700)
    cvload.create_image(50, 430, image=imgdata3, anchor=tk.NW)#イメージ表示

    data3 = tk.Label(frame1,text='ファイル3',font=("MSゴシック","18","bold"),bg='LightPink1',width=10, height=1)
    data3.place(x=95,y=455)

    if Datahairetu[2]==True:#data3　loadできるなら

        nitizi,johoHairetu,kaoHairetu,futhandxy=dat.getDataJoho(3)

        #セーブした時間表示
        nitizi3 = tk.Label(frame1,text=nitizi,font=("MSゴシック","18","bold"),bg='white',width=16, height=1)
        nitizi3.place(x=255,y=455)

        #名前、性別、年齢表示
        name3 = tk.Label(frame1,text=johoHairetu[0],font=("MSゴシック","18","bold"),bg='white',width=10, height=1)
        name3.place(x=90,y=515)
        danjo3 = tk.Label(frame1,text=johoHairetu[1],font=("MSゴシック","18","bold"),bg='white',width=5, height=1)
        danjo3.place(x=250,y=515)
        nenrei3 = tk.Label(frame1,text=johoHairetu[2]+'才',font=("MSゴシック","18","bold"),bg='white',width=7, height=1)
        nenrei3.place(x=335,y=515)

        #生物の顔を表示
        if not kaoHairetu[0]=='a':#手
            imghand3 = tk.PhotoImage(file=kaoHairetu[0], width=700, height=700)
            imghand3 =imghand3.subsample(2,2)#画像縮小
            cvload.create_image(futhandxy[0]+320, futhandxy[1]+160, image=imghand3, anchor=tk.NW)#イメージ表示
    
        if not kaoHairetu[1]=='a':#足
            imgfut3 = tk.PhotoImage(file=kaoHairetu[1], width=700, height=700)
            imgfut3 =imgfut3.subsample(2,2)#画像縮小
            cvload.create_image(futhandxy[0]+320, futhandxy[1]+160, image=imgfut3, anchor=tk.NW)#イメージ表示
        #生物
        imgSkao3 = tk.PhotoImage(file=kaoHairetu[2], width=700, height=700)
        imgSkao3 =imgSkao3.subsample(2,2)#画像縮小
        cvload.create_image(470, 475, image=imgSkao3, anchor=tk.NW)#イメージ表示

        if not kaoHairetu[3]=='a':
            imgeye3 = tk.PhotoImage(file=kaoHairetu[3], width=700, height=700)
            imgeye3 =imgeye3.subsample(2,2)#画像縮小
            cvload.create_image(470, 475, image=imgeye3, anchor=tk.NW)#イメージ表示
        
        if not kaoHairetu[4]=='a':
            imgnose3 = tk.PhotoImage(file=kaoHairetu[4], width=700, height=700)
            imgnose3 =imgnose3.subsample(2,2)#画像縮小
            cvload.create_image(470, 475, image=imgnose3, anchor=tk.NW)#イメージ表示
        
        if not kaoHairetu[5]=='a':
            imgmouth3 = tk.PhotoImage(file=kaoHairetu[5], width=700, height=700)
            imgmouth3 =imgmouth3.subsample(2,2)#画像縮小
            cvload.create_image(470, 475, image=imgmouth3, anchor=tk.NW)#イメージ表示
        
        #削除ボタン
        btnKesu3=tk.Button(frame1,text='削除',font=("MSゴシック","16","bold"),bg='VioletRed1',width=3, height=1,command=dataSakujo3)
        btnKesu3.place(x=615,y=565)
        

    else:#dataなかったら

        nodata3 = tk.Label(frame1,text='データがありません',font=("MSゴシック","21","bold"),bg='white',width=18, height=1)
        nodata3.place(x=190,y=505)
    
    if mode==0 or  Datahairetu[2]==True:#Ikusei画面から　か、　ロード可能だったら
        #決定ボタン
        btnKettei3=tk.Button(frame1,text='決定',font=("MSゴシック","18","bold"),bg='PaleVioletRed1',width=23, height=1,command=databtn3)
        btnKettei3.place(x=95,y=560)
    
    #戻るボタン
    btnmodoru=tk.Button(frame1,text='戻る',font=("MSゴシック","18","bold"),bg='LightGoldenrod1',width=6, height=1,command=DataHyoujiModoruButoon)
    btnmodoru.place(x=15,y=640)

    if mode==0:
        #Homeアイコン画像
        #イメージ作成
        imgHome = tk.PhotoImage(file="./img/HomeIcon.png", width=500, height=500)
        #imgHaikei =imgHaikei.zoom(2,2)#画像拡大
        cvload.create_image(130, 620, image=imgHome, anchor=tk.NW)#イメージ表示

    cvload.bind('<ButtonPress-1>',DataHyoujiClickSyori)
    root.protocol("WM_DELETE_WINDOW",close)
    root.mainloop()

def DataHyoujiModoruButoon():

    if 1==ukewatasi.getint():#つづきから

        #ボタン押した音
        if sound.KoukaonOnOff==True:
            KoukaonKihon[2].play()
        
        Title()

    else:#セーブボタン

        Ikusei()

def databtn1():

    DataHyoujiSyori(1)

def databtn2():

    DataHyoujiSyori(2)

def databtn3():

    DataHyoujiSyori(3)

def dataSakujo1():

    DataSakujoSyori(1)

def dataSakujo2():

    DataSakujoSyori(2)
def dataSakujo3():

    DataSakujoSyori(3)



def DataHyoujiClickSyori(event):

    print('x:'+str(event.x))
    print('y:'+str(event.y))
    x=event.x
    y=event.y
    if 133<=x and x<=200 and 626<=y and y<=691:#ホームアイコンクリックしたら
        TitleSentaku()

def DataHyoujiSyori(code):
   
    if 1==ukewatasi.getint():#つづきから
        
        lod.load(code)
        TudukiKaisiJunbi()

    else:#セーブボタン

        sav.save(code)

        #ボタン押した音
        if sound.KoukaonOnOff==True:
            KoukaonKihon[3].play()

        message=messagebox.askyesno('セーブ','セーブ完了しました！\nタイトル画面へ戻りますか？')

        if message ==True:#戻る　だったら
            BeforeTitle()
        
        
        DataHyouji()#画面読み込み'''

def DataSakujoSyori(code):

    #だいあろぐぼっくす
    #削除
    cre.crea(code)

    DataHyouji()


def TudukiKaisiJunbi():

    if sound.BGMOnOff==True:

        #BGM準備

        #音楽ファイルの読み込み
        pygame.mixer.music.load("./sound/BGM.wav")
        #音量調節
        pygame.mixer.music.set_volume(sound.getBGMvol())#0.0~1.0
        #音楽の再生回数（無限）
        pygame.mixer.music.play(-1)

    Ikusei()



def syokika():

    Seibutu.syokika()
    Tarn.syokika()

def TitleSentaku():

    message=messagebox.askyesno('Titleへ','タイトル画面へ戻りますか？')

    if message ==True:#戻る　だったら
        BeforeTitle()



                



#GetName()
with ThreadPoolExecutor() as Thread1:

    features=[Thread1.submit(TitleJunbi),Thread1.submit(BGM)]

    root.mainloop()#表示


    #for feature in features:
        #feature.result()
#Title()










