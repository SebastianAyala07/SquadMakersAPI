# SquadMakersAPI


## Up the server 📋

### __Con Docker__ 🚀

_In the root folder of the project (where the entrypoint.py is) execute the following commands_
```
$ docker-compose up -d
```

__Run tests__

```
$ docker exec -it <name_container> bash
$ pytest
```


# Testing API
_For testing api I provide you this aws instance and the url is:_

_http://ec2-3-92-255-107.compute-1.amazonaws.com/_

_In this url you can see the histogram image_

## /joke/
___
### /joke/_\<origin\>_
_http://ec2-3-92-255-107.compute-1.amazonaws.com/joke/_

## /joke/chuck
_http://ec2-3-92-255-107.compute-1.amazonaws.com/joke/chuck_

## /joke/dad
_http://ec2-3-92-255-107.compute-1.amazonaws.com/joke/dad_

## /num/
### _send parameters "number" or "numbers"_
_http://ec2-3-92-255-107.compute-1.amazonaws.com/num/_