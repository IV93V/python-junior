def get_numbers():
    """Возвращает все числа от 1000 до 2000, которые делятся на 7, но не кратны 5

    Returns: итерируемый объект с нужными числами
    """
    nums = []
    for i in range(1001,2001,7):
        if i%5 != 0:
            nums.append(i)
    
    return nums

    raise NotImplementedError