import Syori.KotobaKanri
import Syori.SonotaSyori.HairetuCheck
import random

class Hanasikakeru:

    Kotoba = Syori.KotobaKanri.KotobaKanri()
    hairetuck=Syori.SonotaSyori.HairetuCheck.HairetuCheck()

    kiokukotoba='a'

    def __init__(self,insKotoba):

        self.Kotoba=insKotoba

    #話しかける処理    
    def setKotoba(self,kotoba):

        #キャッシュ保存
        self.kiokuKotoba=kotoba
        self.Kotoba.kiokuKotoba=kotoba

        if False==self.hairetuck.HairetuCheck(self.Kotoba.kotoba,kotoba):#新しい言葉だったら保存

            #配列更新
            self.Kotoba.kotoba.append(kotoba)
            self.Kotoba.hindo.append(1)

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            #種類コード更新処理
            self.Kotoba.syuruiTuika(0)#0:話しかけるとき（話題の初め)

            self.Kotoba.setSyuruicodeHairetu(0,kotobaSoeji)
            
            #返信領域追加
            self.Kotoba.HensinTuika()

            return 4 #学習ポイント
               

        else:#既に知ってる言葉だったら
            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            #hindo[]更新
            self.Kotoba.hindo[kotobaSoeji]+=1

            self.Kotoba.syuruicodeKousin1(kotoba,0)#syuruicode0追加

            return 2 #学習ポイント
    
    def HanasikakeruHenji(self,nenrei):#生物が返事する言葉　返す

        return self.Kotoba.Henji(nenrei,1)
    