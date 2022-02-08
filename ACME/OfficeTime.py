from ACME.Employees import employee
from ACME.GetData import new_employee

def calculate_office_time(minutesStart, minutesEnd):
    ''' 

    From the start and end minutes of the working day, 
    calculate the total time two employees have been in the company. 

    Parameters
    ----------
    minutesStart:
        List representing the minutes at the start of the working day
    minutesEnd:
        List representing end of working day minutes

    Returns
    -------
    sum(totalTime)
        send the time spent together by two employees at the office  e.g "7.75"

    '''
    sumHoursMinutes = []

    def minutes_office(minutesStart, minutesEnd):
        '''

        This function traverses the start and end times of two employees, 
        subtracts them to obtain the minutes spent together by the two employees.

        Returns
        -------
        minutesInoffice
            returns a list of absolute values subtracted from start and end times

        '''
        minutesInoffice = []

        for i in range(len(minutesStart)):
            minutesInoffice.append(abs(minutesStart[i] - minutesEnd[i]))
        return minutesInoffice

    def hour_office():
        '''

        This function converts the minutes in the office of two employees to hours.

        Returns
        -------
        hoursInOffice
            returns the minutes turned into hours

        '''
        hoursInOffice = []

        for i in range(len(minutes_office(minutesStart, minutesEnd))):
            hoursInOffice.append(minutes_office(minutesStart, minutesEnd)[i]/60)
        return hoursInOffice

    def hours_decimal():
        '''

        This function takes the decimal part of the hours in the office. 

        Returns
        -------
        decimalHours
            returns the decimal part of the hours of each day that two employees coincide

        '''
        decimalHours = []

        for i in range(len(hour_office())):
            decimalHours.append(hour_office()[i] % 1)
        return decimalHours

    def horas_entero():
        '''
        Take the entire part of the hours in the office of two employees.

        Returns
        -------
        enteros
            returns the whole part of the hours

        '''
        enteros = []

        for i in range(len(hour_office())):
            enteros.append(int(hour_office()[i]))
        return enteros

    def convertir_minutos():
        '''

        This function allows you to convert decimal hours into minutes. 

        Returns
        -------
        decimalMinutesConverted
            decimal hours converted to minutes

        '''
        decimalMinutesConverted = []

        for i in range(len(hours_decimal())):
            decimalMinutesConverted.append(
                (hours_decimal()[i]*employee.metric_hour)/100)
        return decimalMinutesConverted

    def calculate_office_time():
        '''

        Takes whole hours and decimals converted to minutes and adds them together.

        Returns
        -------
        sumHoursMinutes
            Returns the time two employees have been together in a list of HH:MM of the workweek. 

        '''
        for i in range(len(horas_entero())):
            sumHoursMinutes.append(horas_entero()[i]+convertir_minutos()[i])
        return sumHoursMinutes

    return sum(calculate_office_time())


""" for employeeTime in new_employee:
        print(
            f'The amount to pay {employee.name} is: {sum(calculate_office_time())} USD') """