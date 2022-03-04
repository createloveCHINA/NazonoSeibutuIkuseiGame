import Syori.SeibutuSyori 
import random

class Tarn():

    seibutu=Syori.SeibutuSyori.SeibutuSyori()

    def __init__(self,insSeibutu):

        self.seibutu=insSeibutu

    tarn=0
    Htarn=0
    Ttarn=0
    Ntarn=0
    manpukuherasiTarn=1
    uruoiherasiTarn=1
    aijoPointHerasiTarn=1

    GameOverNaiyo=''
    GameOverColor=''


        
    def a(self):
        a=0
    
    def setHTarn(self):#話しかけたターンを更新

        self.Htarn=self.tarn

    def setTTarn(self):#食べたターン更新
        self.Ttarn=self.tarn
    

    def setNTarn(self):#飲んだターン更新
        self.Ntarn=self.tarn

    def getTTarnCheck(self):#食べれるターンだったらTrue

        if self.seibutu.Manpukudo<10:
            return True
        else:
            return False

    def getNTarnCheck(self):#飲めるターンだったらTrue

        if self.seibutu.Uruoido<10:
            return True
        else:
            return False

    def setTarn(self):#ターン更新その他の更新もする
        #self.seibutu.gakusyuPoint+=200
 
        self.tarn +=1
        self.ManpukuHerasi()#満腹度更新
        self.UruoiHerasi()#うるおい度更新
        self.AijoPointHerasi()#愛情ポイント更新
        self.NenreiKousin()#年齢更新

        self.SeikakuKousin()#性格更新

        #テスト出力(状態)
        print('\n更新された情報')
        print('\n'+str(self.tarn)+'ターン（次から）')
        
        return self.Hantei()

    #まんぷく度を減らす処理
    def ManpukuHerasi(self):

        if self.seibutu.Manpukudo==10 and self.tarn-self.manpukuherasiTarn==8:#まんぷく　かつ　減らしたターンより8ターン経過したら、5減らす

            self.seibutu.Manpukudo -=5

            self.manpukuherasiTarn=self.tarn
        
        elif not self.seibutu.Manpukudo==10 and self.tarn-self.manpukuherasiTarn==4:#まんぷくじゃないときは、　５ターンごとに　２　減っていく


            self.seibutu.Manpukudo -=2

            self.manpukuherasiTarn=self.tarn

    #潤い度を減らす処理 
    def UruoiHerasi(self):

        if self.seibutu.Uruoido==10 and self.tarn-self.uruoiherasiTarn==8:#潤い度まんぷく　かつ　減らしたターンより8ターン経過したら、5減らす


            self.seibutu.Uruoido -=5

            self.uruoiherasiTarn=self.tarn

        elif not self.seibutu.Uruoido==10 and self.tarn-self.uruoiherasiTarn==4:#まんぷくじゃないときは、　５ターンごとに　２　減っていく

            self.seibutu.Uruoido -=2

            self.uruoiherasiTarn=self.tarn
    
    #愛情ポイントを減らす処理
    def AijoPointHerasi(self):

        if self.tarn-self.aijoPointHerasiTarn==10:#愛情ポイント減らしたターンより10ターン経過したら、4減らす

            self.seibutu.aijoPoint -=4

            self.aijoPointHerasiTarn=self.tarn
            
    #年齢更新処理
    def NenreiKousin(self):

        nenrei=self.seibutu.Nenrei
        usiro=len(self.seibutu.gakusyuPointMokuhyou)-1

        #self.seibutu.gakusyuPoint+=100###########################################

        if usiro>=nenrei:

            if nenrei==0:

                if self.tarn>4:#==self.seibutu.gakusyuPointMokuhyou[nenrei]:#5回お世話したら##############################

                    self.seibutu.Nenrei+=1# 1裁になる

            elif nenrei==1:

                if self.tarn>9:#==self.seibutu.gakusyuPointMokuhyou[nenrei]:#5回お世話###############################

                    self.seibutu.Nenrei+=1# 2裁になる
                    self.seibutu.nenreibetuSetSeibutu()#生物の見た目更新

                    
            elif nenrei==2:

                if self.seibutu.gakusyuPoint>self.seibutu.gakusyuPointMokuhyou[nenrei]:#35ポイント以上で

                    self.seibutu.Nenrei+=1# 3裁になる

            elif nenrei==3:
                
                if self.seibutu.gakusyuPoint>self.seibutu.gakusyuPointMokuhyou[nenrei]:#45ポイント以上で

                    self.seibutu.Nenrei+=1# 4裁になる
                    self.seibutu.nenreibetuSetSeibutu()#生物の見た目更新
        

            elif nenrei==4:

                if self.seibutu.gakusyuPoint>self.seibutu.gakusyuPointMokuhyou[nenrei]:

                    self.seibutu.Nenrei+=1# 5裁になる

            elif nenrei==5:

                if self.seibutu.gakusyuPoint>self.seibutu.gakusyuPointMokuhyou[nenrei] :
                    
                    self.seibutu.Nenrei+=1# 6裁になる
                    self.seibutu.nenreibetuSetSeibutu()#生物の見た目更新

            elif nenrei==6:

                if self.seibutu.gakusyuPoint>self.seibutu.gakusyuPointMokuhyou[nenrei] :

                    self.seibutu.Nenrei+=1# 7裁になる
            
            elif nenrei==7:

                if self.seibutu.gakusyuPoint>self.seibutu.gakusyuPointMokuhyou[nenrei] :

                    self.seibutu.Nenrei+=1# 8裁になる
                    self.seibutu.nenreibetuSetSeibutu()#生物の見た目更新
            elif nenrei==8:

                if self.seibutu.gakusyuPoint>self.seibutu.gakusyuPointMokuhyou[nenrei]:

                    self.seibutu.Nenrei+=1# 9裁になる
            elif nenrei==9:

                if self.seibutu.gakusyuPoint>self.seibutu.gakusyuPointMokuhyou[nenrei]:

                    self.seibutu.Nenrei+=1# 10裁になる
            elif nenrei==10:

                if self.seibutu.gakusyuPoint>self.seibutu.gakusyuPointMokuhyou[nenrei]:

                    self.seibutu.Nenrei+=1# 11裁になる
                    #self.seibutu.nenreibetuSetSeibutu()#生物の見た目更新
            
            
        else:
             
            mokuhyo=self.seibutu.gakusyuPointMokuhyou[usiro]+(nenrei-usiro)*25

            if self.seibutu.gakusyuPoint>mokuhyo:

                self.seibutu.Nenrei+=1



        

        
        
    #性格更新処理
    def SeikakuKousin(self):

        if self.seibutu.Nenrei>=3:
            
            self.seibutu.SeikakuKousin()
    
    #event決める処理

    def setevent(self):
        print('\nイベント決めます')
        num=random.randint(1,100)
        if num<=60:#60%の確率でイベント発生
            print('\neventあり')
            num=random.randint(1,100)
            
            if num>30:#お話イベント

                return 1
            else:#プレゼントイベント
                num=random.randint(1,100)
                if num%2==0:
                    return 2#食べ物プレゼントイベント
                else:
                    return 3#飲み物プレゼントイベント
        else:
            print('\neventなし')
            return 99#イベントなし
            

    def Hantei(self):#ゲームオーバーか判定
        
        if self.seibutu.Manpukudo<=0 :

            self.GameOverNaiyo='えいようしっちょう'
            self.GameOverColor='LightSalmon1'

            return  False#ゲームオーバーの理由

        elif self.seibutu.Uruoido<=0:

            self.GameOverNaiyo='だっすいしょうじょう'
            self.GameOverColor='LightSkyBlue1'

            return False#ゲームオーバーの理由

        elif self.seibutu.aijoPoint<=0:

            self.GameOverNaiyo='あいじょうぶそく'
            self.GameOverColor='RosyBrown1'

            return False#ゲームオーバーの理由

        return True#死なない
    def Save(self,code):
    
        data=[]

        data.append(str(self.tarn)+'\n')
        data.append(str(self.Htarn)+'\n')
        data.append(str(self.Ttarn)+'\n')
        data.append(str(self.Ntarn)+'\n')
        data.append(str(self.manpukuherasiTarn)+'\n')
        data.append(str(self.uruoiherasiTarn)+'\n')
        data.append(str(self.aijoPointHerasiTarn)+'\n')

        #出力
        print('\nTarnセーブ')
        print(data)

        f=open('./file/save'+str(code)+'/Tarn.txt','w',encoding='utf-8')
        f.writelines(data)
        f.close()
    
    def crea(self,code):

        #出力
        print('\nTarnクリア')

        f=open('./file/save'+str(code)+'/Tarn.txt','w',encoding='utf-8')
        f.close()

    def load(self,code):
        self.syokika()
        data=[]
        with open('./file/save'+str(code)+'/Tarn.txt','r',encoding='utf-8')as f:
            data=f.read().split("\n")

            #出力
            print("tarnロード")
            print(data)
       
        self.tarn=int(data[0])
        self.Htarn=int(data[1])
        self.Ttarn=int(data[2])
        self.Ntarn=int(data[3])
        self.manpukuherasiTarn=int(data[4])
        self.uruoiherasiTarn=int(data[5])
        self.aijoPointHerasiTarn=int(data[6])

    def syokika(self):
        self.tarn=1

        self.Htarn=0
        self.Ttarn=0
        self.Ntarn=0
        self.manpukuherasiTarn=1
        self.uruoiherasiTarn=1
        self.aijoPointHerasiTarn=1
       
    

