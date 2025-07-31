from name2gender import Name2Gender

if __name__ == '__main__':
    n2g = Name2Gender()
    print(n2g('Otto', return_probability=True))
    print(n2g('Jane', return_probability=True))
