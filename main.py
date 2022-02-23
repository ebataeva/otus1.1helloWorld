import json
from _csv import reader


class Users:

    def __init__(self) -> None:
        self.new_users = []
        self.index = 0
        super().__init__()

    with open('users.json', 'r') as json_data:
        users = json.load(json_data)
        new_users = []
        for i in users:
            new_users.append(
                {'name': i['name'], 'gender': i['gender'], 'address': i['address'], 'age': i['age'], 'books': []})

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.new_users):
            self.index = 0

        result = self.new_users[self.index]
        self.index += 1
        return result


class Books:
    with open('books.csv') as csv_data:
        header = next(reader(csv_data))
        new_books = []
        for row in reader(csv_data):
            new_books.append(dict(zip(header, row)))


class Main(Users, Books):

    def __init__(self) -> None:
        super().__init__()

    Users.new_users[0]['books'].append(dict(Books.new_books[0]))

    print(Users.new_users[0])
    count_books = len(Books.new_books)
    count_users = len(Users.new_users)
    least = count_books / count_users
    print(count_books, count_users, least)
    print(next(iter(Users.new_users)))
    for i in range(len(Users.new_users) + 5):
        print(Users.new_users[i])

    with open('result_json.json', 'w') as result:
        result_data = json.dumps(Users.new_users, indent=4)
        result.write(result_data)
