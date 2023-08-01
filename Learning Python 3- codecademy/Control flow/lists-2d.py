# 2d list with test scores from a classroom
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)
# Variable with value of Sam score (selecting the third list and the second index from that one)
sams_score = class_name_test[2][1]
print(sams_score)
# Variable with value of ellie score using negative values
ellies_score = class_name_test[-1][-1]
print(ellies_score)

# 2d list with name, nationality and grade level of students
incoming_class = [["Kenny","American",9], ["Tanya","Ukrainian",9],["Madison","Indian",7]]
# Update Madison grade to 8 using positive indexes
incoming_class[2][2] = 8
# Update Kenny name using negative indexes
incoming_class[-3][-3] = "Ken"
print(incoming_class)