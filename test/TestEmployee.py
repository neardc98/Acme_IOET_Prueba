from ACME.Employees import employee
from ACME.GetData import new_employee
import unittest

class testemployee(unittest.TestCase):
    tesSchedule = [('MO', '10:00', '12:00'), ('TH', '12:00',
                                              '14:00'), ('SU', '20:00', '21:00')]
    schedule = 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'

    linesEmployee=['ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']

    testEmployee="Employee(name=ASTRID, schedule=[('MO', '10:00', '12:00'), ('TH', '12:00', '14:00'), ('SU', '20:00', '21:00')])"

    def test_workdays(self):
        '''

        Allows to check if the format is correct for processing each employee's timetable

        '''
        self.assertEqual(self.tesSchedule,
                         employee.workdays(self, self.schedule))

    def test_new_employee(self):
        '''

        check the format divided by the employee's name and schedule

        '''
        employeeTest=new_employee(self.linesEmployee)
        self.assertEqual(self.testEmployee, employeeTest[0].__str__())