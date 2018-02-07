ez_dict = {'birthdate': '1946-06-14', 'party': 'Republican',
           'gender': 'M',
           'identifiers': {
             'twitter': 'realDonaldTrump',
             'fec': 'P80001571',
           },
           'name': {'first': 'Donald', 'last': 'Trump'},
           'birthplace': {'state': 'NY', 'city': 'New York City'},
           'children': ['Donald', 'Ivanka',
                        'Eric', 'Tiffany', 'Barron'],
            'spouse': 'Melania Trump',
            'terms': [{'start_date': '2017-01-20',
                     'end_date': '2021-01-20'}]
           }
def foo_hello():
   
    return type(ez_dict)
def foo_a():
    return ez_dict['spouse']
def foo_b():
   
   return ez_dict['name']['first']
def foo_bx():
    return type(ez_dict['terms'])
def foo_c():
   
   myseq = ez_dict['name']['last'],ez_dict['name']['first']
   return ', '.join(myseq)
def foo_d():
   
   return len(ez_dict)
def foo_e():
    return len(ez_dict['children'])
def foo_f():
   
   return ez_dict['children'][4]
def foo_g():
    a = ez_dict['spouse']
    b = ez_dict['children']
    mylist = ",".join(b)
    return(a + ',' + mylist)
def foo_h():
   
   return ez_dict['terms'][0]['start_date']
def foo_i():
    import dateutil.parser
    from dateutil.relativedelta import relativedelta
    term = ez_dict['terms'][0]
    ty = dateutil.parser.parse(term['end_date'])
    tx = dateutil.parser.parse(ez_dict['birthdate'])
    diff = relativedelta(ty, tx)
    return diff.years
def foo_j():
   
  return 'http://docquery.fec.gov/cgi-bin/fecimg/?P80001571'