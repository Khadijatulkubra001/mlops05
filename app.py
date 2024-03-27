from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for all routes
client = MongoClient('mongodb+srv://i200760:wGbhkkHxiYWRTggo@cluster0.g6cgx.mongodb.net/')
db = client['user_database']
collection = db['users']

# Check MongoDB connection
try:
    client.server_info()  # Attempt to retrieve server info
    print("Connected to MongoDB")
except Exception as e:
    print("Failed to connect to MongoDB:", e)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    if name and email:
        # Store data in MongoDB
        collection.insert_one({'name': name, 'email': email})
        return 'Data stored successfully!', 200
    else:
        return 'Name and email are required!', 400

if __name__ == '__main__':
    app.run(debug=True)
