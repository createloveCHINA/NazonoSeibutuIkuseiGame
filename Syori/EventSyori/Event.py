import Syori.KotobaKanri
import Syori.SonotaSyori.HairetuCheck
import random


class Event():

    Kotoba = Syori.KotobaKanri.KotobaKanri()
    hairetuck=Syori.SonotaSyori.HairetuCheck.HairetuCheck()

    def __init__(self,insKotoba):

        self.Kotoba=insKotoba

    #event系処理

    #生物が話しかけてくるイベント

    def Hanasuevent(self):
                self.Skotoba=self.Kotoba.eventbetuKotoba(0)
                return self.Skotoba

    def seteventHanasuKotoba(self,kotoba):#新しい言葉として保存&返信する言葉として保存

        #キャッシュ保存
        self.Kotoba.kiokuKotoba=kotoba

        gakusyupoint=0
        
        #入力した言葉 更新
        if False==self.hairetuck.HairetuCheck(self.Kotoba.kotoba,kotoba):#新しい言葉だったら保存

            #配列更新
            self.Kotoba.kotoba.append(kotoba)
            self.Kotoba.hindo.append(1)

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            #syuruicode処理
            self.Kotoba.syuruiTuika(13)

            self.Kotoba.setSyuruicodeHairetu(0,kotobaSoeji)
            
            #返信ネット追加
            self.Kotoba.HensinTuika()

            gakusyupoint= 5 #学習ポイント
               

        else:#既に知ってる言葉だったら

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            #hindo[]更新
            self.Kotoba.hindo[kotobaSoeji]+=1
            
            #種類コード更新処理
            self.Kotoba.syuruicodeKousin1(kotoba,13)#syuruicode0追加
            
            self.Kotoba.syuruicodeKousin1(kotoba,15)#syuruicode0追加#15:あいさつ

            self.Kotoba.syuruicodeGyakuKousin(kotoba,1,4)#返事のことばの種類コードに、１（感謝）があったら、　言った言葉は　４（感謝される言葉）ということ

            gakusyupoint= 5 #学習ポイント
        
        print("EventHanasuのダメ返信")
        print(self.Kotoba.DameHensin)
        self.Kotoba.HensinKousin(self.Kotoba.kiokuSkotoba,kotoba)#kotobaが今回生物が言った言葉に対する返事として、Hensin　更新

        return gakusyupoint

    
    #プレイヤーに食べさせるイベント

    def getTabemono(self):#プレイヤーにプレゼントする食べ物を返す

        num=random.randint(0,len(self.Kotoba.tabemono)-1)

        return self.Kotoba.tabemono[num]

    def getTKotoba(self):#プレイヤーに食べ物プレゼントするときにいう言葉を返す

        return self.Kotoba.eventbetuKotoba(2)        

    def seteventTArigatoKotoba(self,kotoba):#食べ物をもらったときにいうかんしゃのことば　保存 and 学習ポイント 返す

        #キャッシュ
        self.Kotoba.kiokuKotoba=kotoba

        gakusyupoint=0

        if True==self.hairetuck.HairetuCheck(self.Kotoba.kotoba,kotoba) :#kotobaが既に配列にあったら

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            self.Kotoba.hindo[kotobaSoeji]+=1

            self.Kotoba.syuruicodeKousin1(kotoba,5)#syuruicode5追加

            self.Kotoba.syuruicodeKousin2(kotoba,6,1)#syuruicode6があったら1追加

            gakusyupoint=3

        else:
            self.Kotoba.kotoba.append(kotoba)
            self.Kotoba.hindo.append(1)

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            #syuruicode処理
            self.Kotoba.syuruiTuika(5)
            print('種類追加')
            print(self.Kotoba.syuruicode)
            self.Kotoba.setSyuruicodeHairetu(5,kotobaSoeji)

            #返信領域追加
            self.Kotoba.HensinTuika()

            gakusyupoint=4
        
        self.Kotoba.HensinKousin(self.Kotoba.kiokuSkotoba,kotoba)#kotobaが今回生物が言った言葉に対する返事として、Hensin　更新
        
        return gakusyupoint
    
    #飲ませるイベント

    def getNomimono(self):#プレイヤーにプレゼントする飲みモノを返す

        num=random.randint(0,len(self.Kotoba.nomimono)-1)

        return self.Kotoba.nomimono[num]

    def getNKotoba(self):#プレイヤーに飲み物プレゼントするときにいう言葉を返す

        return self.Kotoba.eventbetuKotoba(3)


    def seteventNArigatoKotoba(self,kotoba):#飲みものをもらったときにいうかんしゃのことば

        #キャッシュ
        self.Kotoba.kiokuKotoba=kotoba

        gakusyupoint=0

        if True==self.hairetuck.HairetuCheck(self.Kotoba.kotoba,kotoba) :#kotobaが既にあったら

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            self.Kotoba.hindo[kotobaSoeji]+=1

            self.Kotoba.syuruicodeKousin1(kotoba,6)#syuruicode6追加

            self.Kotoba.syuruicodeKousin2(kotoba,5,1)#syuruicode5があったら1追加

            gakusyupoint=3

        else:
            self.Kotoba.kotoba.append(kotoba)
            self.Kotoba.hindo.append(1)

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            #syuruicode処理
            self.Kotoba.syuruiTuika(6)
            self.Kotoba.setSyuruicodeHairetu(6,kotobaSoeji)

            #返信領域追加
            self.Kotoba.HensinTuika()

            gakusyupoint=4

        self.Kotoba.HensinKousin(self.Kotoba.kiokuSkotoba,kotoba)#kotobaが今回生物が言った言葉に対する返事として、Hensin　更新

        return gakusyupoint

    #クリックイベント処理

    def SeibutuClickHenji(self,nenrei):
        return self.Kotoba.Henji(nenrei,0)

