import Syori.KotobaKanri
import Syori.SonotaSyori.HairetuCheck
import random

class Kaiwasuru:

    Kotoba = Syori.KotobaKanri.KotobaKanri()
    hairetuck=Syori.SonotaSyori.HairetuCheck.HairetuCheck()
    
    def __init__(self,insKotoba):

        self.Kotoba=insKotoba
    
    count=0#会話、何回連続会話しているか

    def getcount(self):

        return self.count

    def setcount(self):

        self.count+=1
    
    def syuryo(self):

        self.count=0
    
    
    def setKaiwaKotoba(self,kotoba):#新しい言葉として保存&返信する言葉として保存

        #キャッシュ保存
        self.Kotoba.kiokuKotoba=kotoba

        gakusyupoint=0
        
        #入力した言葉 更新
        if False==self.hairetuck.HairetuCheck(self.Kotoba.kotoba,kotoba):#新しい言葉だったら保存

            #配列更新
            self.Kotoba.kotoba.append(kotoba)
            self.Kotoba.hindo.append(1)

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            if self.count==0:

                #syuruicode処理
                self.Kotoba.syuruiTuika(0)
            else:
                #syuruicode処理
                self.Kotoba.syuruiTuika(13)
                
            self.Kotoba.setSyuruicodeHairetu(0,kotobaSoeji)
            
            #返信ネット追加
            self.Kotoba.HensinTuika()

            gakusyupoint= 2 #学習ポイント
               

        else:#既に知ってる言葉だったら

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            #hindo[]更新
            self.Kotoba.hindo[kotobaSoeji]+=1

            if self.count==0:

                #syuruicode処理
                self.Kotoba.syuruicodeKousin1(kotoba,0)
            else:
                #syuruicode処理
                self.Kotoba.syuruicodeKousin1(kotoba,13)
                
                self.Kotoba.syuruicodeKousin1(kotoba,15)#syuruicode0追加#15:あいさつ

                print(self.Kotoba.syu15)

                self.Kotoba.syuruicodeGyakuKousin(kotoba,1,4)#返事のことばの種類コードに、１（感謝）があったら、　言った言葉は　４（感謝される言葉）ということ


            gakusyupoint= 1 #学習ポイント
        
        if self.count!=0:
        
            self.Kotoba.HensinKousin(self.Kotoba.kiokuSkotoba,kotoba)#kotobaが今回生物が言った言葉に対する返事として、Hensin　更新

        return gakusyupoint

    def KaiwaHenji(self,nenrei):#生物が返事する言葉　返す

        return self.Kotoba.KaiwaHenji(self.count)##会話はkaiwa専用のメソッド呼び出す
