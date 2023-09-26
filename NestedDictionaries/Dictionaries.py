x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]["last_name"] = "Bryant"
sports_directory["soccer"][0] = "Andres"
z[0]["y"] = 30

print(x)
print(students[0])
print(sports_directory)
print(z)
print("1^------------------------------")

students1 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students1):
    for names in students1:
        print(names)

iterateDictionary(students1)
print("2^------------------------------")

def iterateDictionary2(key_name,some_list):
    for names1 in students1:
        print(names1[key_name])
#     print(students1[0][key_name])
#     print(students1[1][key_name])
#     print(students1[2][key_name])
#     print(students1[3][key_name])

iterateDictionary2('first_name',students1)
print("-----")
iterateDictionary2('last_name',students1)
print("3^------------------------------")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(search):
    print(len(dojo['locations']), "Locations")
    for x in dojo['locations']:
        print(x)
    print(len(dojo['instructors']), "Instructors")
    for y in dojo['instructors']:
        print(y)

printInfo(dojo)