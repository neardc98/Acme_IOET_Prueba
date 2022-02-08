import re


class employee():
    '''

    Attributes
    ----------
    metric_hour :
        A variable containing the equivalence of an hour in minutes
    name : str
        an string to represent the name of the employee
    schedule : str
        a string representing the days and time the employee worked
            e.g. "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
    Methods
    -------
    workdays()
        Stylizes the schedule of each employee entered 

    '''

    metric_hour = 60

    def __init__(self, name: str, schedule: str = None):
        '''

        Parameters
        ----------
        name : str
            the name of the employee
        schedule : srt 
            a list employee schedule objects that represent the time the
            employee worked

        '''

        self.name = name
        self.schedule = schedule


    def workdays(self, schedule):
        '''for the schedule, formatting it with the regular expressions

        Returns
        -------
        self.schedule
            returns a list in the form 
            e.g. [('MO', '10:05', '12:00'), ('TH', '01:00', '03:20'), ('SU', '18:00', '20:00')]

        '''

        try:
            formate_schedule = re.findall(
                r'(MO|TU|WE|TH|FR|SA|SU)(?P<time>[0-9:]+)\-(?P<end>[0-9:]+)', schedule)
        except ValueError as fail:
            print(fail)
        finally:
            self.schedule = formate_schedule

        return self.schedule

    def __str__(self):
        workdaysEmployee=employee.workdays(self, self.schedule)
        return f"Employee(name={self.name}, schedule={workdaysEmployee})"