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


# q5-->print all countries under region asia

region_filter=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(region_filter)

#q6--> print all countries where timezone="UTC+04:30"
timezone_filter=[c.get("name") for c in data if "UTC-04:00" in c.get("timezones")]
# print(timezone_filter)

#q7--> print borders of "China"
borders_filter=[c.get("borders") for c in data if c.get("name")=="China"]
# print(borders_filter[0])


# q8-->print all independent countries
independent_countries=[c.get("name") for c in data if c.get("independent")==True]
# print(independent_countries)

# q9-->print total no.of independent countries
# print(len(independent_countries))

#q10--> print largest population country
def get_population(dictionary):
    return dictionary.get("population")
largest_population=max(data,key=get_population)
# print(largest_population.get("name"))


# q11-->print smallest population country
smallest_population=min(data,key=lambda dictionary:dictionary.get("population"))
# print(smallest_population.get("name"))


# q12-->print all countries where subregion="Western Asia"
subregion_filter=[c.get("name")for c in data if c.get("subregion")=="Western Asia"]
# print(subregion_filter)


# q13-->print languages of Uganda
lang_filter=[c.get("languages") for c in data if c.get("name")=="Uganda"]
# print(lang_filter)

#q14--> print countries  that include Indian border
indian_borders=[c.get("name") for c in data if "borders" in c and "IND" in c.get("borders")]
# print(indian_borders)

#q15-->country name with languages

# values={}
# for c in data:
#     lang_list=[]
#     if "languages" in c:
#         for l in c.get("languages"):
#             lang_list.append(l.get("name"))
            # print(lang_list)
        # values[c.get("name")]=lang_list
# print(values.get("India"))
# print(values)

#q16--> countries with Indian rupee
# for c in data:
#     if "currencies" in c:
#         for cur in c.get("currencies"):
#             if cur.get("name")=="Indian rupee":
#                 print(c.get("name"))

# q17-->all countries with multiple timezones
timezone_filter2=[c.get("name") for c in data if len(c.get("timezones"))>1]
# print(timezone_filter2)

# q18-->countrie names starts with A
name_filter=[c.get("name") for c in data if c.get("name").startswith("Af")]
# print(name_filter)

# q19-->region wise count eg: asia=50

# region_filter2=[c.get("name") for c in data if c.get("region")=="Polar"]
# print(region_filter2)

# method1
# region=[c.get("region") for c in data]
# wc={r:region.count(r) for r in set(region)}
# print(wc)

# method2
region_list=[]

for c in data:
    region_list.append(c.get("region"))
# print(region_list)

rc={r:region_list.count(r) for r in set(region_list)}
print(rc)

india_timezone=[c.get("timezones") for c in data if c.get("name")=="India"]  
print(india_timezone[0][0])
time_zone_india=india_timezone [0][0]    

afg_timezone=[c.get("timezones") for c in data if c.get("name")=="Afghanistan"]  
print(afg_timezone[0][0]) 
time_zone_afg=afg_timezone[0][0]

india_offset=time_zone_india.lstrip("UTC").replace(":",".")
print(india_offset)

afg_offset=time_zone_afg.lstrip("UTC").replace(":",".")
# print(afg_offset)

# if india_offset>afg_offset:
#     print("Indian timezone ahead of Afghanistan timezone")
# else:
#     print("Indian timezone behind of Afghanistan timezone")

from datetime import datetime,timedelta
offset_india=timedelta(hours=float(india_offset))
print("india offset",offset_india)
offset_usa=timedelta(hours=float(afg_offset))
print("usa offset",offset_usa)

time_country1=datetime.utcnow()+offset_india
print("first",time_country1)

time_country2=datetime.utcnow()+offset_usa
print("second",time_country2)

time_diff=time_country1-time_country2
print("time fifference:",time_diff.total_seconds())

if time_diff.total_seconds()>0:
    print("ahead")
else:
    print("behind")











        
         







