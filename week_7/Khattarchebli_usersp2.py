
"""
Author: Leslie Khattarchebli
Date: 09/24/2025
Description: MongoDB Connection to web335DB
"""

# Import MongoClient from pymongo
from pymongo import MongoClient

# Step 1: Connect to MongoDB (replace <username> and <password> with your credentials)
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Step 2: Access the web335DB database
db = client['web335DB']

# Step 3: Create a new user document
new_user = {
    "firstName": "Ara",
    "lastName": "Lovelace",
    "email": "arra.lovelace@bellevue.edu",
    "employeeId": "2025"
}

insert_result = db.users.insert_one(new_user)
print(f"User created with _id: {insert_result.inserted_id}")

# Step 4: Prove the document was created
created_user = db.users.find_one({"employeeId": "2025"})
print("Created User:", created_user)

# Step 5: Update the email address
db.users.update_one(
    {"employeeId": "2025"},
    {"$set": {"email": "ara.lovelace@bellevue.edu"}}
)

# Step 6: Prove the document was updated
updated_user = db.users.find_one({"employeeId": "2025"})
print("Updated User:", updated_user)

# Step 7: Delete the document
db.users.delete_one({"employeeId": "2025"})

# Step 8: Prove document deleted
deleted_user = db.users.find_one({"employeeId": "2025"})
print(" Deleted User (should be None):", deleted_user)
