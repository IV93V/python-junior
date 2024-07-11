def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу

    Args:
        month: название месяца

    Returns: количество дней
    """
    if   month == 'январь': return 31
    elif month == 'февраль': return 28
    elif month == 'март': return 31  
    elif month == 'апрель': return 30  
    elif month == 'май': return 31  
    elif month == 'июнь': return 30  
    elif month == 'июль': return 31  
    elif month == 'август': return 31  
    elif month == 'сентябрь': return 30  
    elif month == 'октябрь': return 31  
    elif month == 'ноябрь': return 30  
    elif month == 'декабрь': return 31 
    else: return 0
    
    raise NotImplementedError
