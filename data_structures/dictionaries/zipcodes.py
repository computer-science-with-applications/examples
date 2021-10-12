import csv
import random

def get_state_from_zip(zip_code, zip_codes):
    """
    Look up the state associated with a ZIP code

    Inputs:
      zip_code: string
      zip_codes: list of (ZIP Code, State) tuples

    Returns: string or None
    """
    state = None
    
    for zc, st in zip_codes:
        if zc == zip_code:
            state = st
            break
            
    return state

def gen_random_zip():
    """ 
    Generate a random ZIP Code
    """
    return "".join([str(random.randint(0,9)) for i in range(5)])


zip_codes_list = []
zip_codes_dict = {}

tiny_size = 0

with open("us_postal_codes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        zip_codes_list.append( (row["Postal Code"], row["State Abbreviation"]) )
        zip_codes_dict[row["Postal Code"]] = row["State Abbreviation"]        

small_zip_codes_list = zip_codes_list[:5000]
small_zip_codes_dict = dict(small_zip_codes_list)

medium_zip_codes_list = zip_codes_list[:20000]
medium_zip_codes_dict = dict(medium_zip_codes_list)
        
# From IPython, run the following:
#
# %timeit zipcodes.get_state_from_zip(zipcodes.gen_random_zip(), zipcodes.zip_codes_list)
# %timeit zipcodes.zip_codes_dict.get(zipcodes.gen_random_zip())

# %timeit zipcodes.get_state_from_zip(zipcodes.gen_random_zip(), zipcodes.small_zip_codes_list)
# %timeit zipcodes.get_state_from_zip(zipcodes.gen_random_zip(), zipcodes.medium_zip_codes_list)

# %timeit zipcodes.small_zip_codes_dict.get(zipcodes.gen_random_zip())
# %timeit zipcodes.medium_zip_codes_dict.get(zipcodes.gen_random_zip())


def time_dict_iter():
    for k, v in zip_codes_dict.items():
        pass

def time_list_iter():
    for k, v in zip_codes_list:
        pass


# %timeit time_dict_iter()
# %timeit time_list_iter()


