## CHANGE LOG

### [Unreleased Version] - 2022 - 05 - 31

<p>

Initial Commit for IGIS Geo API Project.

NAVER API account created.

NAVER geocode and static map API created. 

TODO: create reverse geocode and web-dynamic map api

</p>

##### Added

<p>

* dir
  * maps
    * dmap: domestic maps api (NAVER API)
    * fmap: foreign maps (preferably google API)
  * geocode
    * dgeo: domestic geocode api (NAVER API)
    * fgeo: foreign geocode api (preferably google API)

* files
  * geocode/dgeo/geocode.py
  * maps/dmap/staticmap.py
  * c.py

</p>

##### Changed

<p>

</p>

##### Fixed

<p>

</p>


## CHANGE LOG

### [Unreleased Version] - 2022 - 06 - 13

<p>

support counting of close public transportation stations.
only bus station for now. subway api is waiting for approval

</p>

##### Added

<p>

* ./pub_trans
  * bus.py
    * pick out latitude and longitude from the data
    * static data - data is not gained by api. 
  * subway.py
    * TODO: not finished
* test_data
  * address.csv
    * location of IGIS assets - private information!!
  * bus_station_addr.csv
    * location of bus-station and its latitude and longitude position.
  * subway_name.csv
    * subway_name is insufficient to find latitude and longitude position of the station. 
    * waiting on open-api approval right now
* ./asset_location.py
  * records IGIS assets and geocode them
  * produce ./asset_addr.json
* ./asset_location_dist.py
  * func main() - measures distance between asset and public transportation station(bus) and count them.
  * >>> (37.56, 127.07) 0
* ./asset_addr.json
  * {'[fundcode]': {"addr": ..., "x": ..., "y": ...}} shape
  * if NAVER API cannot find x and y coordinates it is left out as None
  * TODO: x and y is inverted. change the position!
</p>

##### Changed

<p>

* ./.gitignore
  * add csv files to ignore
  
</p>

##### Fixed

<p>

</p>
