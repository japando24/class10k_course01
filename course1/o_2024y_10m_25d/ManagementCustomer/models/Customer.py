class Customer:
    def __init__(self,
                 id=None,
                 name=None,
                 email=None,
                 phone=None,
                 tp=None,
                 age=None,
                 tc=None):
        self.id=id
        self.name = name
        self.email = email
        self.phone = phone
        self.tp = tp
        self.age = age
        self.tc = tc
    def __str__(self):
        msg=f"{self.id}\t{self.name}\t{ self.email: >18}\t{self.phone}\t{self.tp.value}\t{self.age}\t{self.tc.value:>17}"
        return msg
    def get_details(self):
        msg=(f"Id={self.id}\n"
             f"Name={self.name}\n"
             f"Phone={self.phone}\n"
             f"Age={self.age}\n"
             f"Type Customer={self.tc.value}")
        return msg