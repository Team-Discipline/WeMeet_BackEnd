import requests
import pandas as pd
import numpy as np

# request to Kakao API from location information (entered by user)
# gets user-entered information from the Front-End

def requestLocation(region):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    params = {'query': region}
    headers = {"Authorization": "60f67244349d7ae054b6216815c8431a"}
    places = requests.get(url, params=params, headers=headers).json()['documents']
    
    return places

# Data list for both front and back ends
def infoLocation(places):
    axis_x = []
    axis_y = []
    place_name = []
    address = []
    place_url = []
    place_ID = []
        
    axis_x.append(float(places['axis_x']))
    axis_y.append(float(places['axis_y']))
    place_name.append(places['place_name'])
    address.append(places['address'])
    place_url.append(places['place_url'])
    place_ID.append(places[id])
        
    info_arr = np.array([place_ID, place_name, axis_x, axis_y, address, place_url]).T
    dataframe = pd.DataFrame(info_arr, columns = ['place_ID', 'place_name', 'axis_x', 'axis_y', 'address', 'place_url'])

    return dataframe

# Create data lists for multiple locations
def makeDatalist(place_name):
    dataframe = None
    
    for place in place_name:
        p_name = requestLocation(place)
        p_info = infoLocation(p_name)
        
        if dataframe is None:
            dataframe = p_info
        elif p_info is None:
            continue
        else:
            dataframe = pd.concat([dataframe, p_info], join = 'outer', ignore_index = True)
    
    return dataframe