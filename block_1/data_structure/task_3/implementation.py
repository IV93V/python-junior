import copy

def copy_dict(origin_dict: dict) -> dict:
    new_dict = dict()
    for key, val in origin_dict.items():
        # print(f'{key}, {val}')
        if (isinstance(val,dict)):
            new_dict[key] = copy_dict(val)
        elif (isinstance(val,list)):
            new_dict[key] = copy.deepcopy(val)
        else:
            new_dict[key] = val
    return new_dict
    # raise NotImplementedError
