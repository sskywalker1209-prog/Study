# Cexm.py

class Cexm:
    def fsam(self):
        print("맴버 함수(매소드)")
    def fsbm(self,pa):
        self.x = pa
        print("맴버변수 x:", self.x)

ca = Cexm()
ca.fsam()
ca.fsbm(10)


cb = Cexm()
cb.fsam()
cb.fsbm(20)


