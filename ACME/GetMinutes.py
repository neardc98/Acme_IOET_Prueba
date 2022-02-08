from ACME.Employees import employee


def calculate_minutes(employeeHoursA, employeeHoursB, position):
    """

    Take the list of employees' schedules A, B and the position of the lists.

    Parameters
    ----------
    employeeHoursA,employeeHoursB: list
        employee A's schedule and employee B's schedule

    position: int
        allows to obtain the position of the list, to take the start or end time of the day.

    Returns
    -------
    employeeMinutes
        a contains the converted start and end times of the employees' working day  
        e.g "[605, 660, 120, 840]"

    """
    employeeMinutes = []
    for searchEmployeeA, searchEmployeeB in zip(employeeHoursA, employeeHoursB):
        if searchEmployeeA[0] == searchEmployeeB[0]:

            A_hours, A_minutes = searchEmployeeA[position].split(':')
            B_hours, B_minutes = searchEmployeeB[position].split(':')
            total_m_A = int(A_hours) * \
                employee.metric_hour + int(A_minutes)
            total_m_B = int(B_hours) * \
                employee.metric_hour + int(B_minutes)
            if total_m_A > total_m_B:
                rest1 = (total_m_A)
            else:
                rest1 = (total_m_B)
            employeeMinutes.append(rest1)
            
    return employeeMinutes
