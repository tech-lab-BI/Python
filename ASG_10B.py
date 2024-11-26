class B:
    def __init__(self,val1:int):
        self.val1 = val1
        print("class B object created.")
    def show(self):
        print(f"Showing class B object having value {self.val1}")

l = B(10)
l.show()