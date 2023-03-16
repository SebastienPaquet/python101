def print_file_n_name():
    if __name__ == "__main__":
        print("ran current file/module directly, tested by 'if __name__='__main__':'")
    else:
        print("ran file as an import")
    print("(dunder file) __file__ :",__file__)
    print("(dunder name) __name__ :",__name__)
    #print("(dunder qualname) __qualname__ :",__qualname__)  #NameError: name '__qualname__' is not defined

if __name__ == "__main__":
    print_file_n_name()

def divide(dividend, divisor):
    return dividend / divisor