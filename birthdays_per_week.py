from datetime import datetime, timedelta

users = {"Pavlo": datetime(1982, 7, 28),
         "Ivan": datetime(2007, 8, 3),
         "Olena": datetime(1956, 7, 30),
         "Max": datetime(1990, 7, 28),
         "Maria": datetime(1994, 7, 31),
         "Kateryna": datetime(1985, 8, 2),
         "Varvara": datetime(2012, 8, 24),
         "Prokop": datetime(1956, 7, 22)}

def get_birthdays_per_week(users):

    birthdays_weekdays_list = {
        0: [],  # Monday
        1: [],  # Tuesday
        2: [],  # Wednesday
        3: [],  # Thursday
        4: [],  # Friday
        5: [],  # Saturday
        6: []   # Sunday
        }

    current_date = datetime.now()
    # current_date = datetime(2023, 7, 24) # перевірка, якби сьогодні був понеділок
    interval = timedelta(days=7)
    weekend_interwal = timedelta(days=2)
    upcoming_date = current_date + interval
    
    # робимо словник, в якому будуть тільки ті люди, у яких ДР протягом наступних 7 днів:    
    
    for name, date in users.items():
        date = date.replace(year=current_date.year)

        if current_date <= date <= upcoming_date:
            day_of_week_num = datetime.weekday(date)   # вказуємо, що то за день тижня (date з рядку 31)
            birthdays_weekdays_list[day_of_week_num].append(name)
    
        if current_date.weekday() == 0 and current_date - weekend_interwal <= date < current_date: # якщо сьогодні понеділок
        # то вітаємо тих, у кого минулих вихідних був ДР, if any:
            birthdays_weekdays_list[0].append(name)

    # print(birthdays_weekdays_list) # перевірочний print

    dict_with_day_names = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"}
    
    for day in range(5): # 5, а не 7, бо без наступних вихідних
        name_of_the_day = dict_with_day_names[day]
        colleagues_to_greet = birthdays_weekdays_list[day]
        if colleagues_to_greet:
            print(f"{name_of_the_day}: {', '.join(colleagues_to_greet)}")

    
get_birthdays_per_week(users)
