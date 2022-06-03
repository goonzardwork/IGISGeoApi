import c as const

from typing import Dict
import requests
import json


class DomesticGeocode:
    def __init__(self):
        self.header = self.gen_header()
        self.base = const.DOMESTIC_GEOCODE_BASE

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
    def gen_param(srch_key: str) -> Dict:
        return {"query": srch_key}

    def addr_to_cord(self, address: str):
        p = self.gen_param(address)
        r = requests.get(
            url=const.DOMESTIC_GEOCODE_BASE,
            params=p,
            headers=self.header
        )

        print(r)
        print(r.json())
        r.close()


if __name__ == "__main__":
    d = DomesticGeocode()

    testing = "경기도 안양시 만안구 안양동 627-287"
    d.addr_to_cord(testing)
