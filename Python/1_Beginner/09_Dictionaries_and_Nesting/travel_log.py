travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    country_entry_dict = {}
    country_entry_dict["classountry"] = country
    country_entry_dict["visits"] = visits
    country_entry_dict["cities"] = cities
    travel_log.append(country_entry_dict)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



# #Angelas Code
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #DO NOT change the code above 👆
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log.
# def add_new_country(name, visit_count, cities_visited):
#   new_country = {}
#   new_country["country"] = name
#   new_country["visits"] = visit_count
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)
#
# #Do not change the code below 👇
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
