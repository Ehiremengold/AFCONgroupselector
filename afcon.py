from random import choice
countries = ["benin","cameroon", "algeria", "angola", "burundi", "DR congo", "egypt", "ghana", "guinea", "guinea-bissau", "ivory coast",
             "kenya", "madagascar", "mali", "mauritania", "morocco", "namibia", "nigeria", "senegal",
             "southafrica", "tanzania", "tunisia", "uganda", "zimbabwe"]

groupname = ["groupA", "groupB", "groupC", "groupD"]

teamA = []
teamB = []
teamC = []
teamD = []
teamE = []
teamF = []

while len(countries) > 0:
    countryA = choice(countries)
    teamA.append(countryA)
    countries.remove(countryA)

    if countries == []:
        break

    countryB = choice(countries)
    teamB.append(countryB)
    countries.remove(countryB)

    countryC = choice(countries)
    teamC.append(countryC)
    countries.remove(countryC)

    countryD = choice(countries)
    teamD.append(countryD)
    countries.remove(countryD)

    countryE = choice(countries)
    teamE.append(countryE)
    countries.remove(countryE)

    countryF = choice(countries)
    teamF.append(countryF)
    countries.remove(countryF)

print('Group A',teamA)
print('Group B',teamB)
print('Group C',teamC)
print('Group D',teamD)
print('Group E',teamE)
print('Group F',teamF)
