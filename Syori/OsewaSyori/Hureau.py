import Syori.KotobaKanri
import Syori.SonotaSyori.HairetuCheck
import random

class Hureau():

    Kotoba = Syori.KotobaKanri.KotobaKanri()
    hairetuck=Syori.SonotaSyori.HairetuCheck.HairetuCheck()

    def __init__(self,insKotoba):

        self.Kotoba=insKotoba

    hiragana='a'
    color='a'

    #前回のふれあう番号
    ima=999
    mae=999

    #ima更新(キャッシュ)

    def setima(self,num):

        #maeKousin
        self.mae=self.ima

        #初期化
        self.ima=999
        self.hiragana='a'
        self.color='a'

        self.ima=num

        #hiragana と color 更新
        self.setHiragana()
        self.setColor()

    #愛情ポイントを返す
    def getPoint(self):

        if self.mae != self.ima:

            return 6
        
        else :
            return 3

    #選択したラジオボタンの結果を更新
    def setHiragana(self):


        if self.ima==0:
            self.hiragana='なでる'
        elif self.ima==1:
            self.hiragana= 'ハグする'
        elif self.ima==2:
            self.hiragana= 'だっこする'
        elif self.ima==3:
            self.hiragana= 'キスする'

    #選択したラジオボタンの色を更新
    def setColor(self):

        if self.ima==0:
            self.color='yellow'
        elif self.ima==1:
            self.color='LightSalmon'
        elif self.ima==2:
            self.color='LightSkyBlue'
        elif self.ima==3:
            self.color='PaleVioletRed1'

    def getNaiyou(self):#HiraganaとColorを返す
        return self.hiragana,self.color
    
    #種類コードを返す(ふれあう言葉更新する時に使う)
    #先頭は、その時選んだ種類コード
    def getSyuruicode(self):

        if self.ima==0:
            return [8,9,10,11]
        elif self.ima==1:
            return [9,8,10,11]
        elif self.ima==2:
            return [10,8,9,11]
        elif self.ima==3:
            return [11,8,9,10]
    
    #ふれあう時に言う言葉

    def setHKotoba(self,kotoba):

        gakusyupoint=0
        
        #先頭：そのとき選んだふれあう種類コード　それ以降：それ以外の種類コード を受け取る
        Hsyu=self.getSyuruicode() #←←配列

        #キャッシュ保存
        self.Kotoba.kiokuKotoba=kotoba

        #既に入力済みかどうか調べて配列更新
        if True==self.hairetuck.HairetuCheck(self.Kotoba.kotoba,kotoba) :#初めてじゃない言葉だったら

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            #言葉の頻度+1
            self.Kotoba.hindo[kotobaSoeji]+=1#kotobaのkotoba配列に]+=1

            self.Kotoba.syuruicodeKousin1(kotoba,Hsyu[0])#syuruicode6追加

            #今回入力した言葉に対応する種類コード配列
            syuhairetu=self.Kotoba.syuruicode[kotobaSoeji]

            if self.hairetuck.HairetuCheck(syuhairetu,(Hsyu[1]))==True or self.hairetuck.HairetuCheck(syuhairetu,(Hsyu[2]))==True or self.hairetuck.HairetuCheck(syuhairetu,(Hsyu[3]))==True  and self.hairetuck.HairetuCheck(syuhairetu,(12))==False:#今回選んでいない、ふれあう種類コードの言葉だったら

                self.Kotoba.setSyuruicodeHairetu(12,kotobaSoeji)#syuに追加
                self.Kotoba.syuruicode[kotobaSoeji].append(12)#syuruicode追加


        else:#初めての言葉だったら

            self.Kotoba.kotoba.append(kotoba)
            self.Kotoba.hindo.append(1)

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字
            
            #種類コード更新処理
            self.Kotoba.syuruiTuika(Hsyu[0])
            self.Kotoba.setSyuruicodeHairetu(Hsyu[0],kotobaSoeji)
            #返信領域追加
            self.Kotoba.HensinTuika()


    def HureauHenji(self,nenrei):#生物が返事する言葉　返す

        #今回ふれあった種類の番号取得
        syu=self.getSyuruicode()

        return self.Kotoba.Henji(nenrei,syu[0])#生物が返事する言葉　返す

    #セーブ
    def save(self,code):

        data=[]
        data.append(self.hiragana+'\n')
        data.append(self.color+'\n')
        data.append(str(self.ima)+'\n')
        data.append(str(self.mae)+'\n')

        #出力
        print('\nHureau4Kanriセーブ')
        print(data)

        f=open('./file/save'+str(code)+'/Hureau.txt','w',encoding='utf-8')
        f.writelines(data)
        f.close()
    
    #データクリア
    def crea (self,code):

        #出力
        print('\nHureau4Kanriクリア')

        f=open('./file/save'+str(code)+'/Hureau.txt','w',encoding='utf-8')
        f.close()
    
    #ロード
    def load(self,code):
        self.syokika()
        data=[]
        with open('./file/save'+str(code)+'/Hureau.txt','r',encoding='utf-8')as f:
            data=f.read().split("\n")

            #出力
            print("Hureau4Kanriロード")
            print(data)

        self.hiragana=data[0]
        self.color=data[1]
        self.ima=int(data[2])
        self.mae=int(data[3])
    
    #初期化
    def syokika(self):

        self.hiragana='a'
        self.color='a'

        #前回のふれあう番号
        self.ima=999
        self.mae=999



        

    


    


