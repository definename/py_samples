import copy
empty_list = []
print(empty_list)

weekdayList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(weekdayList[0])

everything = [1, 2, 3, "one", "two", "three"]

listOfLists = [weekdayList, everything]
print("\tlistOfLists: ", listOfLists)
print("\t\t1st element of listOfLists: ", listOfLists[0])
print("\t\t\t1st element of the 1st elemtn of : ", listOfLists[0][3])

listOfLists[1][0] = 10
print("\t\t\t\tСhanged list of the listOfLists:", listOfLists)

everything.append("the end")
print(everything)

everything.extend(weekdayList)
print("Test extend:", everything)

del everything[-1]
print("Test del:", everything)

everything.remove("Monday")
print("Test del by name:", everything)

print("Test pop front:", everything.pop(0))
print("Test pop back:", everything.pop(0))
print("Pop result:", everything)

print("Index:", everything.index("Tuesday"))

print("Is 'the end' in everything list:", "the end" in everything)

print("Week days have been joined:", "-->".join(weekdayList))

numList = [1, 223, 545, 2, 34, 100, 190, 25, 31]
print("Sorted copy:", sorted(numList))
numList.sort()
print("Sort in place numeric list:", numList)

# create list copy (uses the same data via reference)
origin = [1, 2, 3]
copy0 = origin
origin[0] = "surprise"

# create one level copy of the given list (creates complete copy of the first level)
copy1 = origin.copy()
copy1[0] = 11
copy2 = list(origin)
copy2[0] = 12
copy3 = origin[:]
copy3[0] = 13

print(origin)
print(copy0)
print(copy1)
print(copy2)
print(copy3)

print()

# use copy module to create deeepcopy of the given list (copies all list levels)
l1 = [1, 2, [3, 4]]
l2 = l1.copy()

l1[2][0] = "copy"
print("l1 {} l2 {}".format(l1, l2))

l2 = copy.deepcopy(l1)
l1[2][0] = "nocopy"

print("l1 {} l2 {}".format(l1, l2))

# Replace list values

args = [999]
args[1:] = [1, 2, 3]
print(args)
args[1:] = [0, 1, 2, 3]
print(args)
