# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#print names
print(names)

# write your update damages function here:
def update_damages(list):
    updated_damages = []
    for record in list:
        if record == "Damages not recorded":
            updated_damages.append(record)
        else:
            if record[len(record)-1] == "M":
                temp = float(record[0:len(record)-1]) * 1000000
                updated_damages.append(temp)
            elif record[len(record)-1] == "B":
                temp = float(record[0:len(record)-1]) * 1000000000
                updated_damages.append(temp)
    return updated_damages

damages_in_float = update_damages(damages)

# write your construct hurricane dictionary function here:
def build_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    dictionary = {}
    for i in range(len(names)):
        dictionary[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Deaths": deaths[i]}
    return dictionary

hurricanes_dictionary = build_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_in_float, deaths)

# write your construct hurricane by year dictionary function here:
def organize_by_year(dictionary):
    years = {}
    for value in hurricanes_dictionary.values():
        if not value["Year"] in years:
            years[value["Year"]] = []
    for value in hurricanes_dictionary.values():
        years[value["Year"]].append(value)
    return years

hurricanes_by_year = organize_by_year(hurricanes_dictionary)

# write your count affected areas function here:
def count_area(hurricanes):
    by_area = {}
    #Create a key in by_area for each area present in the dictionary
    #Loop through each value in the dictionary
    for value in hurricanes_dictionary.values():
        #Loop through each Areas Affected key in the subdictionary
        for area in value["Areas Affected"]:
            #Areas Affected contains a list. Iterate through each index in the list, and if it isn't present as a key in by_area,
            #add it with a value of 0
            if not area in by_area:
                by_area[area] = 0
    #Loop again through the dictionary, this time to count how many times an area is repeated
    for value in hurricanes_dictionary.values():
        for area in value["Areas Affected"]:
            by_area[area] += 1
    return by_area

count_area = count_area(hurricanes_dictionary)

# write your find most affected area function here:
def find_most_affected_area(hurricanes):
    biggest = ('', 0)
    for pair in count_area.items():
        if pair[1] > biggest[1]:
            biggest = pair
    print("The most affected area is {area} with {times} hurricanes.".format(area=biggest[0], times=biggest[1]))
    
find_most_affected_area(hurricanes_dictionary)

# write your greatest number of deaths function here:
def find_most_deadly(hurricanes):
    most_deadly = ('', 0)
    for name_key in hurricanes:
        if hurricanes[name_key]["Deaths"] > most_deadly[1]:
            most_deadly = (name_key, hurricanes[name_key]["Deaths"])
    print("{name} caused the greatest number of deaths with {deaths} deaths.".format(name=most_deadly[0], deaths=most_deadly[1]))
    
find_most_deadly(hurricanes_dictionary)

# write your catgeorize by mortality function here:
def rate_by_mortality(hurricanes_dictionary):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}

    by_mortality_rating = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    for hurricane in hurricanes_dictionary:
        if (hurricanes_dictionary[hurricane]["Deaths"] == 0):
            by_mortality_rating[0].append(hurricanes_dictionary[hurricane])
        elif (hurricanes_dictionary[hurricane]["Deaths"] > mortality_scale[0]) and (hurricanes_dictionary[hurricane]["Deaths"] <= mortality_scale[1]):
            by_mortality_rating[1].append(hurricanes_dictionary[hurricane])
        elif (hurricanes_dictionary[hurricane]["Deaths"] > mortality_scale[1]) and (hurricanes_dictionary[hurricane]["Deaths"] <= mortality_scale[2]):
            by_mortality_rating[2].append(hurricanes_dictionary[hurricane])
        elif (hurricanes_dictionary[hurricane]["Deaths"] > mortality_scale[2]) and (hurricanes_dictionary[hurricane]["Deaths"] <= mortality_scale[3]):
            by_mortality_rating[3].append(hurricanes_dictionary[hurricane])
        elif (hurricanes_dictionary[hurricane]["Deaths"] > mortality_scale[3]) and (hurricanes_dictionary[hurricane]["Deaths"] <= mortality_scale[4]):
            by_mortality_rating[4].append(hurricanes_dictionary[hurricane])
        elif (hurricanes_dictionary[hurricane]["Deaths"] >= mortality_scale[4]):
            by_mortality_rating[5].append(hurricanes_dictionary[hurricane])
        
    return by_mortality_rating
    
rate_by_mortality(hurricanes_dictionary)

# write your greatest damage function here:
#let's find the hurricane that caused the biggest damage
def find_greatest_damage(hurricanes):
    greatest_damage = ('', 0)
    for name in hurricanes:
        if hurricanes[name]["Damage"] == "Damages not recorded":
            None
        elif hurricanes[name]["Damage"] > greatest_damage[1]:
            greatest_damage = (name, hurricanes[name]["Damage"])
            
    return "{name} caused the greatest damage with a cost of {damage} dollars.".format(name=greatest_damage[0], damage=greatest_damage[1])

#Call the function with the dictionary
find_greatest_damage(hurricanes_dictionary)

# write your catgeorize by damage function here:
def rate_by_damage(hurricanes_dictionary):
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

    by_damage_rating = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    for hurricane in hurricanes_dictionary:
        if (hurricanes_dictionary[hurricane]["Damage"] == 0):
            by_mortality_rating[0].append(hurricanes_dictionary[hurricane])
        elif (hurricanes_dictionary[hurricane]["Damage"] > damage_scale[0]) and (hurricanes_dictionary[hurricane]["Damage"] <= damage_scale[1]):
            by_mortality_rating[1].append(hurricanes_dictionary[hurricane])
        elif (hurricanes_dictionary[hurricane]["Damage"] > damage_scale[1]) and (hurricanes_dictionary[hurricane]["Damage"] <= damage_scale[2]):
            by_mortality_rating[2].append(hurricanes_dictionary[hurricane])
        elif (hurricanes_dictionary[hurricane]["Damage"] > damage_scale[2]) and (hurricanes_dictionary[hurricane]["Damage"] <= damage_scale[3]):
            by_mortality_rating[3].append(hurricanes_dictionary[hurricane])
        elif (hurricanes_dictionary[hurricane]["Damage"] > damage_scale[3]) and (hurricanes_dictionary[hurricane]["Damage"] <= damage_scale[4]):
            by_mortality_rating[4].append(hurricanes_dictionary[hurricane])
        elif (hurricanes_dictionary[hurricane]["Damage"] >= damage_scale[4]):
            by_mortality_rating[5].append(hurricanes_dictionary[hurricane])
        
    return by_damage_rating
    
rate_by_mortality(hurricanes_dictionary)