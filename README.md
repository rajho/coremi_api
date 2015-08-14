# COREMI ReST API

Rest API created in order to gather all the info required for statistics of the Communion, relationship and mission (base of the discipleship) in the church.

## Http Methods

| HTTP Method | URI          | Action |
| ------------- | ----------- | ----------- |
| GET      | http://[hostname]:[port]/coremi/api/usuarios | [Retrieve list of users with a limit of 100.](https://github.com/rajho92/iasdbecoremi#list-users) |
| GET     | http://[hostname]:[port]/coremi/api/usuarios/[usuario_email] | [Retrieve a user.](https://github.com/rajho92/iasdbecoremi#retrieve-a-user) |
| POST     | http://[hostname]:[port]/coremi/api/usuarios | [Create a new user.](https://github.com/rajho92/iasdbecoremi#create-a-new-user) |
| POST     | http://[hostname]:[port]/coremi/api/login | [Sign in with an existing user.](https://github.com/rajho92/iasdbecoremi#sign-in) |
| PUT     | http://[hostname]:[port]/coremi/api/usuarios/[usuario_email] | [Update attributes of a user.](https://github.com/rajho92/iasdbecoremi#update-user) |
| DELETE     | http://[hostname]:[port]/coremi/api/usuarios/[usuario_email] | [Delete a user.](https://github.com/rajho92/iasdbecoremi#delete-a-user) |
<br />

These are the actions you can do:

* [List users](https://github.com/rajho92/iasdbecoremi#list-users)
* [Retrieve a user](https://github.com/rajho92/iasdbecoremi#retrieve-a-user)
* [Create a new user](https://github.com/rajho92/iasdbecoremi#create-a-new-user)
* [Sign in with an existing user](https://github.com/rajho92/iasdbecoremi#sign-in)
* [Update attributes of a user](https://github.com/rajho92/iasdbecoremi#update-user)
* [Delete a user](https://github.com/rajho92/iasdbecoremi#delete-a-user)


#### List users

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example**
```sh
curl -i http://localhost:8000/coremi/api/usuarios
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Response**
```json
{
    "usuarios": [
        {
            "administrador": true, 
            "apepaterno": "apellido", 
            "id": 1, 
            "nombre1": "nombre", 
            "nombre2": "segundo_nombre", 
            "nombre3": null, 
            "usuario": "email@dominio.com"
        }, {
            "administrador": true, 
            "apepaterno": "apellido2", 
            "id": 2, 
            "nombre1": "nombre2", 
            "nombre2": "segundo_nombre", 
            "nombre3": null, 
            "usuario": "email2@dominio.com"
        }
    ]
}
```

#### Retrieve a user

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example**
```sh
curl -i http://localhost:8000/coremi/api/usuarios/email@dominio.com
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Response**
```json
{
    "usuarios": [
        {
            "administrador": true, 
            "apepaterno": "apellido", 
            "id": 1, 
            "nombre1": "nombre", 
            "nombre2": "segundo_nombre", 
            "nombre3": null, 
            "usuario": "email@dominio.com"
        }
    ]
}
```

#### Create a new user

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example**
```sh
curl -i -H "Content-Type: application/json" -X POST -d '{"nombreusuario":"email@dominio.com", "password":"xxxxxx", "nombreuno":"nombre", "nombredos":"segundo_nombre", "nombretres":"tercer_nombr  
e", "apepaterno":"apellido_paterno", "apematerno":"apellido_materno", "sexo":"M", "fechanacimiento":"1996-01-31","administrador":"False"}' http://localhost:8000/coremi/api/usuarios
```

>**Request**
```json
{
  "nombreusuario": "email@dominio.com",
  "password": "xxxxxx",
  "nombreuno": "nombre",
  "nombredos": "segundo_nombre",
  "nombretres": "tercer_nombre",
  "apepaterno": "apellido_paterno",
  "apematerno": "apellido_materno",
  "sexo": "M",
  "fechanacimiento": "1996-01-31",
  "administrador": "False"
}
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Response**
```json
{
    "data": {
        "usuarios": [
            {
                "apepaterno": "apellido_paterno", 
                "id": 4, 
                "nombre": "nombre", 
                "usuario": "email@dominio.com"
            }
        ]
    }, 
    "reason": "", 
    "statusCode": 200, 
    "sucess": "True"
}
```

#### Sign in

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example**
```sh
curl -i -H "Content-Type: application/json" -X POST -d '{"nombreusuario":"email@dominio.com", "password":"xxxxxx"}' http://localhost:8000/coremi/api/login
```

>**Request**
```json
{
  "nombreusuario": "email@dominio.com",
  "password": "xxxxxx"
}
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Response**
```json
{
    "logged": "True", 
    "reason": "Usuario logueado.", 
    "statusCode": 200, 
    "sucess": "True"
}
```

#### Update user

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example**
```sh
curl -i -H "Content-Type: application/json" -X PUT -d '{"nombredos":"otro_segundo_nombre"}' http://localhost:8000/coremi/api/usuarios/email@dominio.com
```

>**Request**
```json
{
  "nombredos": "otro_segundo_nombre"
}
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Response**
```json
{
    "reason": "", 
    "statusCode": 200, 
    "sucess": "True"
}
```

#### Delete a user

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Example**
```sh
curl -i -H "Content-Type: application/json" -X DELETE http://localhost:8000/coremi/api/usuarios/email@dominio.com
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Response**
```json
{
    "data": {}, 
    "reason": "", 
    "statusCode": 200, 
    "sucess": "True"
}
```
