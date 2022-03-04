import Syori.SeibutuSyori
import Syori.Tarn

class crea():
    
    Seibutu = Syori.SeibutuSyori.SeibutuSyori()
    Tarn=Syori.Tarn.Tarn(Seibutu)

    def __init__(self,insTarn,insSeibutu):

        self.Tarn=insTarn
        self.Seibutu=insSeibutu

    
    def crea(self,code):

        #Tarnファイルクリア
        self.Tarn.crea(code)
        #Seibutuファイルクリア
        self.Seibutu.crea(code)
        #saveJohoファイルクリア
        self.creaDataJoho(code)
        
    #クリア
    def creaDataJoho(self,code):

        #出力
        print('\nSaveJohoクリア')

        f=open('./file/save'+str(code)+'/SaveJoho.txt','w',encoding='utf-8')
        f.close()
    
        f=open('./file/save'+str(code)+'/saveCheck.txt','w')#ノーデータ
        f.write(str(0))
        f.close()
