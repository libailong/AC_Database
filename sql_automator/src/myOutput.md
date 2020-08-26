### Date: 8 March 2019
### Name: Bailong Li


### The Output of my program is the following:
```
lib@aldenv103:~/Documents/lab-4-libailong/src$ python myQueryProgram.py
 My database has been loaded
  Welcome to my database automation program!
what would you like to do taody
1 for query
2 for insert
3 for edit
: 1
 user types in 1
  Enter table name: Course
My command is:   SELECT * FROM Course
  Result is: <sqlite3.Cursor object at 0x7fe555520810>
  Raw tables data : [('adfadfaaf', 'Computer Theory', 'CompSci', 3), ('cs21233XX', 'Graphics', 'CompSci', 3), ('CS300', 'Web Design', 'CompSci', 3), ('CS400', 'Software Design', 'CompSci', 3), ('CS500', 'Databases', 'CompSci', 3), ('CS600', 'Bioinformatics', 'CompSci', 3), ('EN201', '3eqqweq', 'ENG', 3), ('FR301', 'French', 'FRCH', 3), ('12312', '12312312', '213123', 12312312), ('qwe', 'qweqw', 'qweqwe', 'qweqwe'), ('adf', 'dfasd', 'dafasd', 'dasfas')]
lib@aldenv103:~/Documents/lab-4-libailong/src$ python myQueryProgram.py
 My database has been loaded
  Welcome to my database automation program!
what would you like to do taody
1 for query
2 for insert
3 for edit
: 2
user types in 2
 what table? Course
 Insert courseId: 123
 Insert title: 12321
 Insert deptName: 12312
 Insert credits: 2313
  Running this command:
   INSERT INTO course VALUES("123","12321","12312","2313")
lib@aldenv103:~/Documents/lab-4-libailong/src$ python myQueryProgram.py
 My database has been loaded
  Welcome to my database automation program!
what would you like to do taody
1 for query
2 for insert
3 for edit
: 3
user types in 3
 what table? Course
what are we going to updata?title
 What are we going to update to? HEllo
 whatId is it? CS300
My command is:   UPDATE Course SET "title" = "HEllo" WHERE courseId == "CS300"
```
