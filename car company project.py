class cars:
    def company(self):
        
        self.cgst=0.1
        self.sgst=0.1
        self.insurance=100000

        while True:
            print("select a car company mg or tata")
            self.n=input("enter car company")
            if self.n=="mg":
                print("welcome to mg")
                self.model()
                break
            elif self.n=="tata":
                print("welcome to tata")
                self.model()
                break
            else:
                print("select a valid car company")
    def model(self):
        if self.n=="mg":
            while True:
                print("select from hector and gloster")
                self.choice=input("enter tne car name ")
                if self.choice=="hector":
                    self.price(self.choice)
                    break
                elif self.choice=="gloster":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid car name")
        elif self.n=="tata":
            while True:
                print("select from nexon and punch")
                self.choice=input("enter a car name ")
                if self.choice=="nexon":
                    self.price(self.choice)
                    break
                elif self.choice=="punch":
                    self.price(self.choice)
                    break
                else:
                    print("enter valid car name")
    def price(self,choice):

        if choice=="hector":
            self.p=3000000
        elif choice=="gloster":
            self.p=5000000
        elif choice=="nexon":
            self.p=1500000
        elif choice=="punch":
            self.p=1200000


        total=self.p+(self.cgst*self.p)+(self.sgst*self.p)+self.insurance
        print(total)
a=cars()
a.company()