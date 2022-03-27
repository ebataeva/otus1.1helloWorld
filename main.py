import csv
import json


class Users:
    with open("users.json", 'r') as json_file:
        json_data = json.loads(json_file.read())

    json_list = []
    for i in json_data:
        json_list.append({'name': i['name'], 'gender': i['gender'], 'age': i['age'], 'address': i['address']})

    with open('books.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        csv_list = []
        for row in reader:
            csv_list.append(dict(zip(header, row)))

    result_list = []
    for json_el in json_list:
        result_list.append(
            {
                "name": json_el['name'],
                "gender": json_el['gender'],
                "address": json_el['address'],
                "age": json_el['age'],
                "books": []
            }
        )

    readers_count = len(result_list)
    reader_index = 0
    for csv_el in csv_list:
        result_list[reader_index]['books'].append(
            {
                "title": csv_el['Title'],
                "author": csv_el['Author'],
                "pages": int(csv_el['Pages']),
                "genre": csv_el['Genre']
            }
        )
        reader_index += 1
        if reader_index >= readers_count:
            reader_index = 0

    with open('result.json', 'w') as result_json:
        result_data = json.dumps(result_list, indent=4)
        result_json.write(result_data)
