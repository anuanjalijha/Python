class A:
    _a = 10  #protected
    __b = 20 #private
    
    def show(self):
        print("a= ",self._a)
        print("b= ",self.__b)
        
obj = A()
obj.show()
print("Outside of class ",obj._a)
# print("Outside of class ",obj.__b)
