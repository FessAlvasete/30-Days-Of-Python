from countries import countries
len(countries)
print(len(countries))
countries_1 = countries[0:len(countries)//2]
countries_2 = countries[len(countries)//2+1:-1]
print('First pack:',countries_1)
print('Last pack:',countries_2)
TOP3 = countries[countries.index('China')], countries[countries.index('Russia')], countries[countries.index('United States')]
print(TOP3)