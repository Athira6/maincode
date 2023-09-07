class cal1:
  def add(self,a,b):
     return a+b
class cal2:
  def sub(self,a,b):
    return a-b
class cal3:
  def multi(self,a,b):
    return a*b
class calculator(cal1,cal2,cal3):
  def div(self,a,b):
    return a/b
d=calculator()
d.add(6,2)
d.sub(4,2)
d.multi(7,2)
d.div(9,6)

