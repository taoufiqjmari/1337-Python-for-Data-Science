def all_thing_is_obj(object: any) -> int:
    the_type = type(object)
    if the_type is list:
        print(f'List : {the_type}')
    elif the_type is tuple:
        print(f'Tuple: {the_type}')
    elif the_type is set:
        print(f'Set : {the_type}')
    elif the_type is dict:
        print(f'Dict: {the_type}')
    elif the_type is str:
        print(f'{object} is in the kitchen : {the_type}')
    else:
        print('Type not found')

    return 42
