from bs4 import BeautifulSoup
import pathlib
import re
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
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.text


def parse_source(html):
    parsed = BeautifulSoup(html, 'html5lib')  #added html5lib to get rid of find_all attribute error
    return parsed


def load_inspection_page(name):
    file_path = pathlib.Path(name)
    return file_path.read_text(encoding='utf8')


def restaurant_data_generator(html):
    id_finder = re.compile(r'PR[\d]+~')
    return html.find_all('div', id=id_finder)


def has_two_tds(elem):
    is_tr = elem.name == 'tr'
    td_children = elem.find_all('td', recursive=False)
    has_two = len(td_children) == 2
    return is_tr and has_two


def clean_data(td):
    return td.text.strip(" \n:-")


def extract_restaurant_metadata(elem):
    restaurant_data_rows = elem.find('tbody').find_all(
        has_two_tds, recursive=False
    )
    rdata = {}
    current_label = ''
    for data_row in restaurant_data_rows:
        key_cell, val_cell = data_row.find_all('td', recursive=False)
        new_label = clean_data(key_cell)
        current_label = new_label if new_label else current_label
        rdata.setdefault(current_label, []).append(clean_data(val_cell))
    return rdata


def is_inspection_data_row(elem):
    is_tr = elem.name == 'tr'
    if not is_tr:
        return False
    td_children = elem.find_all('td', recursive=False)
    has_four = len(td_children) == 4
    this_text = clean_data(td_children[0]).lower()
    contains_word = 'inspection' in this_text
    does_not_start = not this_text.startswith('inspection')
    return is_tr and has_four and contains_word and does_not_start


def get_score_data(elem):
    inspection_rows = elem.find_all(is_inspection_data_row)
    samples = len(inspection_rows)
    total = 0
    high_score = 0
    average = 0
    for row in inspection_rows:
        strval = clean_data(row.find_all('td')[2])
        try:
            intval = int(strval)
        except (ValueError, TypeError):
            samples -= 1
        else:
            total += intval
            high_score = intval if intval > high_score else high_score

    if samples:
        average = total/float(samples)
    data = {
        'Average Score': average,
        'High Score': high_score,
        'Total Inspections': samples
    }
    return data


if __name__ == '__main__':
    use_params = {
        'Inspection_Start': '2/1/2013',
        'Inspection_End': '2/1/2015',
        'Zip_Code': '98101'
    }
    # html = get_inspection_page(**use_params)
    html = load_inspection_page('inspection_page.html')
    parsed = parse_source(html)
    content_col = parsed.find("td", id="contentcol")
    data_list = restaurant_data_generator(content_col)
    for data_div in data_list:
        metadata = extract_restaurant_metadata(data_div)
        inspection_data = get_score_data(data_div)
        metadata.update(inspection_data)
        print(metadata)
