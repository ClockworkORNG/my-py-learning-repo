class Price:
    def __init__(self, itemsList):
        self.productList = itemsList

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if len(self.productList) == 0:
            raise StopIteration

        if self.idx >= len(self.productList):
            raise StopIteration
        price = self.productList[self.idx].split(';')[1].strip()
        self.idx += 1
        return price


items = ["Lenovo A5; 1234", "Lenovo B8; 1485"]
prices = Price(items)
for price in prices:
    print(price)

#итератор:
class Test:
    def __iter__(self):
        self.n = 0
        return(self)

    def __next__(self):
        self.n += 1
        return self.n
p = Test()
for i in p:
    print(i)
    break