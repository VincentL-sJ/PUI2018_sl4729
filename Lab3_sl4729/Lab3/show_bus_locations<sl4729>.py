from __future__ import print_function
import json
try:
	import urllib2 as urllib
except ImportError:
	import urllib.request as urllib
import os
import sys

apikey = sys.argv[1]  #"b40ed1fc-a440-430c-995c-ed98906d8d52"
bus_line= sys.argv[2] #'M10'


#bus_url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + apikey +'&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
bus_url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, bus_line)

print (bus_url)
response = urllib.urlopen(bus_url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

VehicleActivity = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]["VehicleActivity"]
numbers = len(VehicleActivity)
print("Bus Line:%s"%(bus_line))
print("Number of Active Buses:%s"%(numbers))
count = 0
for vehicle in VehicleActivity:
	Location = VehicleActivity[count]['MonitoredVehicleJourney']['VehicleLocation']
	latitude = Location['Latitude']
	longitude = Location['Longitude']
	print("Bus %s is at latitude %s and longitude %s"%(count,latitude,longitude))
	count += 1



