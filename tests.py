#from functions.write_file import write_file
from functions.run_python import run_python_file

#write_file test cases
#print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
#print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
#print(write_file("calculator", "/tmp/temp.txt", "This should not be allowed"))

#Run_python_file Test Cases
print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py")) #should return error
print(run_python_file("calculator", "nonexistent.py")) #should return error


