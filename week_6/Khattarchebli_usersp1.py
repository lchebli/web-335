"""
Author: Leslie Khattarchebli
Date: September 21, 2025
File Name: Khattarchebli_usersp1.py
Description: This script connects to the web335DB MongoDB database and performs
queries to display user documents.
"""

# Import the MongoClient from pymongo
from pymongo import MongoClient

# Connect to the MongoDB Atlas cluster
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Access the web335DB database
db = client['web335DB']

#Display all documents in the users collection
print("\n--- All Users ---")
for user in db.users.find({}, {"_id": 0}):  # Exclude _id for cleaner output
    print(user)

# Display the document where employeeId is 1011
print("\n--- User with employeeId 1011 ---")
user_1011 = db.users.find_one({"employeeId": "1011"}, {"_id": 0})
print(user_1011)

# Display the document where lastName is Mozart
print("\n--- User with lastName Mozart ---")
user_mozart = db.users.find_one({"lastName": "Mozart"}, {"_id": 0})
print(user_mozart)
