# AirBnB_Clone Console

### OBJECTIVIES

The main objective with this project is to make a powerful storage system that give us an abstraction between "My object" and "How they are stored and presisted".

### The Console

* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)

all of this by a commamd interpreter focused in manage the filestorage

### ¿What is a command interpreter?

Do you remember the Shell? Its exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc
* Do operations on objects (count, compute stats, etc)
* Update attributes of an object
* Destroy an object

### ¿What is the SHELL? 

_Simply put, the shell is a program that takes commands from the keyboard and gives them to the operating system to perform. In the old days, it was the only user interface available on a Unix-like system such as Linux. Nowadays, we have graphical user interfaces (GUIs) in addition to command line interfaces (CLIs) such as the shell.

### Execution

* Your code will be execue this:

```sh
$ ./console.py
(hbnb) 
```

### Console Intereactive Run this

```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Shell No Intereactive Run this

```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
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
## buildt with 

_Project constructions tools_

* [Python3 Language]() - Language of Programming
* [Vim](https://www.javascript.com/) - Editor
* [Emacs]() - Other Editor
* [JSON]() - Object String Representation

##   with   By  :
* **Evert Escalante**
  * [@EscalanteEvert](https://twitter.com/EscalanteEvert)
* **Edward Osorno**
  * [@Edw10l](https://twitter.com/Edw10l)