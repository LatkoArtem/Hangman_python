import json
import csv

with open('image_info_test-dev2017.json', 'r') as f:
    data = json.load(f)
    
images = ["license", "file_name", "coco_url", "height", "width", "date_captured", "id"]
licenses = ["url", "id", "name"]
categories = ["supercategory", "id", "name"]

with open("images.csv", "w", newline="", encoding="utf-8") as images_csv:
    images_writer = csv.DictWriter(images_csv, fieldnames=images)
    images_writer.writeheader()
    for image in data["images"]:
        images_writer.writerow(image)
        
with open("licenses.csv", "w", newline="", encoding="utf-8") as licenses_csv:
    licenses_writer = csv.DictWriter(licenses_csv, fieldnames=licenses)
    licenses_writer.writeheader()
    for license in data["licenses"]:
        licenses_writer.writerow(license)

with open("categories.csv", "w", newline="", encoding="utf-8") as categories_csv:
    categories_writer = csv.DictWriter(categories_csv, fieldnames=categories)
    categories_writer.writeheader()
    for category in data["categories"]:
        categories_writer.writerow(category)