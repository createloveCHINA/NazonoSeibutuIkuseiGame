import Syori.SeibutuSyori
import Syori.Tarn
#import Syori.DataKanri.load
#import Syori.DataKanri.save

class DataKanri():

    Seibutu = Syori.SeibutuSyori.SeibutuSyori()
    Tarn=Syori.Tarn.Tarn(Seibutu)

    def __init__(self,insTarn,insSeibutu):

        self.Tarn=insTarn
        self.Seibutu=insSeibutu


    Datahairetu=[]
    count=0

    def setDatahairetu(self):
        
        del self.Datahairetu[:]

        for x in range(3):

            s=int(0)
            with open('./file/save'+str(x+1)+'/saveCheck.txt','r',encoding='utf-8')as f:
                s=int(f.read())

            if s==1:

                self.Datahairetu.append(True)
            else:
                self.Datahairetu.append(False)
        
    
    def getDatahairetu(self):        

        self.setDatahairetu()

        return self.Datahairetu
    
    def getDataJoho(self,code):

        data=[]
        with open('./file/save'+str(code)+'/SaveJoho.txt','r',encoding='utf-8')as f:
            data=f.read().split("\n")

            #出力
            print("saveJohoロード")
            print(data)

        
        nitizi=data[0]#セーブされた時間

        #顔hairetu
        kaoHairetu=[]

        for i in range(1,7):
            kaoHairetu.append(data[i])
    
        #名前、性別、年齢
        johoHairetu=[]
        for i in range(7,10):

            johoHairetu.append(data[i])
        
        futhandxy=[]
        futhandxy.append(int(data[10]))
        futhandxy.append(int(data[11]))

        return nitizi,johoHairetu,kaoHairetu,futhandxy
    
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
    
