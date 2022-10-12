class Band:
    instruments=[]
    solos=[]
    instances=[]
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)
        if members==[]:
            return None
        for member in self.members:
            Band.instruments.append(member.get_instrument())
    def play_solos(self):
        for member in self.members:
            Band.solos.append(member.play_solo())
        return Band.solos
    @classmethod
    def to_list(cls):

        return Band.instances

    
from abc import ABCMeta, abstractmethod

class Musician(metaclass=ABCMeta):
    
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def get_instrument(self):
        pass
    @abstractmethod
    def play_solo(self):
        pass
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"



class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name)
    def get_instrument(self):
        return "guitar"
    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name)
    def get_instrument(self):
        return "bass"
    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name)
    def get_instrument(self):
        return "drums"
    def play_solo(self):
        return "rattle boom crash"

