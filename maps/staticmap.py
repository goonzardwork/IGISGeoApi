import c as const

from typing import Dict
import requests
import json
import shutil


class DomesticStaticMap:
    def __init__(self):
        self.header = self.gen_header()
        self.base = const.DOMESTIC_MAP_BASE

    @staticmethod
    def __token() -> (str, str):
        with open('../token.json') as file:
            tkn = json.load(file)

        return (tkn['navercloud']['username'],
                tkn['navercloud']['password'])

    def gen_header(self) -> Dict:
        u, p = self.__token()
        header = {
            const.DOMESTIC_GEOCODE_HKEY_ID: u,
            const.DOMESTIC_GEOCODE_HKEY_PW: p,
        }
        return header

    @staticmethod
    def gen_param(x_coord: str,
                  y_coord: str,
                  dataversion: str,
                  level: int,
                  width: int=300,
                  height: int=300,
                  maptype: str='basic',
                  fmt: str="png",
                  scale: int=2,
                  lang: str="ko",
                  public_transit: bool=True):
        param = {
            "center": f"{x_coord},{y_coord}",
            "level": level,
            "w": width,
            "h": height,
            "maptype": maptype,
            "format": fmt,
            "scale": scale,
            "lang": lang,
            "public_transit": public_transit,
            "dataversion": dataversion,
        }
        return param

    @staticmethod
    def gen_data_version():
        r = requests.get(const.DOMESTIC_MAP_VER_API_BASE)
        ver = r.json()
        r.close()
        return ver['version']

    def gen_map_img(self, xc: str, yc: str, zoom: int):
        h = self.gen_header()
        ver = self.gen_data_version()
        p = self.gen_param(xc, yc, ver, level=zoom)

        r = requests.get(
            url=const.DOMESTIC_MAP_BASE,
            headers=h,
            params=p
        )

        assert r.status_code == 200

        with open('img.png', 'wb') as file:
            file.write(r.content)
        r.close()


if __name__ == "__main__":
    testing = "경기도 안양시 만안구 안양동 627-287"
    d = DomesticStaticMap()

    from geocode.geocode import DomesticGeocode
    g = DomesticGeocode()
    a, x, y = g.addr_to_cord(testing)
    d.gen_map_img(x, y, 16)


