from flask import Flask
from flask_cors import CORS
from datetime import datetime
from time import sleep
import json
 
app = Flask(__name__)
CORS(app)

image_size = 100

user = {
    "id": 123,
    "first_name": "John",
    "last_name": "Smith",
    "dob": datetime(1984, 4, 23).strftime("%Y-%m-%d"),
    "email": "johnsmith@gmail.com"
}

contacts = [
    {
        "id": 124,
        "first_name": "Bill",
        "last_name": "Brown",
        "dob": datetime(1955, 8, 4).strftime("%Y-%m-%d"),
        "email": "billbrown@gmail.com",
        "connected_to": 123,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=1"
    },
    {
        "id": 125,
        "first_name": "Alice",
        "last_name": "Johnson",
        "dob": datetime(1990, 3, 12).strftime("%Y-%m-%d"),
        "email": "alicejohnson@gmail.com",
        "connected_to": 123,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=2"
    },
    {
        "id": 126,
        "first_name": "Mike",
        "last_name": "Williams",
        "dob": datetime(1978, 9, 21).strftime("%Y-%m-%d"),
        "email": "mikewilliams@gmail.com",
        "connected_to": 123,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=3"
    },
    {
        "id": 127,
        "first_name": "Emily",
        "last_name": "Taylor",
        "dob": datetime(1986, 5, 8).strftime("%Y-%m-%d"),
        "email": "emilytaylor@gmail.com",
        "connected_to": 123,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=4"
    },
    {
        "id": 128,
        "first_name": "David",
        "last_name": "Clark",
        "dob": datetime(1972, 11, 15).strftime("%Y-%m-%d"),
        "email": "davidclark@gmail.com",
        "connected_to": 123,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=5"
    },
    {
        "id": 129,
        "first_name": "Sarah",
        "last_name": "Miller",
        "dob": datetime(1983, 7, 19).strftime("%Y-%m-%d"),
        "email": "sarahmiller@gmail.com",
        "connected_to": 123,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=6"
    },
    {
        "id": 130,
        "first_name": "Robert",
        "last_name": "Davis",
        "dob": datetime(1965, 2, 10).strftime("%Y-%m-%d"),
        "email": "robertdavis@gmail.com",
        "connected_to": 123,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=7"
    },
    {
        "id": 131,
        "first_name": "Jennifer",
        "last_name": "Wilson",
        "dob": datetime(1992, 6, 7).strftime("%Y-%m-%d"),
        "email": "jenniferwilson@gmail.com",
        "connected_to": 123,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=8"
    },
    {
        "id": 132,
        "first_name": "James",
        "last_name": "Johnson",
        "dob": datetime(1980, 4, 2).strftime("%Y-%m-%d"),
        "email": "jamesjohnson@gmail.com",
        "connected_to": 124,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=9"
    },
    {
        "id": 133,
        "first_name": "Linda",
        "last_name": "Smith",
        "dob": datetime(1975, 10, 20).strftime("%Y-%m-%d"),
        "email": "lindasmith@gmail.com",
        "connected_to": 124,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=10"
    },
    {
        "id": 134,
        "first_name": "Christopher",
        "last_name": "Brown",
        "dob": datetime(1988, 1, 14).strftime("%Y-%m-%d"),
        "email": "christopherbrown@gmail.com",
        "connected_to": 124,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=11"
    },
    {
        "id": 135,
        "first_name": "Amanda",
        "last_name": "Wilson",
        "dob": datetime(1995, 11, 30).strftime("%Y-%m-%d"),
        "email": "amandawilson@gmail.com",
        "connected_to": 124,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=12"
    },
    {
        "id": 136,
        "first_name": "Matthew",
        "last_name": "Taylor",
        "dob": datetime(1982, 9, 5).strftime("%Y-%m-%d"),
        "email": "matthewtaylor@gmail.com",
        "connected_to": 124,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=13"
    },
    {
        "id": 137,
        "first_name": "Karen",
        "last_name": "Anderson",
        "dob": datetime(1977, 12, 8).strftime("%Y-%m-%d"),
        "email": "karenanderson@gmail.com",
        "connected_to": 124,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=14"
    },
    {
        "id": 138,
        "first_name": "Daniel",
        "last_name": "Thomas",
        "dob": datetime(1991, 3, 21).strftime("%Y-%m-%d"),
        "email": "danielthomas@gmail.com",
        "connected_to": 124,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=15"
    },
    {
        "id": 139,
        "first_name": "Patricia",
        "last_name": "Davis",
        "dob": datetime(1970, 7, 16).strftime("%Y-%m-%d"),
        "email": "patriciadavis@gmail.com",
        "connected_to": 124,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=16"
    },
    {
        "id": 140,
        "first_name": "Joseph",
        "last_name": "White",
        "dob": datetime(1987, 5, 12).strftime("%Y-%m-%d"),
        "email": "josephwhite@gmail.com",
        "connected_to": 124,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=17"
    },
    {
        "id": 141,
        "first_name": "Laura",
        "last_name": "Harris",
        "dob": datetime(1984, 8, 19).strftime("%Y-%m-%d"),
        "email": "lauraharris@gmail.com",
        "connected_to": 124,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=18"
    },
    {
        "id": 142,
        "first_name": "Michael",
        "last_name": "Evans",
        "dob": datetime(1979, 11, 24).strftime("%Y-%m-%d"),
        "email": "michaelevans@gmail.com",
        "connected_to": 124,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=19"
    },
    {
        "id": 143,
        "first_name": "Kimberly",
        "last_name": "Roberts",
        "dob": datetime(1993, 2, 27).strftime("%Y-%m-%d"),
        "email": "kimberlyroberts@gmail.com",
        "connected_to": 124,
        "avatar": f"https://i.pravatar.cc/{image_size}?img=20"
    }
]

@app.route('/user')
def get_user():
    response = json.dumps(user)
    
    return response

@app.route('/contacts')
def get_contacts():
    result = []
    
    for contact in contacts:
        if contact["connected_to"] == user["id"]:
            result.append(contact)
            
    response = json.dumps(result)
    
    return response

if __name__ == '__main__':
    app.run(debug=True)
