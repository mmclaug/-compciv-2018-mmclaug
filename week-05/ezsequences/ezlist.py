#################################
# ezsequences/ezlist.py
#
# This skeleton script contains a series of functions that
#  return

ez_list = [0, 1, 2, 3, 4, ['a', 'b', 'c'], 5, ['apples', 'oranges'], 42]



def foo_hello():
    return type(ez_list)
    """
    This function should simply return the `type`
     of the `ez_list` object.

    This guarantees that you'll past at least one of
      the tests/assertions in test_ezlist.py
    """



##################
# Exercises foo_a through foo_e cover basic list access
##################

def foo_a():
   return ez_list[0]
   
   
    """
    Return the very first member of `ez_list`
    """


def foo_b():
   return ez_list[1] + ez_list[3]
   
    """
    Return the sum of the 2nd and 4th members of
      `ezlist`
    """



def foo_c():
    return ez_list[8]
   
    """
    Return the very last member of `ez_list`.

    Use a negative index to specify this member
    """


def foo_cx():
   return type(ez_list[7])
   
   
    """
    Return the type of the object that is the
        second-to-last member of `ez_list`
    """


def foo_d():
    
    return ez_list[7][1]
    
    """
    Return the very last member of the sequence that itself
        is the second-to-last member of `ez_list`
    """


def foo_e():
    
    return len(ez_list)
    
    """
    Calculate and return the length of `ez_list`,  i.e., the
      number of members it contains.
    """


def foo_f():
   
   
string1 = str(ez_list[5][0])
string2 = str(ez_list[5][1])
string3 = str(ez_list[5][2])

   return (string1 + ';' + string2 + ';' + string3)   
    """
    Return the 6th member of `ez_list` as a single,
      semi-colon delimited string

      i.e. the separate values are joined with the
        semi-colon character
    """


def foo_g():
  mylist = ez_list[1], ez_list[2], ez_list[3], ez_list[4]
  return mylist
  
  """
    Return a list that contains the 2nd through 5th
      elements of `ez_list`

      (it should have 4 members total)
    """


def foo_h():
    mylist = ez_list[8], ez_list[7], ez_list[6]
    return mylist 
    
    """
    Return a list that consists of the last
      3 members of `ez_list` in *reverse* order
    """

