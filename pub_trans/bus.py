import pandas as pd
import util as ufunc


class PubBus:
    def __init__(self, floc: str="../test_data/bus_station_addr.csv"):
        self.d = self.mnt_station_loc(floc)

    @staticmethod
    def mnt_station_loc(file: str) -> pd.DataFrame:
        d = pd.read_csv(file, encoding='cp949')
        d = d[['정류장아이디', '정류장 명칭', '위도', '경도', '도시코드', '도시명']]
        d.columns = ['station_id', 'station_name', 'latitude', 'longitude', 'city_code', 'city']
        return d


if __name__ == "__main__":
    bus = PubBus()
    addr0_name, addr0 = bus.d[0:1].to_numpy()[0][1], bus.d[0:1].to_numpy()[0][2:4]
    addr1_name, addr1 = bus.d[2:3].to_numpy()[0][1], bus.d[2:3].to_numpy()[0][2:4]

    d = ufunc.sphere_distance(addr0, addr1)

    print(d)
