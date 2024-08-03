#dictionary is a key-value pair data collection
dict = {"Name" : "Chidozie Okezie", "Age" : 36, "Nationality" : "Nigerian"}
print(dict)
for key, value in dict.items():
    print(f"My {key} is: {value}")
#List
skills = ["Python", "Therapy and Rehabilitation", "Clinical Optometry"]
skills_len = len(skills)
print("My skills are: ")
for i in range(skills_len):
    print(f" * {skills[i]}")


