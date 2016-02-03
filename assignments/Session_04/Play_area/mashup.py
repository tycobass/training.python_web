from bs4 import BeautifulSoup
import requests

INSPECTION_DOMAIN = 'http://info.kingcounty.gov'
INSPECTION_PATH = '/health/ehs/foodsafety/inspections/Results.aspx'
INSPECTION_PARAMS = {
    'Output': 'W',
    'Business_Name': '',
    'Business_Address': '',
    'Longitude': '',
    'Latitude': '',
    'City': '',
    'Zip_Code': '',
    'Inspection_Type': 'All',
    'Inspection_Start': '',
    'Inspection_End': '',
    'Inspection_Closed_Business': 'A',
    'Violation_Points': '',
    'Violation_Red_Points': '',
    'Violation_Descr': '',
    'Fuzzy_Search': 'N',
    'Sort': 'H'
}


def get_inspection_page(**kwargs):
    url = INSPECTION_DOMAIN + INSPECTION_PATH
    params = INSPECTION_PARAMS.copy()
    for key, val in kwargs.items():
        if key in INSPECTION_PARAMS:
            params[key] = val
    #import pdb; pdb.set_trace()    ###import debugger#############################
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.text


def parse_source(html):
    parsed = BeautifulSoup(html, "html5lib")
    return parsed

if __name__ == '__main__':
    use_params = {
        'Inspection_Start': '1/1/2013',
        'Inspection_End': '3/1/2013',
        'Zip_Code': '98105'
    }
    html = get_inspection_page(**use_params)
    parsed = parse_source(html)
    #print(parsed.prettify())  dos codec won't support char map
    with open('inspection_page.html', 'w') as fh:  # these two lines necessary to work around dos window encoding error
        fh.write(parsed.prettify())



