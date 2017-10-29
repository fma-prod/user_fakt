### Currently, It doesn't work with docker file, due to network problem.

We will provide soon a fix

####  In between following steps should allow you to launch the server and test this project  
1. We then propose to download the project from git the repository.
2. To create a virtual environment based on 3.6
3. Work on that virtual environment just created. 
4. change directory to folder where git repository has been downloaded.
5. execute pip install -r requirements.txt
6. execute the server using this command
    python -m aiohttp.web -P 8080 aiouser:app_factory


List of reachable services:

```
get all user - 
    http verb: GET 
    URL: http://localhost:8080/users/
```

```
get user by id - 
    http verb: GET 
    URL: http://localhost:8080/users/{id}
```

```
add a user - 
    http verb: POST 
    URL: http://localhost:8080/users/
    body: application/json
    params: name, age
            {"name": "here-the-name",
             "age": 5
             }
```
    
```
modify a user - 
    http verb: PATCH 
    URL: http://localhost:8080/users/{id}
    body: application/json
    params: name, age
            {"name": "new-name",
             "age": 10
             }
```
    
```
remove a user - 
    http verb: DELETE 
    URL: http://localhost:8080/users/{id}
```

``` 
ping -
    http verb: GET
    URL: http://localhost:8080/users/ping/
```