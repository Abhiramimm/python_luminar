from json import load

f=open("C:\\Users\\Admin\\Desktop\\mypython\\json_works\\restcountries\\data.json","r",encoding="UTF-8")

data=load(f)

# q1-->print total no.of countries
print(len(data))

# q2-->print name of all countries
all_countries=[c.get("name") for c in data]
# print(all_countries)

# q3-->print capitals of all countries
all_capitals=[c.get("capital") for c in data]
# print(all_capitals)

# q4-->print capital of "Afghanistan"
capital_filter=[c.get("capital") for c in data if c.get("name")=="Afghanistan"]
# print(capital_filter)

# q5-->print "alpha2Code" of "Afghanistan"
alpha2Code_filter=[c.get("alpha2Code") for c in data if c.get("name")=="Afghanistan"]
# print(alpha2Code_filter)

# q6-->print "alpha3Code" of "Afghanistan"
alpha3Code_filter=[c.get("alpha3Code") for c in data if c.get("name")=="Afghanistan"]
# print(alpha3Code_filter)

# q7-->print "topLevelDomain" of "Afghanistan"??????????????????????????????????
topLevelDomain=[c.get("topLevelDomain")for c in data if c.get("name")=="Åland Islands"]
# print(topLevelDomain)

# q8-->print "callingCodes" of "Afghanistan"
callingCodes=[c.get("callingCodes")for c in data if c.get("name")=="Afghanistan"]
# print(callingCodes)

# q9-->print "altSpellings" of "Afghanistan"
altSpellings=[c.get("altSpellings")for c in data if c.get("name")=="Afghanistan"]
# print(altSpellings)

# ********************************************************************************************
# q10-->print all countries under region asia

region_filter=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(region_filter)

#q11--> print all countries where timezone="UTC+04:30"
timezone_filter=[c.get("name") for c in data if "UTC-04:00" in c.get("timezones")]
# print(timezone_filter)

#q12--> print borders of "Afghanistan"
borders_filter=[c.get("borders") for c in data if c.get("name")=="Afghanistan"]
# print(borders_filter)

# q13-->print all currencie name?????????????????
all_currencies=[c.get("currencies") for c in data ]
# print(all_currencies)

# q14-->print largest country????????????????????
# def get_area(dictionary):
#     return dictionary.get("area")
# largest_country=max(data,key=get_area)
# print(largest_country)

# q15-->print smallest country based on area
# q16-->print all languages
all_languages=[c.get("languages") for c in data]
# print(all_languages)

# q17-->print english speaking countries????????????????????
language_filter=[c.get("name") for c in data if c.get("languages")=="English"]
# print(language_filter)

# q18-->print all independent countries
independent_countries=[c.get("name") for c in data if c.get("independent")==True]
# print(independent_countries)

# q19-->print total no.of independent countries
# print(len(independent_countries))

#q20--> print largest population country
def get_population(dictionary):
    return dictionary.get("population")
largest_population=max(data,key=get_population)
print(largest_population.get("name"))
# q21-->print smallest population country
smallest_population=min(data,key=get_population)
print(smallest_population.get("name"))


# q22-->print all country name where native name and name are same eg:native_name=english and name=english(languages)

# q23-->print all countries where subregion="Western Asia"
subregion_filter=[c.get("name")for c in data if c.get("subregion")=="Western Asia"]
# print(subregion_filter)

# q24-->print all currency details of India
# q25-->print languages of Uganda
lang_filter=[c.get("languages") for c in data if c.get("name")=="Uganda"]
# print(lang_filter)

# q26-->print othernames of "Western Sahara"   ????????
other_names_filter=[c.get("otherNames") for c in data if c.get("name")=="Yemen"]
# print(other_names_filter)




# q14-->print othernames of "Western Sahara"   ????????
# other_names_fil
# ter=[c.get("otherNames") for c in data if c.get("name")=="Yemen"]
# print(other_names_filter)

#  q17-->print english speaking countries????????????????????
# q18-->print all country name where native name and language name are same eg:native_name=english and name=english(languages)
# q19-->largest country based on area
# def get_area(dictionary):
#     return dictionary.get("area")
# largest_area=max(data,key=(get_area))
# print(largest_area)


# q20-->smallest country
# q21-->print all currency details of India
# q22-->print othernames of "Western Sahara"   ????????
