import random

class HairetuCheck:

    #その配列にその言葉があるかチェック

    def HairetuCheck(self,hairetu,j):
        for i in range(len(hairetu)):

            if hairetu[i]==j:
                return True#見つかった
            

            
        return False
    
    #その配列にその言葉があるかチェックしその添え字返す

    def HairetuSoeji(self,hairetu,j):

        for i in range(len(hairetu)):

            if hairetu[i]==j:
                return i#見つかった
            
        return 999
    
    #ランダムに探して、指定した値が格納されていたら添え字を返す
    
    def TansakuRandom(self,hairetu,x):

         while True:
                i=random.randint(0,len(hairetu)-1)
                if hairetu[i]==x:
                    return i
                    
    #指定した値の数を数える
    
    def HairetuCount(self,hairetu,x):
        count=0
        for i in range(len(hairetu)):

            if hairetu[i]==x:
                count+=1
                
        return count

    def HairetuRandom(self,hairetu):

         
        i=random.randint(0,len(hairetu)-1)
        return i#添え字
    
    def SoreigaiHairetu(self,hairetu,Damehairetu):#Dmehairetuに格納されている番号以外のhairetuの添え字を配列に格納して返す

        OKSoejiHairetu=[]

        for i in range(len(hairetu)):

            for j in range(len(Damehairetu)):

                if i != Damehairetu[j]:

                    OKSoejiHairetu.append(i)
        
        return OKSoejiHairetu

    def SoreigaiRandom(self,hairetu,Damehairetu):#Dmehairetuに格納されている番号以外のhairetuの添え字を返す

        OKhairetu=self.SoreigaiHairetu(hairetu,Damehairetu)

        return OKhairetu[self.HairetuRandom(OKhairetu)]
    
                