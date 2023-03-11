## Details

This is backend todo-list.

## Prerequisites:
- python3
- flask, flask_cors libraries 

## Content:
- app.py
- docker file 
- prereq.txt file

## how to use it:
- run the python application, if the app is running correct you should be able to see this output: 
```
 Serving Flask app 'app'
  Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   Running on all addresses (0.0.0.0)
   Running on http://127.0.0.1:1234
   Running on http://192.168.1.94:1234
Press CTRL+C to quit
```

- in your terminal run the command: ```curl http://localhost:1234``` because the list is empty you will see ```{"TODO":[]}```
- add the first element in your list by running:
```curl -X PUT -H "Content-Type: application/json" -d '{"title": "<task name>", "completed": <boolean>}' http://localhost:1234/```, where the <taskn name> is the name of your ```to do```. 
EXAMPLE: ```curl -X PUT -H "Content-Type: application/json" -d '{"title": "wash the car", "completed": False}' http://localhost:1234/```

### Commands and their paths: 
* GET: ```http://localhost:1234/```
* PUT: ```http://localhost:1234/```
* GET[id]: ```http://localhost:1234/todo/[todo_id]```
* PATCH: ```http://localhost:1234/todo/[todo_id] ```
* DELETE: ```http://localhost:1234/todo/[todo_id]```

### How to use it inside of a container: 
* clone the repository
* open the terminal and navigate inside of the project folder ```cd <path to the folder > ```
* run ```docker build -t <prefered name> . ```
* run `` docker run -d -p <host_port>
* test with ```curl http://localhost:1234```
