# list

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
print(everything)