from Fastapi import fastapi 
import os
import json
import student_api_project

app = fastapi()

file_name = "students.json"

#Read data from file

if os.path.exists(file_name):
   with open (file_name,"r") as f :
        f.read()
        print(json.load)
    
#Write data to file

with open(file_name,"w")as f:
    f.write()
    print(json.load)


# 3. FastAPI Endpoints (20 Marks)
# Create following APIs:

@app.get("/")
def home():
 return{"message":"Welcome to Student API"}

@app.get("/students")
def Get_All_Students():
   return all 

@app.post("/students{id}")
def post():
   return {"message":"post to Student API" }

@app.get("/students/{id}")
def search():
   return {"message":"search to Student API"}

@app.get("DELETE /students/{id}")
def delete():
   return {"message":"delete Student API"}

