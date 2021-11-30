class Person:
  name:str
  gender:str
  phone:str

  def __init__(self,hoten,gioitinh,sdt) -> None:
    self.hoten = hoten
    self.gioitinh = gioitinh
    self.sdt = sdt

  def outputPerson(self) -> str:
    result = "name: "  + (self.hoten) + ", gender:" + self.gioitinh + ", phone:" + (self.sdt)
    return result


class Student(Person):
  studerID:str
  class1:str

  def __init__(self,hoten,gioitinh,sdt,studerID,class1) -> None:
    Person. __init__(self,hoten,gioitinh,sdt)
    self.studerID = studerID
    self.class1 = class1

  def outputStuder(self) ->str:
    result = self.outputPerson () + ", studerID:" + str(self.studerID) + ", class1:" + (self.class1)
    return result


class Lecturer(Person):
  lecturerID:str
  yersofExperince:str

  def __init__(self,hoten,gioitinh,sdt,leturerid,yersofExperince):
    Person.__init__(self,hoten,gioitinh,sdt)
    self.lecturid = leturerid
    self.yersofExperince = yersofExperince

  def outputLectur(self) -> str:
    result = self.outputPerson () + "lecturerID" + str(self.lecturerID) +"\tyersofExperince:" + (self.yersofExperince)
    return result