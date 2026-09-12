
#### Resource Used [FreeCodeCamp](https://youtu.be/tLKKmouUams?si=qskwxdfzOafjKzk-)

```
GET - get information
POST - create something new
PUT - Update
DELETE - delete something
```


FastAPI creates good looking UI Docs at ```localhost:8000/docs``` for you 


### GET

```
curl -X 'GET' \ 'http://127.0.0.1:8000/' \ -H 'accept: application/json'
```

Status Code : 200(OK)

Response Body :
```
 { "name": "First Data" }
```

Response Header : 
```
 content-length: 21 content-type: application/json  date: Fri,11 Sep 2026 22:29:58 GMT server: uvicorn
```



#### Path Parameter :
```/get-student/{student_id}```

**get-student** = endpoint 
**{student_id}** =  Path to which student


#### Path (from fastapi import Path)
```def get_student(student_id: int = Path(..., description="The ID of the Student you want", gt=0))```

**Allows to set description of what the field requires** - Path(..., description="The ID of the Student you want"

**Even allows setting range** - 
- gt=0 (Greater Than)
- lt =3 (Less Than)