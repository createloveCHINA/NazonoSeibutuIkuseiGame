import Syori.SeibutuSyori
import Syori.Tarn

import datetime

class save():
    
    Seibutu = Syori.SeibutuSyori.SeibutuSyori()
    Tarn=Syori.Tarn.Tarn(Seibutu)

    def __init__(self,insTarn,insSeibutu):

        self.Tarn=insTarn
        self.Seibutu=insSeibutu
    
    def save(self,code):#指定したcodeの領域へセーブする

        #ゲームデータセーブ

        self.Tarn.Save(code)
        self.Seibutu.Save(code)

        #ファイル情報セーブ
        self.saveDataJoho(code)
        
        
    def saveDataJoho(self,code):

        data=[]

        time=datetime.datetime.now()
        data.append(str(time)[0:19]+'\n')#セーブした時間

        data.append(self.Seibutu.gethand()+'\n') #生物の顔
        data.append(self.Seibutu.getfut()+'\n')
        data.append(self.Seibutu.getface()+'\n')
        data.append(self.Seibutu.geteye()+'\n')
        data.append(self.Seibutu.getnose()+'\n')
        data.append(self.Seibutu.getmouth()+'\n')

        data.append(self.Seibutu.getName()+'\n')#名前
        data.append(self.Seibutu.getDanjo()+'\n')#性別
        data.append(str(self.Seibutu.getNenrei())+'\n')  #年齢

        futhandx,futhandy=self.Seibutu.getFutHandxy()
        data.append(str(futhandx)+'\n')#生物の手足のxの位置
        data.append(str(futhandy)+'\n')  #生物の手足のyの位置


        #出力
        print('\nSaveJohoセーブ')
        print(data)

        f=open('./file/save'+str(code)+'/SaveJoho.txt','w',encoding='utf-8')
        f.writelines(data)
        f.close()
    
        f=open('./file/save'+str(code)+'/saveCheck.txt','w')#save済みにする
        f.write(str(1))
        f.close()
    