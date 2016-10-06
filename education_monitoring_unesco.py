from rand_test import test_en_unesco
from settings import en_unesco_data_url

def next_page(i):
    next_url = en_unesco_data_url + '?page=' + str(i)
    return next_url

filepath = 'data/education_monitoring_unesco.csv'
test_en_unesco(en_unesco_data_url, filepath)
test_en_unesco(next_page(1), filepath)
