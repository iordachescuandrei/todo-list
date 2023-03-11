from flask import Flask, request, jsonify
from flask_cors import CORS

myapp = Flask(__name__)
CORS(myapp)

#create a list of dictionaries where to store todos

todolist = []
@myapp.route('/', methods = ['GET'])
def get():
    return jsonify({'TODO':todolist})


@myapp.route('/todo/<int:todoid>', methods = ['GET'])
def getbyid(todoid):
    for todo in todolist:
        if todo['id']==todoid:
            return jsonify({'TODO':todolist})
    return jsonify({'error': 'Element not found'})

@myapp.route('/', methods = ['PUT'])
def put_new():
    newentry = request.json
    if not todolist:
        newentry['id']=1
    else:
        newentry['id']= max([t['id'] for t in todolist]) + 1
    todolist.append(newentry)
    return jsonify({'TODO':todolist})
    
@myapp.route('/todo/<int:todoid>', methods = ['PATCH'])
def patch(todoid):
    for todo in todolist:
        if todo['id']==todoid:
            if 'title' in request.json:
                todo['title']=request.json['title']
            if 'comleted' in request.json:
                todo ['completed']==request.json['completed']
            else:
                todo ['completed']==request.json['completed']
            return jsonify ({'TODO':todolist})
    return jsonify({'error':'Id not found'})


@myapp.route('/todo/<int:todoid>', methods = ['DELETE'])
def delete(todoid):
    for todo in todolist:
       if todo['id']==todoid:
           todolist.remove(todo)
           return jsonify ({'TODO':todolist}) 
    return jsonify({'error':'Id not found'})


if __name__ == '__main__':
    myapp.run (host='0.0.0.0', port=1234)