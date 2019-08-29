# User API

## Register User - Post request

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

## Login User - Post request

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

Authorization: Token 7b010856df3577785f735eb6955372839afd1c98
Content-Type: application/json
```

# Server Endpoints

## Get all rooms - Get request

https://travel-game-python.herokuapp.com/api/adv/allrooms

Body:

```
{

		none


}
```

Response:

```
{
  "rooms": [
    {
      "id": 6,
      "title": "Outside Cave Entrance",
      "description": "North of you, the cave mount beckons",
      "n_to": 7,
      "s_to": 0,
      "e_to": 0,
      "w_to": 0
    },
```

Headers:

```

Authorization: Token 7b010856df3577785f735eb6955372839afd1c98
Content-Type: application/json
```

## Initiate game - Get request

https://travel-game-python.herokuapp.com/api/adv/init

Body:

```
{

		none


}
```

Response:

```
{
  "uuid": "3b500155-b976-4089-a24d-888a8090a810",
  "name": "test5",
  "title": "Outside Cave Entrance",
  "description": "North of you, the cave mount beckons",
  "players": [
    "mario",

}
```

Headers:

```

Authorization: Token 7b010856df3577785f735eb6955372839afd1c98
Content-Type: application/json
```

## Move Player - Post request

https://travel-game-python.herokuapp.com/api/adv/move

Body:

```
{

		"direction":"n"


}
```

Response:

```
{
  "name": "test5",
  "title": "Foyer",
  "description": "Dim light filters in from the south. Dusty\npassages run north and east.",
  "players": [],
  "error_msg": ""
}
```

Headers:

```

Authorization: Token 7b010856df3577785f735eb6955372839afd1c98
Content-Type: application/json
```
