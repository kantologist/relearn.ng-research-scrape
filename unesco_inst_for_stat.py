from rand_test import test_uis_unesco
from settings import uis_unesco_data_url

def next_page(i):
    next_url = uis_unesco_data_url + '&SPSLanguage=EN&start1=' + str(i)
    return next_url

filepath = 'data/unesco_institute_for_statistics.csv'
test_uis_unesco(uis_unesco_data_url, filepath)
test_uis_unesco(next_page(6), filepath)
test_uis_unesco(next_page(11), filepath)
