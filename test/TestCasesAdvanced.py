from ACME.GetData import format_employee,new_employee
import unittest

test_input = {
    'format_employee_input': [
        'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00',
        '',
        'RENE=M10:00-12:00',
        'RENE=MO24:00-12:00',
        'RENE=MO23:61-12:00',
        'RENE=MO10:00-12:00,TU10:00-12:00*q12asd,WE10:00-12:00'
    ],

    'format_employee_output': [
        ('RENE', "MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"),
        (None, None),
        ('RENE', "M10:00-12:00"),
        ('RENE', "MO24:00-12:00"),
        ('RENE', "MO23:61-12:00"),
        ('RENE', "MO10:00-12:00,TU10:00-12:00*q12asd,WE10:00-12:00")
    ],
    'getFilePath_input' : [ ""
    ],
    'new_employee_input' : [
        "RENE=MO10:00-12:00",
    ],
    'new_employee_output' : [
        "Employee(name=RENE, schedule=[('MO', '10:00', '12:00')])"
    ],
    
}

class Unittest(unittest.TestCase):
    """Advanced test cases."""

    def test_format_employee(self, _input='format_employee_input', output='format_employee_output'):
        for index, value in enumerate(test_input[_input]):
            result = format_employee(value)
            self.assertEqual(result, test_input[output][index])
            
    def test_new_employee(self, _input='new_employee_input', output='new_employee_output'):
        result = new_employee(test_input[_input])
        self.assertEqual(result[0].__str__(), test_input[output][0])