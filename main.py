from collections import UserDict

class Field:
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
        if len(value) < 10 or len(value) > 10 or not value.isdigit():
            raise ValueError
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone:str):
        phone_object = Phone(phone)
        self.phones.append(phone_object)

    def remove_phone(self, phone:str):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, phone:str, new_phone):       
        for i in self.phones:         
            if i.value == phone:
                i.value = new_phone
        raise ValueError 
                  
    def find_phone(self, phone:str):
        for ph in self.phones:
            if ph.value == phone:
                return ph

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            return self.data.pop(name)