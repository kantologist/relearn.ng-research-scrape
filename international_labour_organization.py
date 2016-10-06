from rand_test import test_ilo
from settings import ilo_data_url


filepath = 'data/international_labour_organization.csv'
test_ilo(ilo_data_url, filepath)
test_ilo(ilo_data_url[0:-8]+"offset=10", filepath)
test_ilo(ilo_data_url[0:-8]+"offset=20", filepath)
