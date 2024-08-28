import json
from datetime import datetime, timedelta

with open(r'dosya konumu', 'r', encoding='utf-8') as file:
    user_data = json.load(file)

for user in user_data:
    user["CreateDate"] = datetime.strptime(user["CreateDate"], "%Y-%m-%d %H:%M:%S")

user_data.sort(key=lambda x: x["CreateDate"])

def find_users_with_close_dates(users, interval_seconds=3):
    grouped_users = []
    group = [users[0]]

    for i in range(1, len(users)):
        if users[i]["CreateDate"] - users[i-1]["CreateDate"] <= timedelta(seconds=interval_seconds):
            group.append(users[i])
        else:
            if len(group) > 1:
                grouped_users.append(group)
            group = [users[i]]

    if len(group) > 1:
        grouped_users.append(group)

    return grouped_users

close_date_users = find_users_with_close_dates(user_data)

close_date_users_flat = [user for group in close_date_users for user in group]

for user in close_date_users_flat:
    user["Count"] = len(close_date_users_flat)

for user in close_date_users_flat:
    user["CreateDate"] = user["CreateDate"].strftime("%Y-%m-%d %H:%M:%S")

output_path = r'dosya konumu'
with open(output_path, 'w', encoding='utf-8') as file:
    json.dump(close_date_users_flat, file, ensure_ascii=False, indent=4)

print(f"Users with close CreateDates have been written to '{output_path}'")
