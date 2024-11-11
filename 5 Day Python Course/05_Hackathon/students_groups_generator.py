# Standard packages
import random
# Third party packages
# Custom packages

random.seed(a=0)


# %% User Inputs
list_of_students = ["Student1",
                    "Student2",
                    "Student3",
                    "Student4",
                    "Student5",
                    "Student6",
                    "Student7",
                    ]

number_of_groups = 2

# %% Calculations
students_per_group = int(round(len(list_of_students)/number_of_groups, 0))

fading_list = list_of_students.copy()
grouped_students = dict()
for i in range(number_of_groups):
    if i < number_of_groups-1 and len(fading_list) >= students_per_group:
        generated_group = random.sample(fading_list, k=students_per_group)
        grouped_students[f"group_{i+1}"] = generated_group
        fading_list = [x for x in fading_list if x not in generated_group]
    else:
        grouped_students[f"group_{i+1}"] = fading_list.copy()

# %% Double check all students are assigned
# This cell will error out and stop the program if a student is not assigned
assigned_students = []
for x in list(grouped_students.values()):
    assigned_students = assigned_students + x
assert len(list_of_students) == len(set(assigned_students))

# %% Show Results
print(f"\nNumber of students: {len(list_of_students)}")
print(f"Number of groups: {number_of_groups}")
print(f"Students per group: {students_per_group} / {[len(list(x)) for x in grouped_students.values()]}\n")
for key in grouped_students.keys():
    print(f"{key}: {grouped_students[key]}")
