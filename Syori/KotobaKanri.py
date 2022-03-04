from os import kill
import random
import Syori.SonotaSyori.KanaCheck
import Syori.SonotaSyori.HairetuCheck
class KotobaKanri ():

    hairetuck=Syori.SonotaSyori.HairetuCheck.HairetuCheck()
    kana=Syori.SonotaSyori.KanaCheck.KanaCheck()
	
	#普通の言葉についての領域
    kotoba =[]
    hindo=[]
    syuruicode= []  
    '''

    syuruicodeの種類番号
    
    0=話しかけるとき（話題の初め）,1=感謝,2=食べさせるとき,3=飲ませるとき,4=感謝される言葉（誉め言葉とか）,5=食べ物を貰った時の感謝
        
        
    ,6=飲み物を貰った時の感謝,7=良い言葉(モノをあげるとき系以外),8=なでるとき,9=ハグするとき,10=だっこするとき
    
    ,11=キスする時,12=ふれあうとき,13=内容？,14=会話を終わらせられる言葉,15=あいさつ

    '''

    syu0=[]#話しかけるとき（話題の初め
    syu1=[]#感謝
    syu2=[]#食べさせる時
    syu3=[]#飲ませるとき
    syu4=[]#感謝される言葉
    syu5=[]#食べ物を貰った時の感謝
    syu6=[]#飲み物を貰った時の感謝
    syu7=[]#良い言葉
    syu8=[]#なでるとき
    syu9=[]#ハグする時
    syu10=[]#だっこするとき
    syu11=[]#キスする時
    syu12=[]#触れ合うとき
    syu13=[]#内容？
    syu14=[]#会話を終わらせられる言葉
    syu15=[]#あいさつ

    Hensin=[]#生物が言った言葉の要素番号の行に、返信された言葉の要素番号を追加していく
    DameHensin=[]#生物が言った言葉の要素番号の行に、その言葉に対して言ってはいけない言葉の要素番号を追加していく
	 
	#食べ物についての領域
    tabemono= []
    Thindo=[]
    Tmanpukudo=[]
	 
	#飲物についての領域
	 
    nomimono =[]
    Nhindo=[]
    Uruoido=[]

    kiokuKotoba=''
    kiokuSkotoba=''
    
    
    def Henji(self,nenrei,code):

        if code==0:#生物クリックの返事

            self.kiokuSkotoba=self.SeibutuClickHenji(nenrei)

            return self.kiokuSkotoba

        elif code==1:#話しかける１の返事

           self.kiokuSkotoba=self.HanasikakeruHenji(nenrei)

           return self.kiokuSkotoba

        elif code==2:#食べさせる２の返事

            self.kiokuSkotoba=self.TabesaseruHenji(nenrei)

            return self.kiokuSkotoba

        elif code==3:#飲ませる3の返事

            self.kiokuSkotoba=self.NomaseruHenji(nenrei)

            return self.kiokuSkotoba

        elif code>=8 and code<=11:#触れ合うときの返事

            self.kiokuSkotoba=self.HureauHenji(nenrei,code)

            return self.kiokuSkotoba


    def KaiwaHenji(self,count):

        self.kiokuSkotoba=self.KaiwaHenjiSyori(count)

        return self.kiokuSkotoba
    
    def eventbetuKotoba(self,code):

        if code==0:#話すイベント
            
            num=self.syuruicodeRandom(0)

            self.kiokuSkotoba=self.kotoba[num]#生物が言う言葉キャッシュに保存

            return self.kiokuSkotoba

        elif code==2:#食べ物イベント

            if self.syuruicodecount(2)>0:

                self.kiokuSkotoba=self.kotoba[self.syuruicodeRandom(2)]#生物が言う言葉キャッシュに保存

                return self.kiokuSkotoba

            else:
                self.kiokuSkotoba=self.kotoba[self.syuruicodeRandom(4)]#生物が言う言葉キャッシュに保存

                return self.kiokuSkotoba

        elif code==3:#飲み物イベント

            if self.syuruicodecount(3)>0:

                self.kiokuSkotoba=self.kotoba[self.syuruicodeRandom(3)]#生物が言う言葉キャッシュに保存

                return self.kiokuSkotoba

            else:

                self.kiokuSkotoba=self.kotoba[self.syuruicodeRandom(4)]#生物が言う言葉キャッシュに保存

                return self.kiokuSkotoba
        

    def SeibutuClickHenji(self,nenrei):#生物をクリックしたとき生物の返事　返す

        if nenrei<5:

            return self.BabyHenji(self.kiokuKotoba,nenrei)
        
        else:
            
            return self.kotoba[self.hairetuck.HairetuRandom(self.kotoba)]

    def HanasikakeruHenji(self,nenrei):#話しかけたとき生物の返事　返す

        if nenrei<5:

            return self.BabyHenji(self.kiokuKotoba,nenrei)

        elif nenrei==5:

            return self.kotoba[self.syuruicodeRandom(13)]

        else:

            retu=self.hairetuck.HairetuSoeji(self.kotoba,self.kiokuKotoba)#返信ネットの使用する列番号

            hairetu=self.Hensin[retu]#言われた言葉に対応するHensinの列（配列）が入る

        
            if not retu==999 and len(hairetu)>0:#プレイヤーが入力した言葉に対して、返事配列に１つでも格納されてたら

                
                num=self.Hensin[retu][self.hairetuck.HairetuRandom(hairetu)]#返信する言葉のkotobaの添え字
                
                return self.kotoba[num]
            else:

                Damehairetu=self.DameHensin[retu]#言われた言葉に対応するHensinの列（配列）が入る

                if not retu==999 and len(Damehairetu)>0:#プレイヤーが入力した言葉に対して、ダメ返事配列に１つでも格納されてたら

                    soeji,hantei=self.SyuruiOKCheck(13,Damehairetu)#syuruicode13　かつ　Damehairetuにない　kotoba配列の添え字　＆　判定

                    if hantei==True:#見つかったら

                        return self.kotoba[soeji]
                    else:

                        soeji,hantei=self.SyuruiIgaiOKCheck(0,Damehairetu)#syuruicode0　ではない　かつ　Damehairetuにない　kotoba配列の添え字　＆　判定

                        if hantei==True:

                            return self.kotoba[soeji]
                        else:

                            return self.kotoba[self.hairetuck.SoreigaiRandom(self.kotoba,Damehairetu)]
                else:

                    return self.kotoba[self.syuruicodeRandom(13)]
    
    def KaiwaHenjiSyori(self,count):#会話のとき生物の返事　返す

        retu=self.hairetuck.HairetuSoeji(self.kotoba,self.kiokuKotoba)#返信ネットの使用する列番号

        hairetu=self.Hensin[retu]#言われた言葉に対応するHensinの列（配列）が入る

        #あいさつしあってた時の処理
        if count != 0 and self.syuruiCheck(15,self.kiokuKotoba)==True and self.syuruiCheck(15,self.kiokuSkotoba)==True:#あいさつしあってたら、
            print('挨拶同士')
            #あいさついがい　の　０
            aisatuhairetu=self.getSyuruicodeHairetu(15)
            soeji,hantei=self.SyuruiOKCheck(0,aisatuhairetu)#0　かつ　aisatuhairetu以外の添え字　と　判定

            if hantei==True:#0番で、15番以外のモノが見つかったら

                return self.kotoba[soeji]
            else:#見つからなかったら
                
                return self.kotoba[self.hairetuck.SoreigaiRandom(self.kotoba,aisatuhairetu)]#aisatuhairetu以外の言葉

        #返事がある場合
        elif not retu==999 and len(hairetu)>0:#プレイヤーが入力した言葉に対して、返事配列に１つでも格納されてたら

            num=self.Hensin[retu][self.hairetuck.HairetuRandom(hairetu)]#返信する言葉のkotobaの添え字
                    
            return self.kotoba[num]
            
        else:

            Damehairetu=self.DameHensin[retu]#言われた言葉に対応するHensinの列（配列）が入る

            if not retu==999 and len(Damehairetu)>0:#プレイヤーが入力した言葉に対して、ダメ返事配列に１つでも格納されてたら

                soeji,hantei=self.SyuruiOKCheck(13,Damehairetu)#syuruicode13　かつ　Damehairetuにない　kotoba配列の添え字　＆　判定

                if hantei==True:#見つかったら

                    return self.kotoba[soeji]
                else:

                    soeji,hantei=self.SyuruiIgaiOKCheck(0,Damehairetu)#syuruicode0　ではない　かつ　Damehairetuにない　kotoba配列の添え字　＆　判定

                    if hantei==True:

                        return self.kotoba[soeji]
                    else:

                        return self.kotoba[self.hairetuck.SoreigaiRandom(self.kotoba,Damehairetu)]
            else:
                #かつ１３　次プレ０➡　kiokuskotobaは会話終了できる言葉？
                return self.kotoba[self.syuruicodeRandom(13)]

    def HenjiHanteiSyori(self,radio) :#言った人：プレイやー　返事した人：生物 
        
        itta=''
        henzi=''

        itta=self.kiokuKotoba
        henzi=self.kiokuSkotoba

        if radio == 1:#合ってる

            self.HensinKousin(itta,henzi)#kotobaが今回生物が言った言葉に対する返事として、Hensin　更新
            #種類コード更新処理
            self.syuruicodeKousin1(henzi,13)#syuruicode0追加#13:内容？
            #種類コード更新処理
            self.syuruicodeKousin1(henzi,15)#syuruicode0追加#15:あいさつ

        else:#ダメ
            self.DameHensinKousin(itta,henzi)  

    def TabesaseruHenji(self,nenrei):#食べさせたとき生物の返事　返す

        if nenrei<5:
            return self.BabyHenji(self.kiokuKotoba,nenrei)
        
        elif nenrei==5:
            return self.kotoba[self.syuruicodeRandom(2)]

        else:
            if self.syuruicodecount(5)>0:

                return self.kotoba[self.syuruicodeRandom(5)]

            elif self.syuruicodecount(1)>0:

                return self.kotoba[self.syuruicodeRandom(1)]

            else:
                return self.kotoba[self.syuruicodeRandom(0)]

    def NomaseruHenji(self,nenrei):#飲ませたとき生物の返事　返す

        if nenrei<5:

            return self.BabyHenji(self.kiokuKotoba,nenrei)
        
        elif nenrei==5:

            return self.kotoba[self.syuruicodeRandom(3)]

        else:

            print(self.syuruicodecount(1))
            if self.syuruicodecount(6)>0:

                return self.kotoba[self.syuruicodeRandom(6)]

            elif self.syuruicodecount(1)>0:
                return self.kotoba[self.syuruicodeRandom(1)]

            else:
                return self.kotoba[self.syuruicodeRandom(0)]
    
    def HureauHenji(self,nenrei,code):#ふれあったとき生物の返事　返す

        if nenrei<5:
            return self.BabyHenji(self.kiokuKotoba,nenrei)
        
        elif nenrei==5:
            return self.kotoba[self.syuruicodeRandom(code)]

        else:
            if self.syuruicodecount(code)>0:

                return self.kotoba[self.syuruicodeRandom(code)]

            elif self.syuruicodecount(12)>0:
                return self.kotoba[self.syuruicodeRandom(12)]

            else:
                return self.kotoba[self.syuruicodeRandom(0)]
    
    def BabyHenji(self,kotoba,nenrei):#生まれたばかりの生物の返事　返す

        if len(self.kotoba)==0:

            return'・・・。'

        if kotoba=='':

            kotoba=self.kotoba[self.hairetuck.HairetuRandom(self.kotoba)]

        if nenrei==0:

            return '・・・。'

        elif nenrei==1:

            if len(kotoba)>1 :

                return self.kana.BoinHenkan(kotoba[0:2])

            else:

                return self.kana.BoinHenkan(kotoba[0])

        elif nenrei==2:

            if len(kotoba)<6 :

                return self.kana.BoinHenkan(kotoba[0:5])
                
            else:
                return self.kana.BoinHenkan(kotoba[0:len(kotoba)])  

        elif nenrei==3:
            return self.kana.BoinHenkan(kotoba) 

        elif nenrei==4:

            return kotoba
    
    #生物が返信するための配列Hensin更新
    def HensinTuika(self):
    
        memori1=[]
        memori2=[]
        self.Hensin.append(memori1)
        self.DameHensin.append(memori2)
    
    def HensinKousin(self,ittaKotoba,kaesitaKotoba):#返事することばに更新

         #kotoba配列の添え字

        ittaSoeji=self.hairetuck.HairetuSoeji(self.kotoba,ittaKotoba)#最初に言ったことばのkotoba配列に対応する添え字

        kaesitaSoeji=self.hairetuck.HairetuSoeji(self.kotoba,kaesitaKotoba)#返事のことばのkotoba配列に対応する添え字

        ittaHairetu=self.Hensin[ittaSoeji]   #最初に言ったことばに対応する返信配列

        if self.hairetuck.HairetuCheck(ittaHairetu,kaesitaSoeji)==False:# ittaHairetu にkaesitaSoeji がなかったら

            self.Hensin[ittaSoeji].append(kaesitaSoeji)#Hensin更新



    def DameHensinKousin(self,ittaKotoba,kaesitaKotoba):#返事することばに更新


         #kotoba配列の添え字

        ittaSoeji=self.hairetuck.HairetuSoeji(self.kotoba,ittaKotoba)#最初に言ったことばのkotoba配列に対応する添え字

        kaesitaSoeji=self.hairetuck.HairetuSoeji(self.kotoba,kaesitaKotoba)#返事のことばのkotoba配列に対応する添え字)

        ittaHairetu=self.DameHensin[ittaSoeji]   #最初に言ったことばに対応するだめ返信配列

        if self.hairetuck.HairetuCheck(ittaHairetu,kaesitaSoeji)==False:# ittaHairetu にkaesitaSoeji がなかったら

            self.DameHensin[ittaSoeji].append(kaesitaSoeji)#Hensin更新
    
    #syuruicode配列更新
    def syuruiTuika(self,code):
    
        memori=[]
        memori.append(code)
        self.syuruicode.append(memori)

    def syuruicodeRandom(self,x):#指定した種類コードのなかからランダムに選ぶ なかったらてきとー

        hairetu=self.getSyuruicodeHairetu(x)

        if len(hairetu)>0:
            i=random.randint(0,len(hairetu)-1)
            
            return hairetu[i]
        else:
            i=random.randint(0,len(self.kotoba)-1)
            
            return i
    
    def SyuruiOKCheck(self,code,Damehairetu):#指定した種類コードの配列の番号で、ダメ返信じゃないやつを返す & 見つかった：True ない：False

        syuhairetu=self.getSyuruicodeHairetu(code)#指定したcode番号のsyuruicodeの配列

        for i in range(len(syuhairetu)):

            for j in range(len(Damehairetu)):

                if syuhairetu[i]==Damehairetu[j]:

                    break
                elif j==len(Damehairetu)-1:

                    return syuhairetu[i],True
        
        return 999,False
    
    def SyuruiIgaiOKCheck(self,code,Damehairetu):#指定した種類コード以外で、ダメ返信じゃないやつを返す & 見つかった：True ない：False

        syuhairetu=self.getSyuruicodeHairetu(code)

        OKsyuhairetu=self.hairetuck.SoreigaiHairetu(self.kotoba,syuhairetu)

        for i in range(len(OKsyuhairetu)):

            for j in range(len(Damehairetu)):

                if OKsyuhairetu[i]==Damehairetu[j]:

                    break
                elif j==len(Damehairetu)-1:

                    return OKsyuhairetu[i],True
        
        return 999,False


        



    
    def syuruicodecount(self,x):#指定した種類コードの数を数える

        hairetu=self.getSyuruicodeHairetu(x)
        count=len(hairetu)

        '''count=0
        for i in range(len(hairetu)):

            if hairetu[i]==x:
                count+=1'''
                
        return count
    
    #指定した種類コードの配列を返す
    def getSyuruicodeHairetu(self,code):

        if code<10:

            if code==0:
                return self.syu0
            elif code==1:
                return self.syu1
            elif code==2:
                return self.syu2
            elif code==3:
                return self.syu3
            elif code==4:
                return self.syu4
            elif code==5:
                return self.syu5
            elif code==6:
                return self.syu6
            elif code==7:
                return self.syu7
            elif code==8:
                return self.syu8
            else : #code==9
                return self.syu9
        else :#code<20
            if code==10:
                return self.syu10
            elif code==11:
                return self.syu11
            elif code==12:
                return self.syu12
            elif code==13:
                return self.syu13
            elif code==14:
                return self.syu14
            else: #code==15:
                return self.syu15
            
    
    #指定した種類コードの配列にデータ保存
    def setSyuruicodeHairetu(self,code,data):

        if code<10:

            if code==0:
                self.syu0.append(data)
            elif code==1:
                self.syu1.append(data)
            elif code==2:
                self.syu2.append(data)
            elif code==3:
                self.syu3.append(data)
            elif code==4:
                self.syu4.append(data)
            elif code==5:
                self.syu5.append(data)
            elif code==6:
                self.syu6.append(data)
            elif code==7:
                self.syu7.append(data)
            elif code==8:
                self.syu8.append(data)
            else : #code==9
                self.syu9.append(data)
        else :#code<20
            if code==10:
                self.syu10.append(data)
            elif code==11:
                self.syu11.append(data)
            elif code==12:
                self.syu12.append(data)
            elif code==13: #code==13:
                self.syu13.append(data)
            elif code==14:
                self.syu14.append(data)
            else:
                self.syu15.append(data)
    
    #指定した種類コードの配列にprint
    def printSyuruicodeHairetu(self,code):

        if code<10:

            if code==0:
                print(self.syu0)
            elif code==1:
                print(self.syu1)
            elif code==2:
                print(self.syu2)
            elif code==3:
                print(self.syu3)
            elif code==4:
                print(self.syu4)
            elif code==5:
                print(self.syu5)
            elif code==6:
                print(self.syu6)
            elif code==7:
                print(self.syu7)
            elif code==8:
                print(self.syu8)
            else : #code==9
                print(self.syu9)
        else :#code<20
            if code==10:
                print(self.syu10)
            elif code==11:
                print(self.syu11)
            elif code==12:
                print(self.syu12)
            elif code==13: #code==13:
                print(self.syu13)
            elif code==14:
                print(self.syu14)
            elif code==15:
                print(self.syu15)
            


    #syuruicode,syuを更新する時

    def syuruicodeKousin1(self,kotoba,tuikaCode):

        kotobaSoeji=self.hairetuck.HairetuSoeji(self.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

        #今回の言葉に対応する種類コード配列
        syuhairetu=self.syuruicode[kotobaSoeji]

        if self.syuruiKousinOkCheck(tuikaCode,syuhairetu)==True:#更新してオッケーだったら

            if self.hairetuck.HairetuCheck(syuhairetu,tuikaCode)==False:#今回入力した言葉に対する種類コード配列に今回の種類コードがなかったら

                    self.setSyuruicodeHairetu(tuikaCode,kotobaSoeji)#syuに追加

                    self.syuruicode[kotobaSoeji].append(tuikaCode)#syuruicode追加


    def syuruiCheck(self,code,kotoba):#kotobaは、種類コードcode番　だったら　True

        kotobaSoeji=self.hairetuck.HairetuSoeji(self.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字
        print('kotobaSoeji')
        print(kotobaSoeji)

        #今回入力した言葉に対応する種類コード配列
        syuhairetu=self.syuruicode[kotobaSoeji]

        return self.hairetuck.HairetuCheck(syuhairetu,code)
        
    
    def syuruiKousinOkCheck(self,code,syuhairetu):#更新してよかったらTrue だめならFalse

        hantei=True

        if code==13:#13更新したいとき

            if self.hairetuck.HairetuCheck(syuhairetu,0)==True:#0はあるかどうか

                hantei=False
            else:
                hantei=True
        
        elif code==15:#挨拶更新したいとき

            if self.kiokuKotoba==self.kiokuSkotoba and True==self.hairetuck.HairetuCheck(syuhairetu,0):#プレイヤーが言った言葉と生物が言った言葉が同じ　かつ　種類コードが0　のとき
                
                hantei=True
            else:
                hantei=False

        return hantei #false 更新しちゃダメ　true おっけー
    
    def syuruicodeKousin2(self,kotoba,joukenCode,tuikaCode):

        kotobaSoeji=self.hairetuck.HairetuSoeji(self.kotoba,kotoba)#kotobaのkotoba配列に対応する添え字

        #今回入力した言葉に対応する種類コード配列
        syuhairetu=self.syuruicode[kotobaSoeji]

        if self.hairetuck.HairetuCheck(syuhairetu,joukenCode)==True and self.hairetuck.HairetuCheck(syuhairetu,tuikaCode)==False:#

            self.setSyuruicodeHairetu(tuikaCode,kotobaSoeji)#syuに追加
            self.syuruicode[kotobaSoeji].append(tuikaCode)#syuruicode追加
    
    #eventの会話から考えて種類コード更新
    
    def syuruicodeGyakuKousin(self,kotoba,joukenCode,tuikaCode):

        #kotoba配列の添え字

        ittaSoeji=self.hairetuck.HairetuSoeji(self.kotoba,self.kiokuSkotoba)#最初に言ったことばのkotoba配列に対応する添え字

        kaesitaSoeji=self.hairetuck.HairetuSoeji(self.kotoba,kotoba)#返事のことばのkotoba配列に対応する添え字

        #種類コード配列
        ittaHairetu=self.syuruicode[ittaSoeji]#返事のことばに対応するsyurui配列

        kaesitaHairetu=self.syuruicode[kaesitaSoeji]#返事のことばに対応するsyurui配列

        if self.hairetuck.HairetuCheck(kaesitaHairetu,joukenCode)==True and self.hairetuck.HairetuCheck(ittaHairetu,tuikaCode)==False:#例：返事のことばの種類コードに、１（感謝）があったら、　言った言葉は　４（感謝される言葉）ということ

            self.setSyuruicodeHairetu(tuikaCode,ittaSoeji)#syuに追加
            self.syuruicode[ittaSoeji].append(tuikaCode)#syuruicode追加





    #セーブ    
    def save(self,code):
        print('\nKotobaKanriセーブ')

        #kotobaセーブ
        savekotoba=[]
        for i in range(len(self.kotoba)) :
            savekotoba.append(self.kotoba[i]+'\n')

        print('\nkotoba[]セーブ')
        print(savekotoba)

        f=open('./file/save'+str(code)+'/KotobaKanri/kotoba.txt','w',encoding='utf-8')
        f.writelines(savekotoba)
        f.close()


        #hindoセーブ
        savehindo=[]
        for i in range(len(self.hindo)) :
            savehindo.append(str(self.hindo[i])+'\n')

        print('\nhindo[]セーブ')
        print(savehindo)

        f=open('./file/save'+str(code)+'/KotobaKanri/hindo.txt','w',encoding='utf-8')
        f.writelines(savehindo)
        f.close()

        #syuruicodeセーブ
        savesyuruicode=[]
        for i in range(len(self.syuruicode)) :

            gyou=self.syuruicode[i]
            
            for j in range(len(gyou)):
                savesyuruicode.append(str(self.syuruicode[i][j])+'\n')
            
            print(savesyuruicode)
            
            savesyuruicode.append('a\n')

        print('\nsyuruicode[]セーブ')
        print(savesyuruicode)    

        f=open('./file/save'+str(code)+'/KotobaKanri/syuruicode.txt','w',encoding='utf-8')
        f.writelines(savesyuruicode)
        f.close()

        #syuセーブ
        savesyu=[]
        for i in range(16) :#syu[]は１４種類ある

            gyou=self.getSyuruicodeHairetu(i)
            
            for j in range(len(gyou)):
                savesyu.append(str(gyou[j])+'\n')
            
            print(savesyu)
            
            savesyu.append('a\n')

        print('\nsyu[]セーブ')
        print(savesyu)    

        f=open('./file/save'+str(code)+'/KotobaKanri/syu.txt','w',encoding='utf-8')
        f.writelines(savesyu)
        f.close()

        #Hensinセーブ
        saveHensin=[]
        for i in range(len(self.Hensin)) :

            gyou=self.Hensin[i]
            
            for j in range(len(gyou)):
                saveHensin.append(str(self.Hensin[i][j])+'\n')
            
            
            saveHensin.append('a\n')

        print('\nHensin[]セーブ')
        print(saveHensin)    

        f=open('./file/save'+str(code)+'/KotobaKanri/Hensin.txt','w',encoding='utf-8')
        f.writelines(saveHensin)
        f.close()
        
    #DameHensinセーブ
        saveDameHensin=[]
        for i in range(len(self.DameHensin)) :

            gyou=self.DameHensin[i]
            
            for j in range(len(gyou)):
                saveDameHensin.append(str(self.DameHensin[i][j])+'\n')
            
            
            saveDameHensin.append('a\n')

        print('\nDameHensin[]セーブ')
        print(saveDameHensin)    

        f=open('./file/save'+str(code)+'/KotobaKanri/DameHensin.txt','w',encoding='utf-8')
        f.writelines(saveDameHensin)
        f.close()

        #tabemonoセーブ

        savetabemono=[]
        for i in range(len(self.tabemono)) :
            savetabemono.append(self.tabemono[i]+'\n')

        print('\ntabemonoセーブ')
        f=open('./file/save'+str(code)+'/KotobaKanri/tabemono.txt','w',encoding='utf-8')
        f.writelines(savetabemono)
        f.close()   

        #Thindoセーブ
        saveThindo=[]
        for i in range(len(self.Thindo)) :
            saveThindo.append(str(self.Thindo[i])+'\n')
        
        print('\nThindoセーブ')
        f=open('./file/save'+str(code)+'/KotobaKanri/Thindo.txt','w',encoding='utf-8')
        f.writelines(saveThindo)
        f.close()

        #Tmanpukudoセーブ
        saveTmanpukudo=[]
        for i in range(len(self.Tmanpukudo)) :
            saveTmanpukudo.append(str(self.Tmanpukudo[i])+'\n')
        
        print('\nTmanpukudoセーブ')
        f=open('./file/save'+str(code)+'/KotobaKanri/Tmanpukudo.txt','w',encoding='utf-8')
        f.writelines(saveTmanpukudo)
        f.close()
        
        #nomimonoセーブ
        
        savenomimono=[]
        for i in range(len(self.nomimono)) :
            savenomimono.append(self.nomimono[i]+'\n')
        
        print('\nnomimonoセーブ')
        f=open('./file/save'+str(code)+'/KotobaKanri/nomimono.txt','w',encoding='utf-8')
        f.writelines(savenomimono)
        f.close()

        #Nhindoセーブ
        saveNhindo=[]
        for i in range(len(self.Nhindo)) :
            saveNhindo.append(str(self.Nhindo[i])+'\n')

        print('\nNhindoセーブ')
        f=open('./file/save'+str(code)+'/KotobaKanri/Nhindo.txt','w',encoding='utf-8')
        f.writelines(saveNhindo)
        f.close()

        #Uruoidoセーブ
        saveUruoido=[]
        for i in range(len(self.Uruoido)) :
            saveUruoido.append(str(self.Uruoido[i])+'\n')

        print('\nUruoidoセーブ')
        f=open('./file/save'+str(code)+'/KotobaKanri/Uruoido.txt','w',encoding='utf-8')
        f.writelines(saveUruoido)
        f.close()


        #KotobaKanriセーブ
        data=[]
        data.append(self.kiokuKotoba+'\n')
        data.append(self.kiokuSkotoba+'\n')

        print('\nKotobaKanriセーブ')

        print(data)

        f=open('./file/save'+str(code)+'/KotobaKanri/KotobaKanri.txt','w',encoding='utf-8')
        f.writelines(data)
        f.close()
    
    def crea(self,code):

        print('\nKotobaKanriクリア')

        print('\nkotoba[]クリア')

        f=open('./file/save'+str(code)+'/KotobaKanri/kotoba.txt','w',encoding='utf-8')
        f.close()

        print('\nhindo[]クリア')

        f=open('./file/save'+str(code)+'/KotobaKanri/hindo.txt','w',encoding='utf-8')
        f.close()

        #syuruicodeクリア

        print('\nsyuruicode[]クリア')   

        f=open('./file/save'+str(code)+'/KotobaKanri/syuruicode.txt','w',encoding='utf-8')
        f.close()

        #syuクリア

        print('\nsyu[]クリア')    

        f=open('./file/save'+str(code)+'/KotobaKanri/syu.txt','w',encoding='utf-8')
        f.close()

        #Hensinクリア

        print('\nHensin[]クリア')    

        f=open('./file/save'+str(code)+'/KotobaKanri/Hensin.txt','w',encoding='utf-8')
        f.close()
        
    #DameHensinクリア

        print('\nDameHensin[]クリア')    

        f=open('./file/save'+str(code)+'/KotobaKanri/DameHensin.txt','w',encoding='utf-8')
        f.close()

        #tabemonoクリア

        print('\ntabemonoクリア')

        f=open('./file/save'+str(code)+'/KotobaKanri/tabemono.txt','w',encoding='utf-8')
        f.close()   

        #Thindoクリア
        
        print('\nThindoクリア')

        f=open('./file/save'+str(code)+'/KotobaKanri/Thindo.txt','w',encoding='utf-8')
        f.close()

        #Tmanpukudoクリア
        
        print('\nTmanpukudoクリア')

        f=open('./file/save'+str(code)+'/KotobaKanri/Tmanpukudo.txt','w',encoding='utf-8')
        f.close()
        
        #nomimonoクリア
        
        print('\nnomimonoクリア')

        f=open('./file/save'+str(code)+'/KotobaKanri/nomimono.txt','w',encoding='utf-8')
        f.close()

        #Nhindoクリア

        print('\nNhindoクリア')

        f=open('./file/save'+str(code)+'/KotobaKanri/Nhindo.txt','w',encoding='utf-8')
        f.close()

        #Uruoidoクリア

        print('\nUruoidoクリア')

        f=open('./file/save'+str(code)+'/KotobaKanri/Uruoido.txt','w',encoding='utf-8')
        f.close()


        #KotobaKanriクリア
        print('\nKotobaKanriクリア')

        f=open('./file/save'+str(code)+'/KotobaKanri/KotobaKanri.txt','w',encoding='utf-8')
        f.close()


    def load(self,code):
        self.syokika()

        #普通の言葉についての領域
        with open('./file/save'+str(code)+'/KotobaKanri/kotoba.txt','r',encoding='utf-8')as f:
            self.kotoba=f.read().split("\n")
            self.kotoba.remove('')

            print("kotobaロード")
            print(self.kotoba)
            

        with open('./file/save'+str(code)+'/KotobaKanri/hindo.txt','r',encoding='utf-8')as f:
            data=[]
            data=f.read().split("\n")
           
            for i in range(len(data)):
                if not data[i]=='':
                    self.hindo.append(int(data[i]))

            print("hindoロード")
            print(self.hindo)

        
        with open('./file/save'+str(code)+'/KotobaKanri/syuruicode.txt','r',encoding='utf-8')as f:

            data=[]
            data=f.read().split("\n")

            self.syuruicode.append([])
            j=0
            for i in range(len(data)):
                
                if data[i]=='a':
                    if not data[i+1]=='':
                        self.syuruicode.append([])
                        j+=1

                elif not data[i]=='':
                    self.syuruicode[j].append(int(data[i]))

                #if i==len(data)-1:
                    #self.Hensin.append(gyou)

            print('ロードsyuruicode')
            print(self.syuruicode)
        
        with open('./file/save'+str(code)+'/KotobaKanri/syu.txt','r',encoding='utf-8')as f:

            data=[]
            data=f.read().split("\n")

            j=0
            for i in range(len(data)):
                
                if data[i]=='a':
                    if not data[i+1]=='':
                        j+=1

                elif not data[i]=='':
                    self.setSyuruicodeHairetu(j,int(data[i]))

                #if i==len(data)-1:
                    #self.Hensin.append(gyou)

            print('ロードsyu')
            for i in range(16):
                print(i,end=' ')
                self.printSyuruicodeHairetu(i)
                        
        with open('./file/save'+str(code)+'/KotobaKanri/Hensin.txt','r',encoding='utf-8')as f:

            data=[]
            data=f.read().split("\n")

            self.Hensin.append([])
            j=0
            for i in range(len(data)):
                
                if data[i]=='a':
                    if not data[i+1]=='':
                        self.Hensin.append([])
                        j+=1

                elif not data[i]=='':
                    self.Hensin[j].append(int(data[i]))

                #if i==len(data)-1:
                    #self.Hensin.append(gyou)

            print('ロードHensin')
            print(self.Hensin)

        with open('./file/save'+str(code)+'/KotobaKanri/DameHensin.txt','r',encoding='utf-8')as f:

                data=[]
                data=f.read().split("\n")

                self.DameHensin.append([])
                j=0
                for i in range(len(data)):
                    
                    if data[i]=='a':
                        if not data[i+1]=='':
                            self.DameHensin.append([])
                            j+=1

                    elif not data[i]=='':
                        self.DameHensin[j].append(int(data[i]))

                    #if i==len(data)-1:
                        #self.Hensin.append(gyou)

                print('ロードDameHensin')
                print(self.DameHensin)

        with open('./file/save'+str(code)+'/KotobaKanri/tabemono.txt','r',encoding='utf-8')as f:
            self.tabemono=f.read().split("\n")
            self.tabemono.remove('')

            print("tabemonoロード")
            print(self.tabemono)

        with open('./file/save'+str(code)+'/KotobaKanri/Thindo.txt','r',encoding='utf-8')as f:
            data=[]
            data=f.read().split("\n")

            for i in range(len(data)):
                if not data[i]=='':
                    self.Thindo.append(int(data[i]))

            print("Thindoロード")
            print(self.Thindo)
            
        with open('./file/save'+str(code)+'/KotobaKanri/Tmanpukudo.txt','r',encoding='utf-8')as f:
            data=[]
            data=f.read().split("\n")

            for i in range(len(data)):
                if not data[i]=='':
                    self.Tmanpukudo.append(int(data[i]))

            print("Tmanpukudoロード")
            print(self.Tmanpukudo)

        with open('./file/save'+str(code)+'/KotobaKanri/nomimono.txt','r',encoding='utf-8')as f:
            self.nomimono=f.read().split("\n")
            self.nomimono.remove('')

            print("nomimonoロード")
            print(self.nomimono)

        with open('./file/save'+str(code)+'/KotobaKanri/Nhindo.txt','r',encoding='utf-8')as f:
            data=[]
            data=f.read().split("\n")
            for i in range(len(data)):
                if not data[i]=='':
                    self.Nhindo.append(int(data[i]))

            print("Nhindoロード")
            print(self.Nhindo)            

        with open('./file/save'+str(code)+'/KotobaKanri/Uruoido.txt','r',encoding='utf-8')as f:
            data=[]
            data=f.read().split("\n")
            for i in range(len(data)):
                if not data[i]=='':
                    self.Uruoido.append(int(data[i]))

            print("Uruoidoロード")
            print(self.Uruoido)
        
        with open('./file/save'+str(code)+'/KotobaKanri/KotobaKanri.txt','r',encoding='utf-8')as f:
            data=[]
            data=f.read().split("\n")

            print("KotobaKanriロード")
            print(data)
            
            self.kiokuKotoba=data[0]#kiokukotoba
            self.kiokuSkotoba=data[1]


	#１話しかけるのときの返事
    def syokika(self):
        #普通の言葉についての領域

        del self.kotoba[:]
        del self.hindo[:]
        del self.syuruicode[:]  #0=不明,1=感謝,2=食べさせるとき,3=飲ませるとき,4=ものを上げるとき（食べさせる飲ませるどっちもの場合）

        del self.syu0[:]
        del self.syu1[:]
        del self.syu2[:]
        del self.syu3[:]
        del self.syu4[:]
        del self.syu5[:]
        del self.syu6[:]
        del self.syu7[:]
        del self.syu8[:]
        del self.syu9[:]
        del self.syu10[:]
        del self.syu11[:]
        del self.syu12[:]
        del self.syu13[:]
        del self.syu14[:]
        del self.syu15[:]

        del self.Hensin[:]#生物が言った言葉の要素番号の行に、返信された言葉の要素番号を追加していく
        del self.DameHensin[:]
		
		#食べ物についての領域
        del self.tabemono[:]
        del self.Thindo[:]
        del self.Tmanpukudo[:]
		
		#飲物についての領域
		
        del self.nomimono[:]
        del self.Nhindo[:]
        del self.Uruoido[:]	

        #self.Uruoido[:]=[]	


		