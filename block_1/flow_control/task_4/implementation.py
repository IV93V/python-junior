from datetime import (
    date,
)

def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    year = some_date.year
    month = some_date.month
    day = some_date.day
    
    m_days = month_days(month,year)
    if m_days==day: 
        new_day=1 
        new_month=month+1
    else: 
        new_day=day+1
        new_month=month
    
    if new_month > 12:
        new_month = 1
        new_year = year + 1
    else:
        new_year = year
    
    return date(new_year,new_month,new_day)
    raise NotImplementedError
    
def month_days(month,year):
    if   month == 1: return 31
    elif month == 2 and year%4 == 0: return 29
    elif month == 2 and year%4 != 0: return 28
    elif month == 3: return 31
    elif month == 4: return 30
    elif month == 5: return 31
    elif month == 6: return 30
    elif month == 7: return 31
    elif month == 8: return 31
    elif month == 9: return 30
    elif month == 10: return 31
    elif month == 11: return 30
    elif month == 12: return 31
    