class A:
    def __init__(self,val1=None):
        self.val1 = val1
        print(f"class A initialization with value :{self.val1}")

class B:
    def __init__(self,val1=None):
        self.val1 = val1
        print(f"class B initialization with value :{self.val1}")

class E(A,B):
    def __init__(self, *args):
        if len(args == 0):
            super().__init__()
            print("class E object created.")
        elif len(args) == 1:
            super.__init__(args[0])
            print("class E created with with one value")
        else:
            raise ValueError("class E can be created with 0 or 1 argument(s).")
    def show(self):
        if not hasattr(self,'val1'):
            print("showing class E")
        else:
            print(f"showing class E with value {self.val1}")

e1 = E()
e1.show()
e2 = E(10)
e2.show()