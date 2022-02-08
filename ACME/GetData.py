from ACME.Employees import employee


def read_file(file):
    """

    Takes a line from the text file and reads it and stops the data to be processed.

    Parameters
    ----------
    file :
        filename to be processed

    Returns
    -------
    lines
        a list that contains the lines of the file

    """

    with open(file) as filename:
        lines=[]
        for lines_file in filename:
            lines.append(lines_file)
        return lines

def new_employee(lines):
    '''
    
    Gets a list with the lines of the .txt file, gets the name 
    of an employee and the schedule and creates the Employee object
    for each line and returns them in a list.

    Parameters
    ----------
    lines :
        a list that contains the lines of the file

    Returns
    -------
    employees
        a list with the Employee objects created from the file


    '''
    employees = []
    for line in lines:
        name, schedule = format_employee(line)
        newEmployee = employee(name, schedule)
        employees.append(newEmployee)
    return employees


def format_employee(string):
    '''

    Separates the data obtained from the text file by dividing by name and working time.

    Returns
    -------
    name
        contains the employee's name
    schedule
        contains the employee's schedule

    '''

    try:
        name, schedule = string.split("=")
    except ValueError:
        return None, None
    return name, schedule


