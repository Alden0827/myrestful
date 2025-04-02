Python 3.11.4

:: test /api/data/summary/ (Public)
http://127.0.0.1:8000/api/data/summary/
curl -X GET http://127.0.0.1:8000/api/data/summary/


:: Test /api/data/sensitive/ (Restricted Origin)
curl -X GET http://127.0.0.1:8000/api/data/sensitive/ -H "Origin: http://allowed-origin.com"

:: Test /api/data/confidential/ (Token Required)
curl -X POST http://127.0.0.1:8000/api/token/ -d "username=admin&password=admin"

result:
{
	"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0MzY0Mjc2OSwiaWF0IjoxNzQzNTU2MzY5LCJqdGkiOiJjMWE2ZjVkMTBiNDI0MGY3YWQwMWQ5ZjJkMzg1YjM1NSIsInVzZXJfaWQiOjF9.RCMJobQq0jg6nwnLs8fWWHgx3j2JVrVfdX16bHJyp5A",
	"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQzNTU2NjY5LCJpYXQiOjE3NDM1NTYzNjksImp0aSI6Ijg3NDk5NzI5ZDVmNDRlMmJhYzE4YmNlZmNmMDg5OGE4IiwidXNlcl9pZCI6MX0.VPx0XL5XYGi9Q3nMrIPAAK341S_26JJ8p8GyJsj_mOQ"
}

:: Use the Token to Access /api/data/confidential/
curl -X GET http://127.0.0.1:8000/api/data/confidential/ -H "Authorization: Bearer <access_token>"

:: Use the Refresh Token to Get a New Access Token
curl -X POST http://127.0.0.1:8000/api/token/refresh/ -d "refresh=<refresh_token>"

result:
{
  "access": "new_access_token_here"
}


:: admin panel
username: admin
password: admin


:: creating data
curl -X POST http://127.0.0.1:8000/api/data/ \
     -H "Authorization: Bearer <access_token>" \
     -H "Content-Type: application/json" \
     -d '{"REGION": "Region 12", "FIRST_NAME": "Juan", "LAST_NAME": "Dela Cruz", "AGE": 30}'

:: List data
curl -X GET http://127.0.0.1:8000/api/data/ -H "Authorization: Bearer <access_token>"

:: Retrieve Data (ID = 1)
curl -X GET http://127.0.0.1:8000/api/data/1/ -H "Authorization: Bearer <access_token>"

:: Update Data (ID = 1)
curl -X PUT http://127.0.0.1:8000/api/data/1/ \
     -H "Authorization: Bearer <access_token>" \
     -H "Content-Type: application/json" \
     -d '{"REGION": "Updated Region", "FIRST_NAME": "Pedro", "LAST_NAME": "Santos", "AGE": 35}'

:: Delete Data (ID = 1)
curl -X DELETE http://127.0.0.1:8000/api/data/1/ -H "Authorization: Bearer <your_access_token>"
