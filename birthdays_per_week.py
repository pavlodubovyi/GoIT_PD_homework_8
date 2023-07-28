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
    interval = timedelta(days=7)
    weekend_interwal = timedelta(days=2)
    
    # робимо словник, в якому будуть тільки ті люди, у яких ДР протягом наступних 7 днів:    
    
    for name, date in users.items():
        date = date.replace(year=current_date.year)

        if current_date.date() <= date.date() <= current_date.date() + interval:
            day_of_week_num = datetime.weekday(date)
            if day_of_week_num in [5, 6]:
                birthdays_weekdays_list[0].append(name)   # якщо ДР на вихідних
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
    
    for day in range(current_date.weekday(), current_date.weekday() + 7): # стартуємо з сьогодні (range(4, 11))
        name_of_the_day = dict_with_day_names[day % 7] # day % 7 - остача від ділення на 7 (або скільки залишається до найближчого меншого числа, що ділиться на 7 без остачі)
        colleagues_to_greet = birthdays_weekdays_list[day % 7]
        if colleagues_to_greet:
            print(f"{name_of_the_day}: {', '.join(colleagues_to_greet)}")

    
get_birthdays_per_week(users)
