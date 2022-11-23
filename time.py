import argparse
import urllib.request
parser = argparse.ArgumentParser(description='Region and city of time zone')

parser.add_argument('region_name', type=str, help='Input region name')
parser.add_argument('city_name', type=str, help='Input city name')

args = parser.parse_args()

urlString = f'http://worldtimeapi.org/api/timezone/{args.region_name}/{args.city_name}'
response = urllib.request.urlopen(urlString, timeout=5)
data = response.read()
res = data.split(b',')[2].split(b'"')[3].split(b'T')
date = res[0]
time = res[1].split(b'+')[0].split(b'-')[0]
timezone = data.split(b',')[13].split(b'"')[3]
print(f"timezone: UTC{timezone.decode('utf-8')}\nlocal time: {date.decode('utf-8')} {time.decode('utf-8')}")

