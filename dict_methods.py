dict = {
    'value': 'key',
    'name': 'Kuba',
    'hobby': 'planszowki',
    'fav_color': 'green'
    }
print(dict)

# .get method RETURNS default value if key doesn't exist. If it exists it returns true value 
print(dict.get('adres','Wilanow')) 
print(dict)

# .setdefault method ADDS default value if key doesn't exist. If it exists it returns true value 
dict.setdefault('adres','Wilanow')
print(dict)
dict.setdefault('adres','Warszawa')
print(dict)