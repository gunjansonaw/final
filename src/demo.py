import random
import json
from faker import Faker
import bson

fake = Faker()

records = []

for _ in range(30000):
    record = {
        "_id": {
            "$oid": str(bson.ObjectId())
        },
        "fname": fake.first_name().lower(),
        "lname": fake.last_name().lower(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "day": random.randint(1, 28),  # Random day in a month
        "month": str(random.randint(1, 12)),  # Random month
        "year": random.randint(2020, 2023),  # Random year in range 2020-2023
        "note": fake.word(),
        "__v": 0
    }
    records.append(record)

# Save to a JSON file
with open('records.json', 'w') as file:
    json.dump(records, file, indent=4)

print("200 records have been created and saved to 'records.json'")
