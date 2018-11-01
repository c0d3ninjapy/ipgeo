from __future__ import print_function
import socket
import pygeoip

# IP GEO v1.0 by c0d3ninja
# Instagram: c0d3ninja
# Discord: discord.gg/JV6pu5q

gip = pygeoip.GeoIP('GeoIP.dat')
gipcity = pygeoip.GeoIP('GeoLiteCity.dat')

ascii = """

$$$$$$\ $$$$$$$\         $$$$$$\  $$$$$$$$\  $$$$$$\  
\_$$  _|$$  __$$\       $$  __$$\ $$  _____|$$  __$$\ 
  $$ |  $$ |  $$ |      $$ /  \__|$$ |      $$ /  $$ |
  $$ |  $$$$$$$  |      $$ |$$$$\ $$$$$\    $$ |  $$ |
  $$ |  $$  ____/       $$ |\_$$ |$$  __|   $$ |  $$ |
  $$ |  $$ |            $$ |  $$ |$$ |      $$ |  $$ |
$$$$$$\ $$ |            \$$$$$$  |$$$$$$$$\  $$$$$$  |
\______|\__|             \______/ \________| \______/ 
                                                      
"""

print(ascii + "\n")
print("Author: c0d3ninja" + "\n")


host = "microsoft.com"
ip = socket.gethostbyname(host)

print("Website: " + host)
print("IP: " + ip)

print("----------------------")

print("Country: " + gip.country_name_by_addr(ip))
print("Time Zone: " + gipcity.time_zone_by_addr(ip))

record = gipcity.record_by_addr(ip)

continent = record["continent"]
areacode = record["area_code"]
countrycode = record["country_code3"]
postalcode = record["postal_code"]
latitude = record["latitude"]
longitude = record["longitude"]
city = record["city"]
metrocode = record["metro_code"]

print("City: " + city)
print("Continent: " + continent)
print("Country Code: " + countrycode)
print("Postal Code: " + str(postalcode))
print("Area Code: " + str(areacode))
print("Metro code: " + str(metrocode))
print("Latitude: " + str(latitude))
print("Longitude: " + str(longitude))

print("----------------------")
