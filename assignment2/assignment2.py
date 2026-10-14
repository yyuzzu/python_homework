import csv
import os
import traceback
import custom_module
from datetime import datetime


# Task 2: Read a CSV file
def read_employees():
    result = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for index, row in enumerate(reader):
                if index == 0:
                    result["fields"] = row
                else:
                    rows.append(row)

        result["rows"] = rows
        return result

    except Exception as e:
        print(f"An exception occurred. {type(e).__name__}")
        print(f"Exception message: {e}")
        traceback.print_exc()
        raise SystemExit(1)


employees = read_employees()
print(employees)


# Task 3: Find the column index
def column_index(column_name):
    return employees["fields"].index(column_name)


employee_id_column = column_index("employee_id")


# Task 4: Find the employee's first name
def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]


# Task 5: Find an employee using a nested function
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))
    return matches


# Task 6: Find an employee using a lambda
def employee_find_2(employee_id):
    matches = list(
        filter(
            lambda row: int(row[employee_id_column]) == employee_id,
            employees["rows"],
        )
    )
    return matches


# Task 7: Sort rows by last name
def sort_by_last_name():
    last_name_column = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]


sort_by_last_name()
print(employees)


# Task 8: Create a dictionary for one employee
def employee_dict(row):
    result = {}

    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            result[field] = row[index]

    return result


print(employee_dict(employees["rows"][0]))


# Task 9: Create a dictionary of all employees
def all_employees_dict():
    result = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        result[employee_id] = employee_dict(row)

    return result


print(all_employees_dict())


# Task 10: Read an environment variable
def get_this_value():
    return os.getenv("THISVALUE")


# Task 11: Set the secret in the custom module
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


set_that_secret("hello!")
print(custom_module.secret)


# Task 12: Read both minutes files
def read_minutes():
    def read_file(filename):
        result = {}
        rows = []

        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)

            for index, row in enumerate(reader):
                if index == 0:
                    result["fields"] = row
                else:
                    rows.append(tuple(row))

        result["rows"] = rows
        return result

    minutes1 = read_file("../csv/minutes1.csv")
    minutes2 = read_file("../csv/minutes2.csv")
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)


# Task 13: Combine the rows into a set
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)


minutes_set = create_minutes_set()


# Task 14: Convert date strings to datetime objects
def create_minutes_list():
    rows = list(minutes_set)

    converted_rows = list(
        map(
            lambda row: (
                row[0],
                datetime.strptime(row[1], "%B %d, %Y"),
            ),
            rows,
        )
    )

    return converted_rows


minutes_list = create_minutes_list()
print(minutes_list)


# Task 15: Sort by date and write the CSV file
def write_sorted_list():
    minutes_list.sort(key=lambda row: row[1])

    converted_list = list(
        map(
            lambda row: (
                row[0],
                datetime.strftime(row[1], "%B %d, %Y"),
            ),
            minutes_list,
        )
    )

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)

    return converted_list


write_sorted_list()
