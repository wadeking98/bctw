import csv
from api.models import *

with open('api/sample_data/bcsee_plants_animals.csv') as data:
    csv_reader = csv.reader(data,delimiter=',')

    init = 2000
    i=init
    for row in csv_reader:
        if(i>0 and i< init-1):
            print(row[3])
            sp = species()
            sp.latin_name = row[1]
            sp.name = row[3]
            sp.invasive = row[37]!="Native"
            sp.CDC_rank = 1
            sp.save()
        elif i<=0:
            break
        i=i-1

data = {
    "users":[
        {
            "fname":"alice", 
            "lname":"test"
        },
        {
            "fname":"bob",
            "lname":"test"
        },
        {
            "fname":"john",
            "lname":"doe"
        },
        {
            "fname":"jane",
            "lname":"doe"
        }
    ],
    "projects":[
        {
            "name":"test proj",
            "manager":1,
            "users":[2,3]
        }
    ],
    "methods":[
        {
            "type":"Ground",
            "methods":[
                "Encounter survey",
                "Spotlight survey",
                "Ground counts at seasonal concentrations",
                "Camera trap station",
                "Pellet group counts",
                "Tracks and sign",
                "Snow track survey",
                "Hair capture station",
                "Den survey"
                ]
        },
        {
            "type":"Aerial",
            "methods":[
                "Encounter survey",
                "Fixed-width survey",
                "Total count",
                "Mark-recapture-resight",
                "Aerial snow tracking"
            ]
        }
    ]
}

for user in data["users"]:
    u=app_user()
    u.fname=user["fname"]
    u.lname=user["lname"]
    u.save()

for proj in data["projects"]:
    p = project()
    p.name=proj["name"]
    p.manager=app_user.objects.get(id=proj["manager"])
    p.save()
    for uid in proj["users"]:
        p.users.add(app_user.objects.get(id=uid))

for method in data["methods"]:
    m_type = survey_method_types()
    m_type.type_name=method["type"]
    m_type.save()
    for method_name in method["methods"]:
        m_name = survey_methods()
        m_name.type_name=m_type
        m_name.method_name=method_name
        m_name.save()
    
    