from rand_test import test_world_bank
from settings import world_bank_data_url

def next_page(i):
    next_url = world_bank_data_url[0:60] + 'page=' + str(i)+ world_bank_data_url[66:]
    return next_url

filepath = 'data/world_bank.csv'
test_world_bank(world_bank_data_url, filepath)
for i in range(2,5):
    test_world_bank(next_page(i), filepath)
