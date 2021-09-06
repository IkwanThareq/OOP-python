
class employee :
  name = "ikwan"
  target = 6
  def checkTarget(self) :
    if self.target >= 5 :
      print("Target terpenuhi")
    else:
      print("belum mencapai target")

objEmployee = employee()
print(objEmployee.name)
objEmployee.checkTarget()