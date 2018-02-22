from datetime import datetime
from urllib.parse import urljoin
import data_helper
DATA_SRC_URL = 'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html'
def txdate_to_iso(datestr):
    
    if len(datestr) == 10:    
        d = datestr[3:5]
        y = datestr[-4:]
        m = datestr[0:2]
    else:
        m, d, y = datestr.split('/')
        y = '19' + y
    
    return '-'.join([y, m, d])
   
   
    """
    A helper function that, given a date formatted the way that the
    Texas Dept. of Justice does it,
        i.e. MM/DD/YYYY, e.g. '10/24/1988'
        or even: '10/24/88'
    and returns a ISO-formatted string, i.e. YYYY-MM-DD
    Args:
        datestr: a <str>, ostensibly one that is meant to be a
            date value like '10/24/1988'
    Returns:
        <str>: in 'YYYY-MM-DD' format, e.g. '1988-10-24'
    """
def calc_years_diff(start_date, end_date):
   xd = datetime.strptime(start_date, '%Y-%m-%d')
   yd = datetime.strptime(end_date, '%Y-%m-%d')
   diff = yd-xd
   return round(diff.days/365,1)
def make_absolute_url(href):
    
    print(href)
    print("Print working?")
    return urljoin(DATA_SRC_URL, href)
    """
    This function uses data_helper.DATA_SRC_URL and the builtin function
      urllib.parse.urljoin() to programmatically join a relative URL with
      the known URL of the source page (DATA_SRC_URL)
    Args:
        href: a <str> object that is a partial URL that looks something like:
           'dr_info/falkjohnjr.html'
    Returns:
        <str>: A fully resolvable URL for a webpage, e.g.
            'https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_info/falkjohnjr.html'
    The TX death penalty page contains URLs for the "Offender Information"
    pages, and these URLs are in relative format, e.g.
    dr_info/falkjohnjr.html
    But we want them in absolute format:
    The absolute form of a URL depends on the URL that the page was
        *scraped* from. In this exercise, it's the value of the
        DATA_SRC_URL which was defined in `data_helper.py`
    e.g.
    https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html
    A helper function that is "aware" that the data was scraped
        From the DATA_SRC_URL as specified in `data_helper.py`, e.g.
            https://example.com/death_row/dr_offenders_on_dr.html
        and knows that a hyperlink href attribute of
            'dr_info/doejohn.html'
        Should resolve to something like:
            'https://example.com/death_row/dr_info/doejohn.html'
        Note that 'https://example.com/death_row/...' is obviously
         not our data source. I'm using it as a placeholder for
         whatever is in data_helper.py
    Pre-reqs:
      The DATA_SRC_URL is defined in a module accessible to this
        script as:
        from data_helper import DATA_SRC_URL
    Args:
      href: a <str> object
    Returns:
      <str>
    """
    #### fill in yourself
    #### could be a one-liner with proper use of the urljoin() function...