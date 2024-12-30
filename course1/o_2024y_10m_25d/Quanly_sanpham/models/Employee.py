from PyQt6.sip import isdeleted


class Employee:
    def __init__(self,id=None,name=None,username=None,password=None,isdeleted=None):
        self.id=id
        self.name=name
        self.username=username
        self.password=password
        self.isdeleted=isdeleted