![license](https://img.shields.io/github/license/SKKUGoon/goServer)

# IGISGEO - IGIS Geo Tools 

<p>

[EN] This packages enables connection to Maps API, Real Estate Information API etc.


[KR] 해당 패키지는 Maps API에 접속하여 지도 정보, 지적 편집도 등등을 불러올 수 있음. 

</p>


| Supported DBMS   | Last Edited | Class Name |
|------------------|-------------|------------|
| Maps             | 2022.06.03  | -          |
| Real Estate Info | 2022.06.03  | -          |
| -                | 2022.05.31  | -          |  


## Maps and GeoCoding API

<p>

For scalability it will be wise to use Google Maps API.
However, google api's support for South Korea is feeble.
Also google uses pay as you go system. 

Therefore, for domestic purpose we use NAVER API. 
And if the need for world-wide application arises, we'll use google API(or other).


</p>

### NAVER MAPS API

<p>

NAVER Maps service support (https://www.ncloud.com/product/applicationService/maps)

</p>

| Service            | Payments       | API LIMIT |
|--------------------|----------------|-----------|
| Web Dynamic Map    | (No Usage Yet) |           |
| Mobile Dynamic Map | (No Usage Yet) |           |
| Static Map         | Free of charge | None      |
| Geocoding          | Free of charge | None      |
| Reverse Geocoding  | Free of charge | None      |
| Direction 5        | (No Usage)     |           |
| Direction 15       | (No Usage)     |           |


#### 1. NAVER MAPS - STATIC MAP

<p>

API Explanation: https://api.ncloud-docs.com/docs/ai-naver-mapsstaticmap

</p>


#### 2. NAVER MAPS - GEOCODING

<p>

API Explanation: https://api.ncloud-docs.com/docs/ai-naver-mapsgeocoding

</p>


#### 3. NAVER MAPS - REVERSE GEOCODING

<p>

API Explanation: https://api.ncloud-docs.com/docs/ai-naver-mapsreversegeocoding

</p>
