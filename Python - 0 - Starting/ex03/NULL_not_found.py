def NULL_not_found(object: any) -> int:
    the_type = type(object)
    if object is None:
        print(f'Nothing: {object} {the_type}')
    elif the_type is float and object != object:
        print(f'Cheese: {object} {the_type}')
    elif the_type is int and object == 0:
        print(f'Zero: {object} {the_type}')
    elif the_type is str and object == '':
        print(f'Empty: {object} {the_type}')
    elif the_type is bool and object is False:
        print(f'Fake: {object} {the_type}')
    else:
        print('Type not Found')
        return 1
    return 0
