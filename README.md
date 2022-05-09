# Images API
<i>Flask application for storing images</i>

<h3><b>Routes</b></h3>

<h4>Registration:</h4> 
<b>[POST]</b> <i>/api/registration</i>

Payload:
```json
{
    "login": "username",
    "email": "usernam@email.com",
    "password": "secret"
}
```

Response:
```json
{
    "createTime": "2022-05-09T05:16:05.284103+00:00",
    "email": "username@email.com",
    "id": "f5c234c5-2f0b-44a2-b4e6-9e89cee7545a",
    "login": "username"
}
```

<h4>Login:</h4>
<b>[GET]</b> <i>/api/login</i>

Payload:
```json
{
    "login": "username",
    "password": "secret"
}
```

Response:
```json
{
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InVzZXJuYW1lIiwiYXV0aFRpbWUiOiIyMDIyLTA1LTA5IDA1OjE2OjM3LjIxNzU5MiswMDowMCJ9.Es8VrKnVc84Z4MYvk_58wzgRWEDpd1wKOAY2FoDw4Ho"
  
}
```

<h4>Me:</h4>

Route to get your page

<b>[GET]</b> <i>/api/me</i>

Headers: 
```shell
"Authorization" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InVzZXJuYW1lIiwiYXV0aFRpbWUiOiIyMDIyLTA1LTA5IDA1OjE2OjM3LjIxNzU5MiswMDowMCJ9.Es8VrKnVc84Z4MYvk_58wzgRWEDpd1wKOAY2FoDw4Ho"
```

Response: 
```json
{
    "id": "f5c234c5-2f0b-44a2-b4e6-9e89cee7545a",
    "images": [
        {
            "description": "Me at the zoo",
            "id": "8ceae123-4324-466d-9cd1-d9c8b5ad2018",
            "source": "/api/images/8ceae123-4324-466d-9cd1-d9c8b5ad2018",
            "upload_date": "2022-05-09 04:54:15.472797"
        }
    ],
    "login": "username"
}
```

<h4>Update Image:</h4>
<b>[POST]</b> <i>/api/images</i>

<b>Payload</b>:

Headers: 
```shell
"Authorization" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6InVzZXJuYW1lIiwiYXV0aFRpbWUiOiIyMDIyLTA1LTA5IDA1OjE2OjM3LjIxNzU5MiswMDowMCJ9.Es8VrKnVc84Z4MYvk_58wzgRWEDpd1wKOAY2FoDw4Ho"
```

```json
{
  "data": "<< base 64 string >>",
  "description": "image description"
}
```

<b>Response</b>: 
```json
{
    "id": "0ca40566-2a53-4f36-8c09-8e5872b81481",
    "login": "dangost",
    "source": "/api/images/0ca40566-2a53-4f36-8c09-8e5872b81481",
    "upload_date": "2022-05-09 05:07:08.750388+00:00"
}
```

<h4>Get raw image:</h4>
<b>[GET]</b> <i>/api/images/0ca40566-2a53-4f36-8c09-8e5872b81481  (image id from last response)</i>


Response: try in browser, it will return photo




<h3><b>Build</b></h3>
```console
pip install poetry
poetry install && poetry shell
make
```

<h3><b>Docker</b></h3>
```console
docker build -t images-api .
```

