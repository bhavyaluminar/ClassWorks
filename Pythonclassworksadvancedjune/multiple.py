class Hospital:
    def __init__(self):
        self.hos_name=input("Enter Hospital name")
    def show_hospital(self):
        print("Hospital Name",self.hos_name)


class Department:
    def __init__(self):
        self.dept_name=input("Enter Department name")
    def show_department(self):
        print("Department Name",self.dept_name)


class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.name=input("Enter name")
        self.age=int(input("Enter age"))
        self.admission_date=input("Enter admission date")
        self.bed_no=input("Enter the bed number")
        self.discharge_date=""
    def full_summary(self):
        Hospital.show_hospital(self)
        Department.show_department(self)
        print("Patient Info")
        print("Name",self.name)
        print("Age",self.age)
        print("Admission Date",self.admission_date)
        print("Bed No",self.bed_no)
        if(self.discharge_date!=""):
            print("Discharge_date",self.discharge_date)

    def set_discharge(self):
        self.discharge_date=input("Enter the discharge date")

p=Patient()
p.full_summary()
p.set_discharge()
p.full_summary()

