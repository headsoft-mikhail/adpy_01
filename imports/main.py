from application.salary import calculate_salary
from application.people import get_employees
from datetime import datetime as dt

if __name__ == '__main__':
    print(dt.now().strftime("%Y-%m-%d %H:%M:%S"))
    calculate_salary()
    get_employees()

