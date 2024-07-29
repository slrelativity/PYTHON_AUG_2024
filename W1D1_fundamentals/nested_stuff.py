# Dictionary of lists
resume_data = {
    "skills": ["front-end", "back-end", "database"],
    "languages": ["Python", "JavaScript"],
    "hobbies": ["rock climbing", "knitting"],
}

# print(resume_data["skills"][1])

# print all the skills
def print_all_skills(some_dict):
    for key, list_value in some_dict.items():
        # print(key, list_value)
        for each_item in list_value:
            print(each_item)

        


print_all_skills(resume_data)