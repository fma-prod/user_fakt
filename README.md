### Currently, It doesn't work with on Linux docker image, due to network problem.

we have tryied to make it work with 2 differents Docker images.
First one based on the official python 3.6 image (FROM python:3.6) and 
the other based on official ubuntu image (FROM ubuntu:16.04).


We got same error in both cases:

```
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/runpy.py", line 193, in _run_module_as_main
    "_main_", mod_spec)
  File "/usr/local/lib/python3.6/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/usr/local/lib/python3.6/site-packages/aiohttp/web.py", line 546, in <module>
    main(sys.argv[1:])  # pragma: no cover
  File "/usr/local/lib/python3.6/site-packages/aiohttp/web.py", line 541, in main
    run_app(app, host=args.hostname, port=args.port, path=args.path)
  File "/usr/local/lib/python3.6/site-packages/aiohttp/web.py", line 454, in run_app
    asyncio.gather(*server_creations, loop=loop)
  File "/usr/local/lib/python3.6/asyncio/base_events.py", line 467, in run_until_complete
    return future.result()
  File "/usr/local/lib/python3.6/asyncio/base_events.py", line 1048, in create_server
    % (sa, err.strerror.lower()))
OSError: [Errno 99] error while attempting to bind on address ('::1', 8080, 0, 0): cannot assign requested address
```


### Currently this code works perfectly on a OSX version 10.11

We will provide soon a fix for the linux os.

####  In between following steps should allow you to launch the server and test this project  
1. We then propose to download the project from git the repository.  
   - git clone git@github.com:fma-prod/user_fakt.git 
2. To create a virtual environment based on 3.6
3. Activate that virtual environment just created.
4. Change directory to folder where git repository has been downloaded.
5. execute 
    - pip install -r requirements.txt
6. Launch the server using this command
    - python -m aiohttp.web -P 8080 aio_user:app_factory


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