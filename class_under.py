class korea_univ_mem :
    def __init__(self, high_Sch, region):
        self.high_Sch = high_Sch
        self.region = region
    def printall(self, age):
        print(f"{self.high_Sch}출신 {self.region}출신 {age}세")

seokhee = korea_univ_mem("동암고", "전주")

seokhee.printall(26)
