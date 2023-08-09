import csv

filename = "Tree-In.txt"
with open(filename, "r") as f:
    lines = f.readlines()

# Initialize the dict of people
people = {}

#bool statements used to confirm if a line has been done or not
name_line = True    # default true bc first thing on list is a name
year_line = False   # only for getting school
teacher_line = False    # only for adding multiple extra teacher names

#initialize a count for those that are missing the indexing value
line_number = 0

for line in lines:
    line = line.strip()
    if line == "":
        name_line = True
        continue
    else:
        if name_line == True:
            #counter for number of teachers, anywhere from one to maximum of four
            i = 0
            # initializes a list of person's info, with name as first item in list
            person_info = [None, None, None, None, None, None, None, None, None, None, None, None]
            person = line
            people[person] = person_info
            person_info[0] = person
            name_line = False
        elif teacher_line == True:
            if line.startswith("#") is not True:
                person_info[i+7] = line
                if i < 4:
                    i += 1
            else:
                line_number += 1
                if line == "#":
                    line_to_add = "#" + str(line_number)
                    #print("line to add: ", line_to_add)
                    person_info[11] = line_to_add
                else:
                    person_info[11] = line
                teacher_line = False
        else:
            if line[0:3].isnumeric():   # checks year
                person_info[1] = line
                year_line = True
            elif year_line == True: # checks school by seeing if it comes after year
                person_info[2] = line
                year_line = False
            elif line.startswith('"'):  # checks thesis
                person_info[3] = line
            elif "@" in line:   # checks email
                person_info[4] = line
            elif line.startswith("http"):   # checks website
                person_info[5] = line
            elif line.startswith("loc:"):    # checks location
                line_to_insert = line[6:]
                person_info[6] = line_to_insert
            elif line == "T:":  # checks teacher list
                teacher_line = True
            elif line.startswith("#"):  # checks number
                line_number += 1
                if line == "#":
                    line_to_add = "#" + str(line_number)
                    #print("line to add: ", line_to_add)
                    person_info[11] = line_to_add
                else:
                    person_info[11] = line
        #print("line: ", line)
        #print("person info: ", person_info)

#for key, value in people.items():
#    print("key: ", key, "value: ", value)

# Convert dict values to list for csv writer
people_list = [person_info for person_info in people.values()]

# Write to csv file
with open("Test-Tree-Out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Year", "School", "Thesis", "Email", "Website", "Location", "Teacher 1", "Teacher 2", "Teacher 3", "Teacher 4", "#"])
    for person_info in people_list:
        writer.writerow(person_info)

print("all done!")
