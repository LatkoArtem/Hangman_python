import os
folder_name_to_find = 'archive'
folder_path = None
for root, dirs, files in os.walk('/'): 
    if folder_name_to_find in dirs:  
        folder_path = os.path.join(root, folder_name_to_find)
if folder_path:
    males_names = {} 
    females_names = {}
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            with open(os.path.join(folder_path, file_name), 'r') as file:
                male_names = {}
                female_names = {}
                for line in file:
                    name, sex, occurrences = line.strip().split(',')
                    occurrences = int(occurrences)
                    if sex == "M":
                        if name in male_names:
                            male_names[name] += occurrences
                        else: 
                            male_names[name] = occurrences
                    elif sex == "F":
                        if name in female_names:
                            female_names[name] += occurrences
                        else: 
                            female_names[name] = occurrences          
                most_popular_male_name = max(male_names, key=male_names.get)
                if most_popular_male_name:
                    if most_popular_male_name in males_names:
                        males_names[most_popular_male_name] += 1
                    else:
                        males_names[most_popular_male_name] = 1
            
                most_popular_female_name = max(female_names, key=female_names.get)
                if most_popular_female_name:
                    if most_popular_female_name in females_names:
                        females_names[most_popular_female_name] += 1
                    else:
                        females_names[most_popular_female_name] = 1
                    
males_names = dict(sorted(males_names.items(), key=lambda item: item[1], reverse=True))
females_names = dict(sorted(females_names.items(), key=lambda item: item[1], reverse=True))

print("Males:")
for name, count in males_names.items():
    print(f"{name}: {count}")

print("\nFemales:")
for name, count in females_names.items():
    print(f"{name}: {count}")