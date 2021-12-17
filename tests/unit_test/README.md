# Unit Test
This document will describe how to implement unit tests correctly for this repo.

Every part of this application will be developed as component. A component could be a class or a set of function that implement a specific function as an interface. A component is bundled as single Python file. This component contains different function to implement the specified functionallity. Each function of the compoenent has to be unit tested! For example you got and sql server then your SQL_Server.py may look like

    class SQLServer:
        def __init__(self):
            # Do some stuff
        def runQuery(self, string):
            # Do some stuff
        def getInformation(self, string):
            # Do more stuff

Then you should create unit tests for all function in this case:

- <code>\_\_init__() </code>
- <code>runQuery()</code>
- <code>getInformation()</code>

To test those Units you create a Unit Test Python file here and name it as the componente that you will test. So for this example **SQL_Server_UT.py**

In this repository the unittest Framework from Python will get used. See [Unit Test Documentation](https://docs.python.org/3/library/unittest.html)

Always try to do white box testing. For that it is neccesary that you stub function and mock them. For a short introduction how to use the function stubbing int python with the unittest module you can see the Stackoverflow anwer [function stubbing](https://stackoverflow.com/questions/3909942/how-to-stub-python-methods-without-mock)

