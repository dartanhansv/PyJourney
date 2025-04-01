from datetime import datetime


def calculate_age(birth_date):
    today = datetime.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        days += (
            birth_date.replace(month=birth_date.month + 1, day=1)
            - birth_date.replace(month=birth_date.month, day=1)
        ).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days


def main():
    birth_date_input = input("Enter your birth date (MM/DD/YYYY): ")
    try:
        birth_date = datetime.strptime(birth_date_input, "%m/%d/%Y")
        years, months, days = calculate_age(birth_date)
        print(f"Your age is: {years} years, {months} months, and {days} days.")
    except ValueError:
        print("Invalid date format. Please use MM/DD/YYYY.")


if __name__ == "__main__":
    main()
