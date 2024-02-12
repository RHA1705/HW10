'''Class system for address book management'''
from collections import UserDict

class Field:
    '''Parent class for others, common logic for all fields is implemented'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    '''A class for storing a contact name. Mandatory field.'''
    # реалізація класу
    pass

class Phone(Field):
    '''A class for storing a phone number. Has format validation (10 digits).'''
    # реалізація класу
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError
        super().__init__(value)

class Record:
    '''A class for storing information about a contact, including name and phone list.'''
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone:str):
        '''Add phone to record in self.data'''
        phone_object = Phone(phone)
        self.phones.append(phone_object)
        return phone_object

    def remove_phone(self, phone:str):
        '''Remove phone from record in self.data'''
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return p
            return None

    def edit_phone(self, phone:str, new_phone):
        '''Edit phone in record in self.data'''
        Phone(new_phone)
        for i in self.phones:
            if i.value == phone:
                i.value = new_phone
                return i
        raise ValueError

    def find_phone(self, phone:str):
        '''Remove phone from record in self.data'''
        for ph in self.phones:
            if ph.value == phone:
                return ph

    def __str__(self):
        return f"Contact name: {str(self.name)}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    '''A class for storing and managing records.'''
    # реалізація класу
    def add_record(self, record):
        '''Add a record to the address book.'''
        self.data[record.name.value] = record

    def find(self, name):
        '''Find a record by name.'''
        return self.data.get(name, None)


    def delete(self, name):
        '''Delete a record by name.'''
        if name in self.data:
            return self.data.pop(name)
        return None

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
