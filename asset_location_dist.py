from pub_trans.bus import PubBus
import util as ufunc

import pandas as pd

import json


def get_bus_station_cnt(base: (str, str), comparison:pd.DataFrame, thres: int):
    """
    :param base:
    - Point of origin. Base Point. Compare from here
    :param comparison:
    - DataFrame of all the bus station in South Korea
    :param thres:
    - If the distance between bus station and the base is below this threshold
    - count it as close-station
    :return:
    """
    base_addr = (float(base[0]), float(base[1]))
    stations = comparison.to_numpy()
    count = 0

    for _, _, lat, lng, _, _ in stations:
        station_addr = (lat, lng)
        d = ufunc.sphere_distance(base_addr, station_addr)
        if d < thres:
            count += 1

    print(base_addr, count)


def main():
    with open("./asset_addr.json", 'r') as file:
        r = json.load(file)

    bus = PubBus('./test_data/bus_station_addr.csv')
    for fund_code, data in r.items():
        if data['x'] is not None:
            addr_tmp = (data['y'], data['x'])
            # station inside 500 meters
            get_bus_station_cnt(addr_tmp, bus.d, thres=100)
        else:
            print(data['addr'], 'no coordinates')

main()
