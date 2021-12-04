# Reto9 Postman

### Introduction
This is a brief project that helps process and properly format the ninth assignment. This time the task is about the desktop program Postman, 
the API testing software. The assignment was to simply make a series of GET requests at the public [Countries API](https://restcountries.com/). 

The python project before you is simply a tool to automate (not fully, but to some degree) the required format of the .txt files to hand in. Each GET request
returns a JSON file that along with a title, the endpoint and the complete URL must be included in a single .txt file.




### Files and information flow
A custom class was created to store all relevant information on every exercise/request. The _ProcesarEjercicio_ class is defined in tools.py. The process is 
organized in main.py: the class is imported into memory, then one object is created. Input request is called for the user to manually type the title title of
the exercise, the API version (some endpoints where not available in the latest version 3.1), the specific endpoint for the exercise and finally the name of the
 JSON file with the response.
 
 The methods in the class are useful for naming the .txt file, eliminating spaces, organizing separate directories for the JSON responses on one hand
 and the processed .txt files on the other, and finally to write a .txt file with all this information.





### Improvements and next steps
This is a small reflection: if I were to improve this program by making it more autonomous. I would design a way to eliminate the user inputs and
automate it fully. The benefit would be removing the user from the process, which makes it prone to errors. 
