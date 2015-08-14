# COREMI ReST API

Rest API created in order to gather all the info required for statistics of the Communion, relationship and mission (base of the discipleship) in the church.

## Http Methods

| HTTP Method | URI          | Action |
| ------------- | ----------- | ----------- |
| GET      | http://[hostname]:[port]/coremi/api/usuarios | Retrieve list of users with a limit of 100 . |
| GET     | http://[hostname]:[port]/coremi/api/usuarios/[usuario_email] | Retrieve a user. |
| POST     | http://[hostname]:[port]/coremi/api/usuarios | Create a new user. |
| POST     | http://[hostname]:[port]/coremi/api/login | Sign in with an existing user. |
| PUT     | http://[hostname]:[port]/coremi/api/usuarios/[usuario_email] | Update an existing user. |
| PUT     | http://[hostname]:[port]/coremi/api/usuarios/[usuario_email] | Delete a user. |
<br />

These are the actions you can make:

* [List Users](https://github.com/rajho92/iasdbecoremi#list-users)

<br />
#### List Users

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
