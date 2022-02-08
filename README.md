# ACME
This module calculates the frequency with which pairs of incoming employees have coincided in the office, we have the name of an employee and the time he/she worked, indicating the day, hours and minutes.

> **`Python 3.x`** is required.

### Run Tests:
    python3 -m unittest -v <ruta/filename>

### Clone the project:
```
git clone https://github.com/neardc98/Acme_IOET_Prueba
```

### Change to the app directory:

```
cd ACME_IOET_PRUEBA
```

### Problem Statement

#

<details>
  <summary>Problem</summary>
  

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame.
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.
Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

#

#### Example :

##### INPUT

```
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
```


##### OUTPUT

```
OUTPUT:
ASTRID-RENE: 2
ASTRID-ANDRES: 3
RENE-ANDRES: 2
```
#

</details>


<details>
    <summary>More</summary>

### Solution


It is required to solve the problem of the company ACME, they want to keep better control of the hours in which their employees coincide in the company, given their flexible work schedules for this, we compare the days that work equally workers take the time of arrival and departure time, we convert them to minutes to establish total time of minutes and then take them to their respective hours. 

When comparing the arrival minutes we prioritize the higher number on the other hand with the departure minutes we take the lower time these results we subtract them and place them in absolute values, we convert them into hours from this we divide the number into whole parts and decimal part which is converted into minutes, and once the conversion is done, we add the whole part in hours and the decimal part in minutes obtaining the time in which two employees coincide in the office.






![UML-class case](https://lucid.app/publicSegments/view/978975f9-7448-411e-bd83-04199e49a2eb/image.png)

This UML was created using  [lucid.app](https://lucid.app)

After the architecture of the project. I defined the structure as the following:
```
ACME_IOET_PRUEBA
|____ACME
|     | __init__.py
│     │ __main__.py
|     | Employees.py
|     | GetData.py
|     | GetMinutes.py
|     | OfficeTime.py
|     | test_employees.txt
|__tests
|     | __init__.py
|     | TestCasesAdvanced.py
|     | TestEmployee.py
|     | TestGetData.py
|     | TestOfficeTime.py
|
|__README.md
```
</details>