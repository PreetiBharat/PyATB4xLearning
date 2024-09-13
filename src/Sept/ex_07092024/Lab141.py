from abc import ABC, abstractmethod


class PyATB(ABC):

    @abstractmethod
    def payfees(self):
        pass

    def enrolled(self):
        print("Enrolled")


class Amit(PyATB):

    def payfees(self):
        print("Paid")


shubham = Amit()
shubham.enrolled()
shubham.payfees()
