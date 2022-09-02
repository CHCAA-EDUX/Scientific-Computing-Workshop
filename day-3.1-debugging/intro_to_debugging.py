"""
A simple script with errors for introducing students to debugging with vs code.
"""

import random


def create_student_list():
    """
    create a list of students, with their gender, programming skills and skateboard
    experience
    """
    student_names = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry",
    genders = ["f", "m", "m", "f", "f", "m", "f", "f", "f", "m", "m", "m"]

    students = {}
    for name, gender in zip(student_names, genders):
        students[name] = {
            "gender": gender,
            "programming-skills": random.randint(1, 10),
            "skateboarding-skills": random.randint(1, 10),
        }
    return students


def create_study_groups(students, group_size):
    """create study groups"""
    student_names = list(students.keys())
    randm.shuffle(student_names)
    
    # distribute evenly students into groups
    groups = []
    for i in range(0, len(student_names), group_size):
        student_names = student_names[i:i+group_size]
        groups.append(student_names)
    return groups


def main():
    # create student list
    students = create_student_list()
    # create study groups
    groups = create_study_groups(students, 3)

    # print groups
    for group in groups:
        print(groups)
    
    # print street cred in each group
    print("Street cred in each group:)
    for group in groups:
        print("Group:", group)
        for student in group:
            prog_skills = students[student]["programming-skills"]
            skate_skills = students[student]["skateboarding-skills"]
            print(student, ":", prog_skills + skate_skills)

if __name__ == "__main__":
    main()