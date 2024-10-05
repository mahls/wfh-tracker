import csv
import pickle
import os

# File paths
DATA_FILE = 'employees.pkl'
CSV_FILE = 'employees.csv'

# Data Structure: Dictionary to store employee records
# Example record: {'employee_id': {'name': 'John Doe', 'week': 34, 'hours': [8, 8, 7, 8, 6]}}

def load_data():
    print("Loading data...")
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'rb') as file:
            data = pickle.load(file)
            print(f"Data loaded: {data}")
            return data
    return {}

def save_data(data):
    print(f"Saving data: {data}")
    with open(DATA_FILE, 'wb') as file:
        pickle.dump(data, file)

def manipulate_string():
    while True:
        print("\nString Manipulation Options:")
        print("1. Convert name to uppercase")
        print("2. Convert name to lowercase")
        print("3. Capitalize name")
        print("4. Find and replace in name")
        print("5. Return to main menu")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name to convert to uppercase: ")
            print(name.upper())
        elif choice == '2':
            name = input("Enter name to convert to lowercase: ")
            print(name.lower())
        elif choice == '3':
            name = input("Enter name to capitalize: ")
            print(name.capitalize())
        elif choice == '4':
            name = input("Enter name: ")
            find = input("Enter text to find: ")
            replace = input("Enter text to replace with: ")
            print(name.replace(find, replace))
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

def add_employee(data):
    while True:
        print("\nAdd Employee and Hours (Type 'menu' at any time to return to the main menu)")

        week_number = input("Enter the current working week number: ")
        employee_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")

        hours_worked = []
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            while True:
                try:
                    hours = input(f"Enter hours worked on {day} (0-24): ")
                    hours = float(hours)
                    if hours < 0 or hours > 24:
                        print("Hours must be between 0 and 24. Please enter a valid number.")
                        continue
                    hours_worked.append(hours)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value for hours.")

        data[employee_id] = {
            'name': name,
            'week': week_number,
            'hours': hours_worked
        }

        total_hours = sum(hours_worked)
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        for i, day in enumerate(days_of_week):
            if hours_worked[i] < 4:
                print(f"Insufficient hours worked on {day}")
            elif hours_worked[i] > 10:
                print(f"Too many hours worked on {day}")

        if total_hours < 30:
            print("You didn’t do enough work this week")
        elif total_hours > 40:
            print("You are working too hard!!")

        print(f"Updated hours for {name}: {hours_worked}")
        save_data(data)

        another = input("Do you want to add another employee? (yes to continue, 'menu' to return to the main menu): ")
        if another.lower() == 'menu':
            return

def read_employees(data):
    print("Reading employees data...")
    if not data:
        print("No data available.")
    else:
        print("Employee Records:")
        for emp_id, details in data.items():
            hours = details['hours']
            print(f"ID: {emp_id}, Name: {details['name']}, Week: {details['week']}")
            print(f"Hours Worked: Monday: {hours[0]}, Tuesday: {hours[1]}, Wednesday: {hours[2]}, Thursday: {hours[3]}, Friday: {hours[4]}")
    input("Press Enter to return to the main menu...")

def save_to_csv(data):
    print(f"Data to be saved to CSV: {data}")
    filter_choice = input("Do you want to filter data before saving? (yes/no): ").strip().lower()
    
    filtered_data = data
    if filter_choice == 'yes':
        employee_id = input("Enter employee ID to export (leave blank to export all): ").strip()
        if employee_id:
            filtered_data = {eid: details for eid, details in data.items() if eid == employee_id}

    with open(CSV_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Employee ID', 'Employee Name', 'Week Number', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
        for emp_id, details in filtered_data.items():
            writer.writerow([
                emp_id,
                details['name'],
                details['week'],
                *details['hours']
            ])
    print(f"Data saved to {CSV_FILE}")
    input("Press Enter to return to the main menu...")

def delete_employee(data):
    while True:
        print("\nDelete Employee (Type 'menu' at any time to return to the main menu)")
        employee_id = input("Enter the ID of the employee to delete: ")
        if employee_id.lower() == 'menu':
            return

        if employee_id in data:
            del data[employee_id]
            print(f"Deleted employee with ID: {employee_id}")
            save_data(data)
        else:
            print("Employee not found.")

        another = input("Do you want to delete another employee? (yes to continue, 'menu' to return to the main menu): ")
        if another.lower() == 'menu':
            return

def generate_weekly_report(data):
    less_than_30 = 0
    more_than_40 = 0
    between_37_and_39 = 0

    for details in data.values():
        total_hours = sum(details['hours'])

        if total_hours < 30:
            less_than_30 += 1
        elif total_hours > 40:
            more_than_40 += 1
        elif 37 <= total_hours <= 39:
            between_37_and_39 += 1

    print("\nWeekly Employee Report:")
    print(f"Number of employees who worked less than 30 hours a week: {less_than_30}")
    print(f"Number of employees who worked more than 40 hours a week: {more_than_40}")
    print(f"Number of employees who worked between 37-39 hours: {between_37_and_39}")

def menu():
    data = load_data()
    while True:
        print("\nEmployee Work Tracker")
        print("1. Add Employee and Hours")
        print("2. Read All Employees and Their Hours")
        print("3. Save Data to CSV")
        print("4. Generate Weekly Report")
        print("5. String Manipulation")
        print("6. Delete Employee")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_employee(data)
        elif choice == '2':
            read_employees(data)
        elif choice == '3':
            save_to_csv(data)
        elif choice == '4':
            generate_weekly_report(data)
        elif choice == '5':
            manipulate_string()
        elif choice == '6':
            delete_employee(data)
        elif choice == '7':
            save_data(data)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")

if __name__ == '__main__':
    menu()
