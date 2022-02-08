from ACME.OfficeTime import calculate_office_time
from ACME.GetMinutes import calculate_minutes
import unittest


class testofficetime(unittest.TestCase):

    employeeHoursA = [('MO', '10:05', '12:00'), ('TU', '9:00', '12:00'), (
        'TH', '01:00', '03:20'), ('SA', '14:00', '18:00'), ('SU', '18:00', '20:00')]
    employeeHoursB = [('MO', '10:00', '12:00'), ('TU', '11:00',
                                                 '12:00'), ('TH', '02:00', '03:00'), ('SA', '14:00', '18:00')]
    minutes_start = [605, 660, 120, 840]
    minutes_end = [720, 720, 200, 1080]

    def test_calculate_office_time(self):
        '''

        when calculate_office_time receives start minutes and end minutes then compares added minutes

        '''

        self.assertEqual(7.75, calculate_office_time(
            self.minutes_start, self.minutes_end))

    def test_calculate_minutesA(self):
        '''

        when time start receives employee schedule A then compares the initial converted minutes

        '''

        self.assertEqual([605, 660, 120, 840], calculate_minutes(
            self.employeeHoursA, self.employeeHoursB, 1))

    def test_calculate_minutesB(self):
        '''

        when time start receives employee schedule B then compare the final converted minutes

        '''
        self.assertEqual([720, 720, 200, 1080], calculate_minutes(
            self.employeeHoursA, self.employeeHoursB, 2))
