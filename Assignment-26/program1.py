"""1. Write a python script to multiple 2 or 3 or 4 numbers with a single multiply method in
a class using method overloading."""

class multiple:
    def multi_num(self,a=None,b=None,c=None,d=None):
        
        if a!= None and b!=None and c!=None and d!=None :
            return a*b*c*d
        
        elif a!= None and b!=None and c!=None :
            return a*b*c
        
        elif a!= None and b!=None :
            return a*b
       
        else:
            return "Nothing find"    

obj=multiple()
print(obj.multi_num())
print(obj.multi_num(10,20))
print(obj.multi_num(10,20,30))
print(obj.multi_num(10,20,30,40))

                     