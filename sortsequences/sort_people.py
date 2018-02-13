from datastubs import PEOPLE_LIST

def longest_name():
    """
    sort by length of name in descending order
    """
    def foolen(p): # nothing wrong with having a function inside a function
        return len(p['name'])
    return sorted(PEOPLE_LIST, key=foolen, reverse=True)

def youngest():
    """
    sort by age in ascending order
    """
    # fill it out

    def foo(x)
        return x['age']

    return sorted(PEOPLE_LIST, key=foo)


def oldest():
    """
    sort by age in descending order
    """
    # fill it out

    def foo(x)
        return x['age']

    return sorted(PEOPLE_LIST, key=foo, reverse=True)


def name_reverse_alpha():
    # fill it out
    def foo(x)
        return x['name']

    return sorted(PEOPLE_LIST, key=foo, reverse=True)

def country_then_age():
    # fill it out
    def bob(y)
        return y['country']
    
    def foo(x)
        return x['age']

s = sort(PEOPLE_LIST, key =foo)

     return sorted(s, key=bob)
    