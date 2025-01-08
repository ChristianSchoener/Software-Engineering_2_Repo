import urllib.request


def get_data(data):
  get_url = "https://api.open-meteo.com/v1/forecast?"

  for key,val in data.items():
    get_url += "&" + key + "=" + val

  contents = urllib.request.urlopen(get_url).read()
  return contents

my_data = {"latitude":"49.4542",
           "longitude":"11.0775",
           "timezone":"Europe/Berlin",
           "start_date":"2025-01-08",
           "end_date":"2025-01-13",
           "hourly":"temperature_2m"}
print(get_data(my_data))
print()

my_new_data = {"latitude":"49.4542",
               "longitude":"11.0775",
               "timezone":"Europe/Berlin",
               "start_date":"2019-03-08",
               "end_date":"2019-03-08",
               "hourly":"temperature_2m"}
print(get_data(my_new_data))
