from rand_test import test_uk
from settings import uk_gov_data

def next_page(i):
    next_url = uk_gov_data + '&start=' + str(i)
    return next_url

filepath = 'data/uk_government.csv'
test_uk(uk_gov_data, filepath)
for i in range(20,280,20):
    test_uk(next_page(i), filepath)

