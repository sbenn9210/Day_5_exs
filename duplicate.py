names = ["Alex","John","Mary","Steve","John", "Steve"]


#print the list to find the duplicate
print(names)
#print the list line by line
for name in names:
    print(name)
# look in the list to find the duplicate

#remove the duplicate

def remove(duplicate):
    no_duplicates_list = []
    for name in duplicate:
        if name not in no_duplicates_list:
            no_duplicates_list.append(name)
    print(no_duplicates_list)


remove(names)
