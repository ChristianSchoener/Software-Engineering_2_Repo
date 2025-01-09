import urllib.request


def get_data(start_url,data):
  get_url = start_url
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
print(get_data("https://api.open-meteo.com/v1/forecast?",my_data))
print()

my_new_data = {"latitude":"49.4542",
               "longitude":"11.0775",
               "timezone":"Europe/Berlin",
               "start_date":"2019-03-08",
               "end_date":"2019-03-08",
               "hourly":"temperature_2m"}
print(get_data("https://archive-api.open-meteo.com/v1/archive?",my_new_data))
