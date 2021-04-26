class Variable:
    def __init__(self, v):
        self.v=v
        self.command=None
    def set(self, v):
        self.v=v
        if self.command!=None:
            self.command()
    def get(self):
        return self.v
    def trace(self, command):
        self.command=command

x=Variable(0)

def money():
    amount="{:.2f}".format(x.get())
    print("You have $"+amount+".")

x.trace(money)

x.set(8.00)
x.set(16.00)