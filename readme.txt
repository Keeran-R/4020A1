Group 1 members
---------------
Keeran Ravishankar, 216387771
CheukWai Chan, 218464057  
Domenico Lasalandra,  217125105
Peipei Yu, 215869753

Compiling and running the program
---------------------------------
The following program uses Python.

Before running the program you must install Requests. On OSX/Linux "sudo pip install requests" or on Windows
"pip install requests" in your terminal. Once you have installed Requests it will now allow you to import the
library in your program.  

You must change the path in line 5 to where your XML file is located, I recommend just importing the XML file in
your project folder and copy the paty from there.

To change the information you are searching for you must change the attribute your are looking for in the parenthesis
to what you want to find. Some search results include title, year, month, day. 

After running the program, a groupID_result.xml file will be created in your program folder containg all the PMID's 
of the search results in XML format.