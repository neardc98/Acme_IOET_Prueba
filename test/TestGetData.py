
from ACME.GetData import format_employee, read_file, new_employee
# from ACME.Employees import employee
import unittest


class testgetdata(unittest.TestCase):
    file = "/home/near/Documents/Acme_IOET_Prueba/ACME/test_employees.txt"
    
    scheduleEmployee = ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00\n','ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\n']

    formateEmployee = (
        'RENE', 'MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00')
    
    line = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'

    testEmployee="Employee(name=RENE, schedule=[('MO', '10:00', '12:00'), ('TU', '10:00', '12:00'), ('TH', '01:00', '03:00'), ('SA', '14:00', '18:00'), ('SU', '20:00', '21:00')])"

    linesEmployee=['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00']

    def test_read_file(self):
        '''

        compresses the extraction of the lines from the text file

        '''

        self.assertEqual(self.scheduleEmployee, read_file(self.file))

    def test_format_employee(self):
        '''

        check the format divided by the employee's name and schedule

        '''

        self.assertEqual(self.formateEmployee, format_employee(self.line))

    def test_new_employee(self):
        '''

        check the format divided by the employee's name and schedule

        '''
        employeeTest=new_employee(self.linesEmployee)

        self.assertEqual(self.testEmployee, employeeTest[0].__str__())