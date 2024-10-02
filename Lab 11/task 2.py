import os
import time

folder_name = 'archive'
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
folder_path = os.path.join(current_dir, folder_name)
files = os.listdir(folder_path)

def func_decorator_main(func):
    def inner():
        start_func = time.time()
        func()
        end_func = time.time()
        func_time = end_func - start_func
        print()
        print(f"Execution time of the main body: {func_time}")
    return inner

@func_decorator_main
def main_code():
    males_names = {} 
    females_names = {}
    for file_name in files:
        if file_name.endswith(".txt"):
            with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as file:
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
        
main_code()