from class10k.course1.o_2024y_10m_25d.ManagementCustomer.models.TypePhone import TypePhone


class ListCustomer:
    def __init__(self):
        self.customers=[]
    def add_customer(self,c):
        self.customers.append(c)
    def update_customer(self,index,c):
        self.customers[index]=c
    def print_customers(self):
        for c in self.customers:
            print(c)
    def filter_type_customer(self,tc):
        filters=[]
        for c in self.customers:
            if c.tc==tc:
                filters.append(c)
        return filters
    def filter_age_customers(self,min_age,max_age):
        filter=ListCustomer()
        for c in self.customers:
            if c.age>=min_age and c.age<=max_age:
                filter.add_customer(c)
        return filter
    def filter_type_phone_customer(self,tp): #Hàm lọc khách hàng theo nhà mang di động Viettel, MobiFone, Vinaphone
        filter=ListCustomer()
        match (tp):
            case TypePhone.VIETTEL:
                filter=self.filter_viettel_customers()
            case TypePhone.MOBIFONE:
                filter=self.filter_mobifone_customers()
            case TypePhone.VINAPHONE:
                filter=self.filter_vinaphone_customers()
            case _:
                return filter
        return filter
    def filter_viettel_customers(self):
        filter=ListCustomer()
        for c in self.customers:
            if c.phone.startswith("090") or c.phone.startswith("091"):
                filter.add_customer(c)
        return filter
    def filter_mobifone_customers(self):
        filter=ListCustomer()
        for c in self.customers:
            if c.phone.startswith("092") or c.phone.startswith("093"):
                filter.add_customer(c)
        return filter
    def filter_vinaphone_customers(self):
        filter=ListCustomer()
        for c in self.customers:
            if c.phone.startswith("094") or c.phone.startswith("095"):
                filter.add_customer(c)
        return filter
    def sort_customers_desc_by_age(self):
        for i in range (0,len(self.customers)):
            for j in range(i+1,len(self.customers)):
                ci = self.customers[i]
                cj = self.customers[j]
                if ci.age < cj.age:
                    self.customers[i]=cj
                    self.customers[j]=ci
    def findOne(self,id):
        #primitive dataset
        # object
        for c in self.customers:
            if c.id==id:
                return c
        return None
    def remove_customer_by_index(self,index):
        if index<0 or index>=len(self.customers):
            return False
        self.customers.pop(index)

    def remove_customer_by_id(self,id):
        c_remove=self.findOne(id)
        if c_remove==None:
            return False
        self.customers.remove(c_remove)
        return True