Example of Open Closed Principle.

In the solution for the following task I used OCP.

Task: separate the Files.

Consider a text file that contains a list of C, C++, and C# source code file names. 
The extensions for the file types are as follows:
l.C -> .c
2.C++ -> .cpp
3.C# -> .cs
 
Given a string, baseFilename, that denotes the name of a real text file, create the following three output files where baseFilename denotes the name of the file received as input and the base of the names for output files:
1. c_baseFilename, for storing C file names.
2. cpp_baseFilename, for storing C++ file names.
3. cs_baseFilename, for storing C# file names.

Next, process the list of file names in baseFilename in order and, for each source code file name encountered, append its name to the appropriate output file.
For example, the input baseFilename is file_OO.txt and it contains the following data:
first.c
first.cpp
first.cs
second.c

First, create the three files named c_file_00.txt, cpp_file_OO.txt, and cs_file_00.txt. Read in each source file name and write them out to their appropriate files. The results are:
• c_file_OO.txt
first.c
second.c

• cpp_file_OO.txt
first. cpp

• cs_file_OO.txt
fi rst.cs

The file names must maintain the order in which they were listed in file_00.txt.
Note: There may not be a file of every type included in the input. In that case, the output file for that type should still be created and it should be empty.

The program has the following parameter:
baseFilename: the name of a text file

Constraints
• baseFilename has a maximum of 10^5 lines.
