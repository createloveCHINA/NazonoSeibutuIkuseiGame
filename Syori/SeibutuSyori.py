import Syori.KotobaKanri
import Syori.SonotaSyori.HairetuCheck
import random

import Syori.OsewaSyori.Hanasikakeru
import Syori.OsewaSyori.Tabesaseru
import Syori.OsewaSyori.Nomaseru
import Syori.OsewaSyori.Hureau
import Syori.OsewaSyori.Kaiwasuru

import Syori.EventSyori.Event


class SeibutuSyori():

    Kotoba = Syori.KotobaKanri.KotobaKanri()
    hairetuck=Syori.SonotaSyori.HairetuCheck.HairetuCheck()

    hanasi=Syori.OsewaSyori.Hanasikakeru.Hanasikakeru(Kotoba)
    tabesa=Syori.OsewaSyori.Tabesaseru.Tabesaseru(Kotoba)
    nomase=Syori.OsewaSyori.Nomaseru.Nomaseru(Kotoba)
    hureau=Syori.OsewaSyori.Hureau.Hureau(Kotoba)
    kaiwa=Syori.OsewaSyori.Kaiwasuru.Kaiwasuru(Kotoba)
    
    even=Syori.EventSyori.Event.Event(Kotoba)

    #Tarn=STarn.STarn()

    Danjo=''#メスカオス化
    Iro=''  #メスは赤、オスは青
    KunChan=''#くんちゃん
    Name=''

    #size=1#縮小拡大
    #sx=245
    #sy=320
    
    

    size=2#縮小拡大
    #生物の顔の座標
    sx=305
    sy=410
    endsx=400
    endsy=502
    #足と手があるとき 足が高いとsy=190 低いとsy=255 sx60はそのまま
    #手足、羽などの座標
    # #足と手があるとき 足が高いとsy=170 低いとsy=235 sx60はそのまま
    
    futhandx=60
    futhandy=170

    #fut,hand　xは60 futが高いときは170 低いときは235

    face='a'
    eye='a'
    nose='a'
    mouth='a'
    fut='a'
    hand='a'

    Nenrei=int(0)
    Seikaku='???'
    SeikakuCode=0
    SukiTabemono='???'
    SukiNomimono='???'
    Manpukudo=int(3)
    Uruoido=int(3)

    count=0
    gakusyuPoint=0#学習ポイント
    aijoPoint=20 #愛情ポイント

    gakusyuPointMokuhyou=[5,10,35,45,55,75,85,100,115,130,150]

    kioku='a'#キャッシュ
    Skotoba='a'
    kiokuKotoba='a'
    

    def setDanjo(self,num):

        if num==0:#男
            self.Danjo='オス♂'
            self.KunChan='くん'
            self.Iro='blue'
        else:
            self.Danjo='メス♀'
            self.KunChan='ちゃん'
            self.Iro='firebrick1'
    
    def nenreibetuSetSeibutu(self):

        if self.Nenrei==2:

            self.seteye()#目あるかなしか設定

        elif self.Nenrei==4:

            self.setnose()
            
            self.setmouth()
        
        elif self.Nenrei==6:

            self.size=1 #サイズが大きくなる
            self.sx=245
            self.sy=320

        elif self.Nenrei==8:

            self.sethand()
        
        elif self.Nenrei==11:

            self.setfut()
            

    def setface(self):#顔の形と色のパス

        num1=random.randint(1,2)

        num1=random.randint(1,7)
        num2=random.randint(1,15)
        self.face='./Skao/face/Skao_'+str(num1)+'/Skao_'+str(num1)+'_'+str(num2)+'.png'
    
    def seteye(self):#目の設定

        num1=random.randint(1,28)
        self.eye='./Skao/eye/eye_'+str(num1)+'.png'

    def setnose(self):

        #鼻あるかなしかをランダムに決める
        num1=random.randint(1,100)#確率60%

        if num1>20:#鼻ありのとき鼻設定
            num1=random.randint(1,17)
            self.nose='./Skao/nose/nose_'+str(num1)+'.png'

    def setmouth(self):

        #口設定
        num1=random.randint(1,22)
        self.mouth='./Skao/mouth/mouth_'+str(num1)+'.png'
    
    def sethand(self):
        
        self.futhandy=310
        num=random.randint(1,16)
        self.hand='./Skao/hand/hand_'+str(num)+'.png'

    def setfut(self):

        num=random.randint(1,13)
        self.fut='./Skao/fut/fut_'+str(num)+'.png'

        if num==9 or num==10 or num==11 or num==13:

            self.futhandy=235#足が小さい生物は低くする

            self.sy=255#生物も一緒にずらす
        else:
            self.sy=290#生物も一緒にずらす 190

    
            
        
    def getface(self):
        return self.face
    
    def geteye(self):
        return self.eye
    
    def getnose(self):
        return self.nose

    def getmouth(self):
        return self.mouth
    
    def getfut(self):
        return self.fut

    def gethand(self):
        return self.hand

    def setName(self,name):
        self.Name=name
    
    def getName(self):
        return self.Name
    
    def getDanjo(self):

        return self.Danjo

    def getBokuWatasi(self):

        if self.Danjo=='オス♂':
            return 'ぼく'
        else:
            return 'わたし'
    
    def getNenrei(self):

        return self.Nenrei
    
    def getFutHandxy(self):

        return self.futhandx,self.futhandy
    
    def getManpukudo(self):

        return self.Manpukudo
    
    def getUruoido(self):

        return self.Uruoido

    
    def SeikakuKousin(self):#生物の性格を更新する

        usiro=len(self.gakusyuPointMokuhyou)-1

        if usiro>=self.Nenrei:

            tyuou=int((self.gakusyuPointMokuhyou[self.Nenrei]+self.gakusyuPointMokuhyou[self.Nenrei-1])/2)
        else:
            ima=self.gakusyuPointMokuhyou[usiro]+(self.Nenrei-usiro)*25
            mae=self.gakusyuPointMokuhyou[usiro]+(self.Nenrei-usiro-1)*25
            tyuou=int((mae+ima)/2)

        if self.aijoPoint>=70:

            self.Seikaku='わがまま'
            self.SeikakuCode=7

        elif self.aijoPoint>=50:

            if self.gakusyuPoint>tyuou:

                self.Seikaku='ヒーロー'
                self.SeikakuCode=6

            else:

                self.Seikaku='やさしい'
                self.SeikakuCode=5

        elif self.aijoPoint>=20:

            if self.gakusyuPoint>tyuou:

                self.Seikaku='かしこい'
                self.SeikakuCode=4

            else:
                self.Seikaku='てんねん'
                self.SeikakuCode=3

        elif self.aijoPoint>=10:

            if self.gakusyuPoint>tyuou:

                self.Seikaku='ずるがしこい'
                self.SeikakuCode=2

            else:
                self.Seikaku='いじわる'
                self.SeikakuCode=1

        elif self.aijoPoint<=10:

            self.Seikaku='サイコパス'
            self.SeikakuCode=0
        


    #お世話処理

    #話しかける処理

    def setKotoba(self,kotoba):#話しかけるときに言う言葉更新

        #キャッシュ保存
        self.kiokuKotoba=kotoba
               
        #学習ポイント+setKotoba処理
        self.gakusyuPoint+=self.hanasi.setKotoba(kotoba)

    def HanasikakeruHenji(self):#話しかけたとき生物の返事　返す

        #キャッシュ保存
        self.Skotoba=self.hanasi.HanasikakeruHenji(self.Nenrei)


        return self.Skotoba

    def HenjiHanteiSyori(self,radio):

        self.Kotoba.HenjiHanteiSyori(radio) 
    
    #会話処理

    def KaiwaGetCount(self):#会話の連続回数取得

        return self.kaiwa.getcount()

    def KaiwaSetCount(self):#会話の連続数＋１

        self.kaiwa.setcount()

    def KaiwaSyuryo(self):

        self.kaiwa.syuryo() 

    def setKaiwaKotoba(self,kotoba):#新しい言葉として保存&返信する言葉として保存

        #キャッシュ保存
        self.kiokuKotoba=kotoba
        self.test()
        #会話の言葉保存処理
        self.gakusyuPoint+=self.kaiwa.setKaiwaKotoba(kotoba)#言葉保存 

    def KaiwaHenji(self):#話しかけたとき生物の返事　返す

        #キャッシュ保存
        self.Skotoba=self.kaiwa.KaiwaHenji(self.Nenrei)


        return self.Skotoba    
    
    #食べ物処理 

    def setTabemono(self,tabemono):

        #キャッシュ保存
        self.kioku=tabemono
        
        #まんぷく度更新

        manpukudo=self.tabesa.setTabemono(tabemono)

        if manpukudo+self.Manpukudo<10:
            self.Manpukudo +=manpukudo
        else:
            self.Manpukudo=10

        #SukiTabemono更新
        self.SukiTabemono=self.tabesa.getSukiTabemono()

    def setTKotoba(self,kotoba):#食べさせる時に言う言葉更新
        
        #キャッシュ
        self.kiokuKotoba=kotoba
        
        #食べさせる言葉処理
        self.tabesa.setTKotoba(kotoba)
        
        #学習ポイント
        self.gakusyuPoint+=2

    def TabesaseruHenji(self):#話しかけたとき生物の返事　返す

        return self.tabesa.TabesaseruHenji(self.Nenrei)     
    
    #飲ませる

    def setNomimono(self,nomimono):#飲み物処理

        #キャッシュ保存
        self.kioku=nomimono

        #うるおい度更新

        uruoido=self.nomase.setNomimono(nomimono)

        if uruoido+self.Uruoido<10:
            self.Uruoido +=uruoido
        else:
            self.Uruoido=10

        #SukiNomimono更新
        self.SukiNomimono=self.nomase.getSukiNomimono() 

    def setNKotoba(self,kotoba):#飲ませる時に言う言葉更新

        #キャッシュ
        self.kiokuKotoba=kotoba
        
        #飲ませる言葉処理
        self.nomase.setNKotoba(kotoba)
        
        #学習ポイント
        self.gakusyuPoint+=2
    
    def NomaesruHenji(self):#話しかけたとき生物の返事　返す

        return self.nomase.NomaseruHenji(self.Nenrei) 

    #ふれあう処理
    
    def setAijou(self,num):#愛情ポイント更新

        #キャッシュ
        self.hureau.setima(num)

        #愛情ポイント更新

        self.aijoPoint+=self.hureau.getPoint()

        return self.hureau.getNaiyou()

    def setHkotoba(self,kotoba):#ふれあう時に言う言葉更新

        #キャッシュ保存
        self.kiokuKotoba=kotoba
        
        #ふれあう言葉更新
        self.hureau.setHKotoba(kotoba)       
            
        #学習ポイント
        self.gakusyuPoint+=2
        
    def HureauHenji(self):#ふれあう時の生物の返事　返す

        return self.hureau.HureauHenji(self.Nenrei)
    
    #event系処理

    #話すイベント

    def HanasuEvent(self):
        skotoba=self.even.Hanasuevent()
        self.Skotoba=skotoba
        return skotoba
        

    def seteventHanasuKotoba(self,kotoba):#新しい言葉として保存&返信する言葉として保存

        #キャッシュ保存
        self.kiokuKotoba=kotoba
        self.test()
        #話しかけるイベント処理
        self.gakusyuPoint+=self.even.seteventHanasuKotoba(kotoba)

    #プレイヤーに食べさせるイベント

    def getTabemono(self):#プレイヤーにプレゼントする食べ物を返す

        return self.even.getTabemono()

    def getTKotoba(self):#プレイヤーに食べ物プレゼントするときにいう言葉を返す

        return self.even.getTKotoba()        

    def seteventTArigatoKotoba(self,kotoba):#食べ物をもらったときにいうかんしゃのことば　保存

        #キャッシュ

        self.kiokuKotoba=kotoba
        
        #言葉更新 +学習ポイント取得
        gakusyupoint=self.even.seteventTArigatoKotoba(kotoba)
            
        #学習ポイント
        self.gakusyuPoint+=gakusyupoint
    
    #飲ませるイベント

    def getNomimono(self):#プレイヤーにプレゼントする飲みモノを返す

        return self.even.getNomimono()

    def getNKotoba(self):#プレイヤーに飲み物プレゼントするときにいう言葉を返す

        return self.even.getNKotoba()


    def seteventNArigatoKotoba(self,kotoba):#飲みものをもらったときにいうかんしゃのことば

        #キャッシュ

        self.kiokuKotoba=kotoba
        
        #言葉更新 +学習ポイント取得
        gakusyupoint=self.even.seteventNArigatoKotoba(kotoba)
            
        #学習ポイント
        self.gakusyuPoint+=gakusyupoint     
    
    def SeibutuClickHenji(self):
        return self.even.SeibutuClickHenji(self.Nenrei)


    #その時のゲーム内情報をコマンドプロンプトに表示
    def test(self):

        print('年齢:'+str(self.Nenrei))
        
        print('\n言葉  :'+str(self.Kotoba.kotoba))
        print('返事配列:'+str(self.Kotoba.Hensin))
        print('ダメ返事配列:'+str(self.Kotoba.DameHensin))
        print('種類　:'+str(self.Kotoba.syuruicode))
        print('syu')
        for x in range(16):
            self.Kotoba.printSyuruicodeHairetu(x)
        
        print('\n学習ポイント:'+str(self.gakusyuPoint))
        print('愛情ポイント:'+str(self.aijoPoint))

    #セーブ
    def Save(self,code):
 
        data=[]
        data.append(self.Danjo+'\n')#メスカオス化
        data.append(self.Iro+'\n')  #メスは赤、オスは青
        data.append(self.KunChan+'\n')#くんちゃん
        data.append(self.Name+'\n')

        data.append(str(self.size)+'\n')#縮小拡大
        #生物の顔の座標
        data.append(str(self.sx)+'\n')
        data.append(str(self.sy)+'\n')
        data.append(str(self.endsx)+'\n')
        data.append(str(self.endsy)+'\n')
        #足と手があるとき 足が高いとsy=190 低いとsy=255 sx60はそのまま
        #手足、羽などの座標
        # #足と手があるとき 足が高いとsy=170 低いとsy=235 sx60はそのまま
        
        data.append(str(self.futhandx)+'\n')
        data.append(str(self.futhandy)+'\n')

        #fut,hand　xは60 futが高いときは170 低いときは235

        data.append(self.face+'\n')
        data.append(self.eye+'\n')
        data.append(self.nose+'\n')
        data.append(self.mouth+'\n')
        data.append(self.fut+'\n')
        data.append(self.hand+'\n')

        data.append(str(self.Nenrei)+'\n')
        data.append(self.Seikaku+'\n')
        data.append(self.SukiTabemono+'\n')
        data.append(self.SukiNomimono+'\n')
        data.append(str(self.Manpukudo)+'\n')
        data.append(str(self.Uruoido)+'\n')

        data.append(str(self.count)+'\n')
        data.append(str(self.gakusyuPoint)+'\n')#学習ポイント
        data.append(str(self.aijoPoint)+'\n')#愛情ポイント

        data.append(self.kioku+'\n')#キャッシュ
        data.append(self.Skotoba+'\n')
        data.append(self.kiokuKotoba+'\n')

        data.append(str(self.SeikakuCode)+'\n')

        #出力
        print('\nSeibutuSyoriセーブ')
        print(data)

        f=open('./file/save'+str(code)+'/SeibutuSyori.txt','w',encoding='utf-8')
        f.writelines(data)
        f.close()

        #その他のファイルセーブ
        self.Kotoba.save(code)
        self.tabesa.save(code)
        self.nomase.save(code)
        self.hureau.save(code)
    
    def crea(self,code):

        #出力
        print('\nSeibutuSyoriクリア')

        f=open('./file/save'+str(code)+'/SeibutuSyori.txt','w',encoding='utf-8')
        f.close()

        #その他のファイルクリア
        self.Kotoba.crea(code)
        self.tabesa.crea(code)
        self.nomase.crea(code)
        self.hureau.crea(code)

    #ロード

    def load(self,code):
        self.syokika()
        data=[]
        with open('./file/save'+str(code)+'/SeibutuSyori.txt','r',encoding='utf-8')as f:
            data=f.read().split("\n")

            #出力
            print("SeibutuSyoriロード")
            print(data)

        
        self.Danjo=data[0]#メスカオス化
        self.Iro=data[1]  #メスは赤、オスは青
        self.KunChan=data[2]#くんちゃん
        self.Name=data[3]
        self.size=int(data[4])#縮小拡大
        #生物の顔の座標
        self.sx=int(data[5])
        self.sy=int(data[6])
        self.endsx=int(data[7])
        self.endsy=int(data[8])
        #足と手があるとき 足が高いとsy=190 低いとsy=255 sx60はそのまま
        #手足、羽などの座標
        # #足と手があるとき 足が高いとsy=170 低いとsy=235 sx60はそのまま
        
        self.futhandx=int(data[9])
        self.futhandy=int(data[10])

        #fut,hand　xは60 futが高いときは170 低いときは235

        self.face=data[11]
        self.eye=data[12]
        self.nose=data[13]
        self.mouth=data[14]
        self.fut=data[15]
        self.hand=data[16]

        self.Nenrei=int(data[17])
        self.Seikaku=data[18]
        self.SukiTabemono=data[19]
        self.SukiNomimono=data[20]
        self.Manpukudo=int(data[21])
        self.Uruoido=int(data[22])

        self.count=int(data[23])
        self.gakusyuPoint=int(data[24])#学習ポイント
        self.aijoPoint=int(data[25])#愛情ポイント

        self.kioku=data[26]#キャッシュ
        self.Skotoba=data[27]
        self.kiokuKotoba=data[28]

        self.SeikakuCode=data[29]

        #その他のファイルロード

        self.Kotoba.load(code)
        self.tabesa.load(code)
        self.nomase.load(code)
        self.hureau.load(code)

    
    def syokika(self):
        self.Kotoba.syokika()

        self.Danjo=''#メスカオス化
        self.Iro=''  #メスは赤、オスは青
        self.KunChan=''#くんちゃん
        self.Name=''

        #size=1#縮小拡大
        #sx=245
        #sy=320
        
        

        self.size=2#縮小拡大
        #生物の顔の座標
        self.sx=305
        self.sy=410
        self.endsx=400
        self.endsy=502
        #足と手があるとき 足が高いとsy=190 低いとsy=255 sx60はそのまま
        #手足、羽などの座標
        # #足と手があるとき 足が高いとsy=170 低いとsy=235 sx60はそのまま
        
        self.futhandx=60
        self.futhandy=170

        #fut,hand　xは60 futが高いときは170 低いときは235

        self.face='a'
        self.eye='a'
        self.nose='a'
        self.mouth='a'
        self.fut='a'
        self.hand='a'

        self.Nenrei=int(0)
        self.Seikaku='???'
        self.SeikakuCode=0
        self.SukiTabemono='???'
        self.SukiNomimono='???'
        self.Manpukudo=int(3)
        self.Uruoido=int(3)

        self.count=0
        self.gakusyuPoint=0#学習ポイント
        self.aijoPoint=20 #愛情ポイント

        self.kioku='a'#キャッシュ
        self.Skotoba='a'
        self.kiokuKotoba='a'


    