class Product:
    def __init__(self,id=None,name=None,quantity=None,price=None,cateid=None):
        self.id=id
        self.name=name
        self.quantity=quantity
        self.price=price
        self.cateid=cateid
    def __str__(self):
        #info="{:<{}} \t {:<{}} \t {:>{}} \t {:>{}}".format(self.id,self.name,self.quantity,self.price)
        info = f"{self.id}\t{self.name: <10}\t{self.quantity: >2}\t{self.price:>5}" #\t ==> dữ liệu cách nhau 0.5 inches
        return info