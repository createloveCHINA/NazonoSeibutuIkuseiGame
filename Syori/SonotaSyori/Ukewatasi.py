class Ukewatasi():
    s1=''
    s2=''
    s3=''
    p=0
    n1=0
    n2=0
    def setString1(self,s1):

        self.s1=s1

    def setString(self,s2,s3):
        self.s2=s2
        self.s3=s3
    


    def getString1(self):
        s1=self.s1
        self.s1=''
        return s1
    
    def getString2(self):
        s2=self.s2
        s3=self.s3

        self.s2=''
        self.s3=''
        return s2,s3

    def setint(self,n1):
        self.n1=n1

    def getint(self):
        n1=self.n1
        self.n1=0
        return n1

