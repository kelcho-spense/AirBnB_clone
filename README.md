# AirBnB_clone
## Welcome to the AirBnB clone project!
## **The Console**
### This is the first step towards building full web application: the AirBnB clone
### The console will be a tool to that will enable us to manage the objects of the project.
	* Create a new object (ex: a new User or a new Place)
	* Retrieve an object from a file, a database etc…
	* Do operations on objects (count, compute stats, etc…)
	* Update attributes of an object
	* Destroy an object 
## Installation
### Clone this repository in your terminal:
***

$ git clone https:github.com/kelcho-spense/AirBnB_clone/
---
## Execution
### Console should work like this in interactive mode:
```Python
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):

========================================
EOF  help  quit

(hbnb) 
<<<<<<< HEAD
(hbnb) 
(hbnb) quit
$
```
### Console should work like this in non-interactive mode:
```Python
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):

========================================
EOF  help  quit

(hbnb)
(hbnb) quit
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):

========================================
EOF  help  quit
(hbnb) 
$
```
### Examples
```Python
$ ./console.py                                                                                                                   
(hbnb) help                                                                                                                                                     
Documented commands (type help <topic>):                                                                                                                        
========================================                                                                                                                        
EOF  all  create  destroy  help  quit  show  update                                                                                                             
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)                                                                                              
```
# Authors
***
  * Kevin Gatimu <kelchospense88@gmail.com>
  * Peter Adewole <phemmyadey@gmail.com>
---
