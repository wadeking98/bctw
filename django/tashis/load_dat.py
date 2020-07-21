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
            "lname":"test",
            "email":"alice@mail.com",
            "pass":"test"
        },
        {
            "fname":"bob",
            "lname":"test",
            "email":"bob@mail.com",
            "pass":"test"
        },
        {
            "fname":"john",
            "lname":"doe",
            "email":"john@mail.com",
            "pass":"test"
        },
        {
            "fname":"jane",
            "lname":"doe",
            "email":"jane@mail.com",
            "pass":"test"
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
    ],
    "questions":[
        {
            "question":"is this a test?",
            "mid":[1,3],
            "mtid":[1],
            "data_form":1
        }
    ],
    "question_data":[
        {
            "qid":1,
            "pid":1,
            "uid":2,
            "data_text":"this is a test",
            "data_form":1
            
        }
    ]
}

for user in data["users"]:
    u=User()
    u.first_name=user["fname"]
    u.last_name=user["lname"]
    u.username=user["email"]
    u.email=user["email"]
    u.password=user["pass"]
    u.save()

for proj in data["projects"]:
    p = project()
    p.name=proj["name"]
    p.manager=User.objects.get(id=proj["manager"])
    p.save()
    for uid in proj["users"]:
        p.users.add(User.objects.get(id=uid))

for method in data["methods"]:
    m_type = survey_method_types()
    m_type.type_name=method["type"]
    m_type.save()
    for method_name in method["methods"]:
        m_name = survey_methods()
        m_name.type_name=m_type
        m_name.method_name=method_name
        m_name.save()

for question in data["questions"]:
    q=survey_questions()
    q.question=question["question"]
    q.data_form=question["data_form"]
    q.save()
    for mid in question["mid"]:
        q.method.add(survey_methods.objects.get(id=mid))
    for mtid in question["mtid"]:
        q.method_type.add(survey_method_types.objects.get(id=mtid))

for q_data in data["question_data"]:
    qd=survey_data()
    qd.user=User.objects.get(id=q_data["uid"])
    qd.project=project.objects.get(id=q_data["pid"])
    qd.question=survey_questions.objects.get(id=q_data["qid"])
    qd.data_text=q_data["data_text"]
    qd.data_form=q_data["data_form"]
    qd.public = True
    qd.save()
    
    