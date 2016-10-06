from rand_test import test_oecd
from settings import oecd_data_url

def next_page(i):
    next_url = oecd_data_url + '/' + str(i) + '/'
    return next_url

filepath = 'data/oecd.csv'
test_oecd(oecd_data_url, filepath)
test_oecd(next_page(2), filepath)
test_oecd(next_page(3), filepath)
test_oecd(next_page(4), filepath)
