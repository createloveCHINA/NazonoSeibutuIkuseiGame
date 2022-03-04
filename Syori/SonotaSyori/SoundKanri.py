from tokenize import Double


class SoundKanri():

    BGMsyokiti=0.5
    BGMvol=BGMsyokiti
    BGMOnOff=True  #True=ON
    KoukaonOnOff=True #True=ON

    #BGMをONにする処理
    def BGMon(self):
        if self.BGMOnOff==False:#BGMがオフだったら
            self.BGMOnOff=True
            return True
        else:#BGMが元々オンだったら
            return False

    #BGMをOFFにする処理
    def BGMoff(self):
        if self.BGMOnOff==True:#BGMがオンだったら
            self.BGMOnOff=False
            return True
        else:#BGMが元々オフだったら
            return False

    #効果音をONにする処理
    def Koukaonon(self):
        if self.KoukaonOnOff==False:#効果音がオフだったら
            self.KoukaonOnOff=True
            return True
        else:#効果音が元々オンだったら
            return False

    #効果音をOFFにする処理
    def Koukaonoff(self):
        if self.KoukaonOnOff==True:#効果音がオンだったら
            self.KoukaonOnOff=False
            return True
        else:#効果音が元々オフだったら
            return False

    #BGMを0.1上げる
    def BGMbig(self):
        
        if self.BGMvol<1.0:
            self.BGMvol+=0.1
            return True
        else:
            return 
    #BGMを0.1下げる        
    def BGMsmall(self):
        
        if self.BGMvol>0.0:
            self.BGMvol-=0.1
            return True
        else:
            return False
    
    def getBGMvol(self):
        return self.BGMvol

    #セーブ
    def Save(self):
 
        data=[]
        data.append(str(self.BGMvol)+'\n')#ボリューム
        data.append(str(self.BGMOnOff)+'\n')#BGM on/off
        data.append(str(self.KoukaonOnOff)+'\n')#効果音 on/off

        #出力
        print('\nSoundKanriiセーブ')
        print(data)

        f=open('./Syori/SonotaSyori/SoundKanri.txt','w',encoding='utf-8')
        f.writelines(data)
        f.close()
    
    #ロード

    def load(self):

        data=[]
        with open('./Syori/SonotaSyori/SoundKanri.txt','r',encoding='utf-8')as f:
            data=f.read().split("\n")

            #出力
            print("SoundKanriロード")
            print(data)

        
        self.BGMvol=float(data[0])
        print(self.BGMvol)

        if data[1]=='True':
            self.BGMOnOff=True  #True=ON
        else:
            self.BGMOnOff=False

        if data[2]=='True':
            self.KoukaonOnOff=True #True=ON
        else:
            self.KoukaonOnOff=False
    
    def syokika(self):

        self.BGMvol=self.BGMsyokiti
        self.BGMOnOff=True  #True=ON
        self.KoukaonOnOff=True #True=ON