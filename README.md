# User API

## Register User

https://travel-game-python.herokuapp.com/api/registration/

Body:

```
{

		"username": "user2",
	  "password1": "areas1890stillmadeit",
     "password2": "areas1890stillmadeit"


}
```

Response:

```
{
  "key": "a0671dd6e8b77c155438e47a2bc4a74d4e376564"
}
```

## Login User

https://travel-game-python.herokuapp.com/api/login/

Body:

```
{

		"username": "user2",
	  "password": "areas1890stillmadeit"


}
```

Response:

```
{
  "key": "a0671dd6e8b77c155438e47a2bc4a74d4e376564"
}
```

Headers:

```

AuthorizationToken 7b010856df3577785f735eb6955372839afd1c98
Content-Typeapplication/json
```
