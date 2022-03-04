import random

class KanaCheck():
    # coding: utf-8
    hiragana = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんー"
    katakana = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴー"
    boin     = "ぁあぃいぅうぇえぉおああいいううええおおああいいううええおおああいいぅううええおおあいうえおあああいいいうううえええおおおあいうえおぁあぅうぉおあいうえおぁあうあおんうー"
    hankana = ""
    suuji = "0123456789０１２３４５６７８９"

    # 日本語文字列のソート
    def sort_str(string, reverse=False):
        return "".join(sorted(string, reverse=reverse))

    # ひらがなだけの文字列ならTrue
    def HiraganaCheck(self,strj):
        return all([ch in self.hiragana for ch in strj])

    # カタカナだけの文字列ならTrue
    def iskata(self,strj):
        return all([ch in self.katakana for ch in strj])

    # カタカナ・ひらがなだけの文字列ならTrue
    def iskatahira(self,strj):
        return all([ch in self.katakana or ch in self.hiragana for ch in strj])

    def hiraganaSoeji(self,strj,num):#num番目の文字の添え字返す

        for i in range(len(self.hiragana)):
            if strj[num-1]==self.hiragana[i]:
                return i 
        return 999
    
    def BoinHenkan(self,moziretu):#母音に変換する
        Boin=''
        
        for i in range(len(moziretu)):

            for j in range(len(self.hiragana)):
                if moziretu[i]==self.hiragana[j]:
                    Boin+=self.boin[j]
                    break
                elif j==len(self.hiragana)-1:
                    Boin+=self.hiragana[random.randint(0,len(self.hiragana)-1)]
        
        return Boin

