from geocode.geocode import DomesticGeocode
import pandas as pd


class PubSubway:
    def __init__(self, floc: str="../test_data/subway_name.csv"):
        self.d = self.mnt_station_loc(floc)

    @staticmethod
    def mnt_station_loc(file: str) -> pd.DataFrame:
        d = pd.read_csv(file)
        return d

    def get_latlng(self):
        ...


if __name__ == "__main__":
    subway = PubSubway()
