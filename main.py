''''''
from collections import UserDict

class Field:
    ''''''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    pass

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone:str):
        phone_object = Phone(phone)
        self.phones.append(phone_object)
        return phone_object

    def remove_phone(self, phone:str):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return p

    def edit_phone(self, phone:str, new_phone):
<<<<<<< HEAD
        Phone(new_phone)
        for i in self.phones:
            if i.value == phone:
                i.value = new_phone
                return i
=======
        for i in self.phones:
            if i.value == phone:
                i.value = new_phone
                return
>>>>>>> b1f512e34c0ef9eff88d40893bdad522f4dfc9d1
        raise ValueError

    def find_phone(self, phone:str):
        for ph in self.phones:
            if ph.value == phone:
                return ph

    def __str__(self):
        return f"Contact name: {str(self.name)}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
<<<<<<< HEAD
        return self.data.get(name, None)
=======
        return self.data.get(name)
>>>>>>> b1f512e34c0ef9eff88d40893bdad522f4dfc9d1

    def delete(self, name):
        if name in self.data:
            return self.data.pop(name)

if __name__ == '__main__':
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
<<<<<<< HEAD
=======
    
>>>>>>> b1f512e34c0ef9eff88d40893bdad522f4dfc9d1
