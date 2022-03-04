import Syori.KotobaKanri
import Syori.SonotaSyori.HairetuCheck
import random

class Nomaseru:
    
    Kotoba = Syori.KotobaKanri.KotobaKanri()
    hairetuck=Syori.SonotaSyori.HairetuCheck.HairetuCheck()

    SukiNomimono='a'

    def __init__(self,insKotoba):

        self.Kotoba=insKotoba

    def setNomimono(self,nomimono):#食べ物処理 manpukudo返す
        
        uruoido=0
        Imasoeji=0


        #既に入力済みかどうか調べて配列更新
        if True==self.hairetuck.HairetuCheck(self.Kotoba.nomimono,nomimono):#既に格納されていたら
            #ImaSoeji=今回入力した飲み物の添え字
            ImaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.nomimono,nomimono)

            #飲み物の頻度+1
            self.Kotoba.Nhindo[self.hairetuck.HairetuSoeji(self.Kotoba.nomimono,nomimono)]+=1
            uruoido=self.Kotoba.Uruoido[ImaSoeji]

        else:#初めての飲み物だったら

            #うるおい度計算
            uruoido=random.randint(1,100)%6
            if uruoido==0:
                uruoido+=1

            self.Kotoba.nomimono.append(nomimono)
            self.Kotoba.Nhindo.append(1)
            self.Kotoba.Uruoido.append(uruoido)
            self.kioku=nomimono

            #ImaSoeji=今回入力した飲み物の添え字
            ImaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.nomimono,nomimono)

        #好物更新

        if len(self.Kotoba.nomimono)==1:#初めての飲み物
            
            self.SukiNomimono=nomimono#好物更新
        else:
            #soeji=飲み物の好物の添え字
            Soeji=self.hairetuck.HairetuSoeji(self.Kotoba.nomimono,self.SukiNomimono)#今の好物のうるおい度よりも、今回の飲み物のほうが大きいとき

            if uruoido>self.Kotoba.Uruoido[Soeji]:

                self.SukiNomimono=nomimono#好物更新

            elif uruoido==self.Kotoba.Uruoido[Soeji] and self.Kotoba.Nhindo[ImaSoeji]>self.Kotoba.Nhindo[Soeji]:#うるおい度がどちらも同じ　かつ　飲み物の頻度が今回入力した方が大きいとき

                self.SukiNomimono=nomimono#好物更新

        print('うるおい度：'+str(uruoido))

        return uruoido #飲み物の増えるうるおい度　返す
    
    def setNKotoba(self,kotoba):

        self.Kotoba.kiokuKotoba=kotoba

        if True==self.hairetuck.HairetuCheck(self.Kotoba.kotoba,kotoba) :#知っている言葉だったら

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            self.Kotoba.hindo[kotobaSoeji]+=1

            self.Kotoba.syuruicodeKousin1(kotoba,3)#syuruicode6追加

            self.Kotoba.syuruicodeKousin2(kotoba,2,4)#syuruicode5があったら1追加

        else:

            self.Kotoba.kotoba.append(kotoba)
            self.Kotoba.hindo.append(1)

            kotobaSoeji=self.hairetuck.HairetuSoeji(self.Kotoba.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

            #syuruicode処理
            self.Kotoba.syuruiTuika(3)

            self.Kotoba.setSyuruicodeHairetu(3,kotobaSoeji)
            
            #返信領域追加
            self.Kotoba.HensinTuika()


    def getSukiNomimono(self):#好物返す

        return self.SukiNomimono
    
    def NomaseruHenji(self,nenrei):#生物が返事する言葉　返す

        return self.Kotoba.Henji(nenrei,3)
    
    #セーブ
    def save(self,code):

        data=[]
        data.append(self.SukiNomimono+'\n')
        
        #出力
        print('\nNomaseruセーブ')
        print(data)

        f=open('./file/save'+str(code)+'/Nomaseru.txt','w',encoding='utf-8')
        f.writelines(data)
        f.close()
    
    #データクリア
    def crea(self,code):

        print('\nNomaseruクリア')

        f=open('./file/save'+str(code)+'/Nomaseru.txt','w',encoding='utf-8')
        f.close()
    
    #ロード
    def load(self,code):
        self.syokika()
        data=[]
        with open('./file/save'+str(code)+'/Nomaseru.txt','r',encoding='utf-8')as f:
            data=f.read().split("\n")

            #出力
            print("Nomaseruロード")
            print(data)

        self.SukiNomimono=data[0]
    
    #初期化
    def syokika(self):

        self.SukiNomimono='a'