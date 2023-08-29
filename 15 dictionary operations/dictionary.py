dic={'key1':'value1','key2':'value2'}#dictionary declaration

dic1={'name':'vaithi','age':20}

print(dic1)#print the whole

print(dic1.keys())# print keys

print(dic1.values())#print values


print(dic1.items())#items in list

print(dic1["name"])# prints the specific key s value

dic1.update({"height":7.7})

print(dic1)


dic1["name"]="vinslin"
dic1[7.7]="weight"

print(dic1)

dic1.update({"fav_sports":"kabadi"})

print(dic1)


##copy a dict

new=dic1.copy()


print("\n\n\n",new)


#remove a element from dictionary

new.pop('name')
print("\n\n\n",new)


del new['age']
print("\n\n\n",new)


new.clear()

print("\n\n",new)



















