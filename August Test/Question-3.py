#Given a dictionary get all values from the dictionary and add it in a list but don’t add duplicates.
#speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
speed  ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53,
          'july':54, 'Aug':44, 'Sept':54} 

print("Dictionary's values - ", speed.values())

speedList = list()
for item in speed.values():
  if item not in speedList:
    speedList.append(item)
print("unique list", speedList)