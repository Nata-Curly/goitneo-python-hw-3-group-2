"""handlers module"""

from phonebook_control import Record
from datetime import datetime, timedelta

def input_error(func):
    """decorator for exceptions"""

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "🙃 Give me name and phone please."
        except KeyError:
            return "🙄 Contact not found."
        except IndexError:
            return "🙃 Give me name and phone please."

    return inner


def parse_input(user_input):
    """parses commands"""
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args


@input_error
def add_contact(args, contacts):
    """adds contacts in format: 'name':'phone'"""
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return f"✌️ Contact {name} added."


@input_error
def change_contact(args, contacts):
    """changes contact's phone"""
    name, new_phone = args
    record = contacts.find(name)
    record.edit_phone(new_phone)
    return f"👌 Contact {name} changed."


@input_error
def show_all(contacts):
    """shows all contacts"""
    if len(contacts) > 0:
        result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return result
    else:
        return "🫤 Contacts not found."


@input_error
def show_phone(args, contacts):
    """shows phone of specific name"""
    if len(args) == 1:
        name = args[0].lower()
        record = contacts.find(name)
        if record:
            if record.phones:
                phone = record.phones[0].value
                return f"📱 {record.name.value}`s phone is {phone}"
        else:
            return f"😳 Contact {args[0]} not found."


@input_error
def add_birthday(args, contacts):
    """adds birth day to contact in format DD.MM.YYYY"""
    name, birthday = args
    record = contacts.find(name)
    record.add_birthday(birthday)
    return f"👌 Birthday of {name} added."

@input_error
def show_birthday(args, contacts):
    """shoes birthday of contact"""
    if len(args) == 1:
        name = args[0]
        record = contacts.find(name)
        if record and record.birthday:
            return f"🎉 Birthday for {name}: {record.birthday.value}"
        elif record:
            return f"😒 There is no birthday for {name}."
        else:
            return f"😳 Contact {name} not found."


@input_error
def birthdays(contacts):
    """shoes list of contacts by weekday, who should be congratulated next week"""
    today = datetime.today()
    next_monday = today + timedelta(days=(7 - today.weekday()))
    next_monday = next_monday.replace(hour=0, minute=0, second=0, microsecond=0)
    next_sunday = next_monday + timedelta(days=6, hours=23, minutes=59, seconds=59)
    upcoming_birthdays = []

    for record in contacts.data.values():
        if record.birthday:
            birthday_date = datetime.strptime(record.birthday.value, "%d.%m.%Y")
            birthday_date = birthday_date.replace(year=today.year)

            if next_monday <= birthday_date <= next_sunday:
                upcoming_birthdays.append(
                    (record.name.value, birthday_date.strftime("%d.%m.%Y"))
                )

    if upcoming_birthdays:
        return "🎂 Congratulating this week:\n" + "\n".join(
            [f"{name}: {birthday}" for name, birthday in upcoming_birthdays]
        )
    else:
        return "😒 No birthday parties this week."
