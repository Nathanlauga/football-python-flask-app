def exists(var):
    try:
        var
    except NameError:
        return False
    else:
        return True