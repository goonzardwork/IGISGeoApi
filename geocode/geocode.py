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

    def addr_to_cord(self, address: str) -> (str, str, str):
        """
        :param address: searching keys
        """
        p = self.gen_param(address)
        r = requests.get(
            url=const.DOMESTIC_GEOCODE_BASE,
            params=p,
            headers=self.header
        )

        addr, x, y = self.proc_res(r.json())
        r.close()

        return addr, x, y

    @ staticmethod
    def proc_res(message: dict) -> (str, str, str):
        """
        :param message: parsed json
        :return:
        - address (road Addressname), x coordinate, y coordinate
        - all string
        """
        try:
            assert message['status'] == 'OK', const.DOMESTIC_GEOCODE_REQSTAT_ERR
            assert message['meta']['totalCount'] == 1, const.DOMESTIC_GEOCODE_REQCNT_ERR
        except AssertionError:
            print(
                format(const.DOMESTIC_GEOCODE_MSG, message['errorMessage'])
            )
        return (message['addresses'][0]['roadAddress'],
                message['addresses'][0]['x'],
                message['addresses'][0]['y'])


if __name__ == "__main__":
    d = DomesticGeocode()

    testing = "경기도 안양시 만안구 안양동 627-287"
    print(d.addr_to_cord(testing))
