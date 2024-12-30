class Category:
    def __init__(self,id=None,name=None,isdelete=None):
        self.id=id
        self.name=name
        self.isdelete=isdelete
    def __str__(self):
        return f"{self.id}-{self.name}"


