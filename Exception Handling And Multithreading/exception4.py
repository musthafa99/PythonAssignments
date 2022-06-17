def convertor(x):
    try:
        return int(x)
    except Exception as e:
        print(e)

convertor("XYZ")