import Syori.KotobaKanri
import Syori.SonotaSyori.HairetuCheck
import random

class Tabesaseru:
    
    Kotoba = Syori.KotobaKanri.KotobaKanri()
    hairetuck=Syori.SonotaSyori.HairetuCheck.HairetuCheck()

    SukiTabemono='a'

    def __init__(self,insKotoba):

        self.Kotoba=insKotoba
    
    def setTabemono(self,tabemono):#食べ物処理 manpukudo返す
        
        manpukudo=0
        Imasoeji=0

        #既に入力済みかどうか調べて配列更新

        if True==self.hairetuck.HairetuCheck(self.Kotoba.tabemono,tabemono):#既に格納されていたら

            #ImaSoeji=今回入力した食べ物の添え字
            ImaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.tabemono,tabemono)

            #食べ物の頻度+1
            self.Kotoba.Thindo[ImaSoeji]+=1
            manpukudo=self.Kotoba.Tmanpukudo[ImaSoeji]
            
        else:#初めての食べ物だったら

            #満腹度計算
            manpukudo=random.randint(1,100)%6
            if manpukudo==0:
                manpukudo+=1

            self.Kotoba.tabemono.append(tabemono)
            self.Kotoba.Thindo.append(1)
            self.Kotoba.Tmanpukudo.append(manpukudo)
            self.kioku=tabemono

            #ImaSoeji=今回入力した食べ物の添え字
            ImaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.tabemono,tabemono)

        #好物更新処理

        if len(self.Kotoba.tabemono)==1:#初めての食べ物
            
            self.SukiTabemono=tabemono#好物更新
        else:
            #soeji=食べ物の好物の添え字
            Soeji=self.hairetuck.HairetuSoeji(self.Kotoba.tabemono,self.SukiTabemono)
            

            if manpukudo>self.Kotoba.Tmanpukudo[Soeji]:#今の好物の満腹度よりも、今回の食べ物のほうが大きいとき
                
                self.SukiTabemono=tabemono#好物更新
            
            elif manpukudo==self.Kotoba.Tmanpukudo[Soeji] and self.Kotoba.Thindo[ImaSoeji]>self.Kotoba.Thindo[Soeji]:#まんぷく度がどちらも同じ　かつ　食べ物の頻度が今回入力した方が大きいとき

                self.SukiTabemono=tabemono#好物更新

                

        print('満腹度：'+str(manpukudo))
        return manpukudo #食べ物の増える満腹度　返す
    
    def setTKotoba(self,kotoba):

        self.Kotoba.kiokuKotoba=kotoba
        
        if True==self.hairetuck.HairetuCheck(self.Kotoba.kotoba,kotoba) :

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            self.Kotoba.hindo[kotobaSoeji]+=1
            
            self.Kotoba.syuruicodeKousin1(kotoba,2)#syuruicode6追加

            self.Kotoba.syuruicodeKousin2(kotoba,3,4)#syuruicode5があったら1追加

        else:
            
            #配列更新
            self.Kotoba.kotoba.append(kotoba)
            self.Kotoba.hindo.append(1)

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            #syuruicode処理
            self.Kotoba.syuruiTuika(2)

            self.Kotoba.setSyuruicodeHairetu(2,kotobaSoeji)

            #返信領域追加
            self.Kotoba.HensinTuika()


    def getSukiTabemono(self):#好物返す

        return self.SukiTabemono
    
    def TabesaseruHenji(self,nenrei):#生物が返事する言葉　返す

        return self.Kotoba.Henji(nenrei,2)
    
    #セーブ
    def save(self,code):

        data=[]
        data.append(self.SukiTabemono+'\n')
        
        #出力
        print('\nTabesaseruセーブ')
        print(data)

        f=open('./file/save'+str(code)+'/Tabesaseru.txt','w',encoding='utf-8')
        f.writelines(data)
        f.close()
    
    #データクリア
    def crea(self,code):
        
        #出力
        print('\nTabesaseruクリア')

        f=open('./file/save'+str(code)+'/Tabesaseru.txt','w',encoding='utf-8')
        f.close()
    
    #ロード
    def load(self,code):
        self.syokika()
        data=[]
        with open('./file/save'+str(code)+'/Tabesaseru.txt','r',encoding='utf-8')as f:
            data=f.read().split("\n")

            #出力
            print("Tabesaseruロード")
            print(data)

        self.SukiTabemono=data[0]
    
    #初期化
    def syokika(self):

        self.SukiTabemono='a'


                