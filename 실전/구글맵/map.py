# 구글맵 라이브러리
# pip install googlemaps

import googlemaps

# gcp google map 검색
# 
gmaps_api_key = 'AIzaSyDa_9XcZixmykF2y95JyJCZravaIvqdPPU'
gmaps = googlemaps.Client(key=gmaps_api_key)

g_result = gmaps.geocode('대한민국 인천광역시 부평구 경원대로 1366', language='ko')

latitude = g_result[0]['geometry']['location']['lat']
longtitude = g_result[0]['geometry']['location']['lng']
print('위도 : ', latitude)
print('경도 : ', longtitude)

# pip install folium
import folium
map = folium.Map(location=[latitude, longtitude])
