from geocode.geocode import DomesticGeocode

import pandas as pd

from typing import Dict
import json
import time


def _clean1(v: str):
    if ' 외 ' in v:
        return v.split('외 ')[0]
    return v


def _clean2(v: str):
    if ',' in v:
        return v.split(',')[0]
    return v


def clean_addr(val: str):
    """
    Address names are labeled haphazardly.
    Key words to look:
    ['외 ', ',']
    """
    v = _clean1(val)
    v = _clean2(v)
    if v[-1:] == ' ':
        return v[:-1]
    return v


def asset_to_json() -> Dict:
    geo = DomesticGeocode()

    # get asset loc.
    d = pd.read_csv("./test_data/address.csv")
    d = d.to_numpy()

    result = dict()
    i = 0
    for code, name, addr in d:
        c_addr = clean_addr(addr)
        exists, x, y = geo.addr_to_cord(c_addr)
        if exists is None:
            result[code] = {
                "addr": c_addr,
                "x": None,
                "y": None
            }
            # flag address
            print(f"{c_addr} cannot be found on naver api")

        result[code] = {
            "addr": c_addr,
            "x": x,
            "y": y
        }

        # progress
        i += 1
        print(f"{i}/{len(d)} done")

        # api request constraint
        time.sleep(0.1)

    return result


if __name__ == "__main__":
    a = asset_to_json()
    with open("./asset_addr.json", 'w') as file:
        json.dump(a, file)

    with open("./asset_addr.json", 'r') as file:
        r = json.load(file)

    print(r)
