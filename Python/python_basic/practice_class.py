class Unit:
    def __init__(self):
        print("Unit 생성자")
        
class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__() # super 는 다중상속 할때 맨 처음 클래스에서 데이터 뽑아옴. 그래서 필요한게 안 될수 도 있음. 
        Unit.__init__(self)
        Flyable.__init__(self)
        
# 드랍쉽
dropship = FlyableUnit()
