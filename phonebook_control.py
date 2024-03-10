"""control module"""

from collections import UserDict, defaultdict
from datetime import datetime


class Field:
    """basic class for records fields"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    """stores contacts name"""

    def __init__(self, name=str):
        super().__init__(name)


class Phone(Field):
    """stores phone number"""

    def __init__(self, phone=str):
        if len(phone) != 10 or not phone.isdigit():
            raise ValueError("🤫 Phone number must have 10 digits")
        super().__init__(phone)


class Birthday(Field):
    """stores contacts birthday"""

    def __init__(self, birthday):
        try:
            datetime.strptime(birthday, "%d.%m.%Y")
        except ValueError:
            raise ValueError("🙄 Birthday format should be DD.MM.YYYY")
        super().__init__(birthday)


class Record:
    """stores contact including name and phones list"""

    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.birthday = Birthday(birthday) if birthday else None
        self.phones = []

    def add_phone(self, phone):
        """adds phone number to record"""
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        """removes phone number from record"""
        for p in self.phones:
            print(p)
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, new_phone):
        """edits phone number in record"""
        self.phones[0] = Phone(new_phone)

    def find_phone(self, phone):
        """finds phone number in record"""
        for p in self.phones:
            if p.value == phone:
                return p

    def add_birthday(self, birthday):
        """adds birthday in record"""
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"


class AddressBook(UserDict):
    """containing and controlling records in Address book"""

    def add_record(self, record):
        """adds record to Address book"""
        self.data[record.name.value] = record

    def find(self, name):
        """finds record in Address book"""
        for contact_name, record in self.data.items():
            if contact_name.lower() == name.lower():
                return record
        return None

    def delete(self, key):
        """deletes record from Address book"""
        if key in self.data:
            del self.data[key]

    
   