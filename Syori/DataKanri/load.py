import Syori.SeibutuSyori
import Syori.Tarn

class load():

    Seibutu = Syori.SeibutuSyori.SeibutuSyori()
    Tarn=Syori.Tarn.Tarn(Seibutu)

    def __init__(self,insTarn,insSeibutu):

        self.Tarn=insTarn
        self.Seibutu=insSeibutu

    def load(self,code):#指定したcodeのデータをロードする

        self.count=0

        self.Tarn.load(code)
        self.Seibutu.load(code)

