class Avto:
    __num_avto=0
    def __init__(self,make,model,rang,yil,narh):
        "Avtomobile xususiyatlari!"
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narh=narh
        Avto.__num_avto+=1
    #def __str__(self):
       # pass #f'make: {self.make},model: {self.model},rang: {self.rang},yil: {self.yil},narh: {self.narh}'
    def __repr__(self):
        return f"{self.make} : {self.model}"
    def __eq__(self,y):
        return self.narh==y.narh
    def __lt__(self,y):
        return self.narh<y.narh
    def __le__(self,y):
        return self.narh<=y.narh


Car1=Avto("GM","Cobalt","Zeus",2023,11000)
Car2=Avto("GM","Cobalt","White",2020,9000)
#print(Car1)
#print(Car1==Car2)
#print(Car1<Car2)
#print(Car1<=Car2)

class AvtoSalon:
    def __init__(self,name):
        "Avtomobile xususiyatlari!"
        self.name=name
        self.avtolar=[]
    def __repr__(self):
        return f"{self.name} AvtoSaloni!"
    def __getitem__(self,index):
        return self.avtolar[index]
    def __setitem__(self,index,qiymat):
        self.avtolar[index]=qiymat
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Xato")


salon1=AvtoSalon("Norbekov")
Car1=Avto("GM","Cobalt","Zeus",2023,11000)
Car2=Avto("GM","Cobalt","White",2020,9000)
salon1.add_avto(Car1,Car2)
print(salon1[1])
salon1[1]=Avto("GM","Malibu","Zeus",2023,11000)
print(salon1[1])
print(salon1[:])
salon1[0]
