from pymongo import MongoClient
# Creating DataFrame
client = MongoClient("mongodb+srv://Bhargav:1234@cluster0.npgwjm5.mongodb.net/test")
db = client['test']
collection = db['unoc_report']
data = collection.find()
df = DataFrame(data)
print(df)