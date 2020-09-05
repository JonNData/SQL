## 1: MoM Percent Change 

*Context:* Oftentimes it's useful to know how much a key metric, such as monthly active users, changes between months. Say we have a table logins in the form: 

| user_id | date       |
|---------|------------|
| 1       | 2018-07-01 |
| 234     | 2018-07-02 |
| 3       | 2018-07-02 |
| 1       | 2018-07-02 |
| ...     | ...        |
| 234     | 2018-10-04 |

*Task*: Find the month-over-month percentage change for monthly active users (MAU). 
```
WITH mau AS 
(
  SELECT 
   /* 
    * Typically, interviewers allow you to write psuedocode for date functions 
    * i.e. will NOT be checking if you have memorized date functions. 
    * Just explain what your function does as you whiteboard 
    *
    * DATE_TRUNC() is available in Postgres, but other SQL date functions or 
    * combinations of date functions can give you a identical results   
    * See https://www.postgresql.org/docs/9.0/functions-datetime.html#FUNCTIONS-DATETIME-TRUNC
    */ 
    DATE_TRUNC('month', date) month_timestamp,
    COUNT(DISTINCT user_id) mau
  FROM 
    logins 
  GROUP BY 
    DATE_TRUNC('month', date)
  )
 
 SELECT 
    /*
    * You don't literally need to include the previous month in this SELECT statement. 
    * 
    * However, as mentioned in the "Tips" section of this guide, it can be helpful 
    * to at least sketch out self-joins to avoid getting confused which table 
    * represents the prior month vs current month, etc. 
    */ 
    a.month_timestamp previous_month, 
    a.mau previous_mau, 
    b.month_timestamp current_month, 
    b.mau current_mau, 
    ROUND(100.0*(b.mau - a.mau)/a.mau,2) AS percent_change 
 FROM
    mau a 
 JOIN 
    /*
    * Could also have done `ON b.month_timestamp = a.month_timestamp + interval '1 month'` 
    */
    mau b ON a.month_timestamp = b.month_timestamp - interval '1 month' 
  ```


Q7) Which of the following statement will add a column ‘F_name’ to the STUDENT table?  
A. ALTER TABLE Student add column ( F_name varchar(20));  
B. ALTER TABLE Student add F_name varchar(20);  
C. ALTER TABLE Student add (F_name varchar(20));    
D. ALTER TABLE Student add column (F_name);  

Solution: B  
ALTER TABLE command allows a user to add a new column to a table. Option B is correct syntax of ALTER to add a column in the table.  

Q9) ‘Sid’ in “ENROLLED” table is ‘Foreign Key’ referenced by ‘Sid’ in “STUDENT” table. Now you want to insert a record into the ENROLLED table.  
Which of the following option(s) will insert a row in ENROLLED table successfully?  
INSERT INTO ENROLLED values(53667, '15-420', 'C');  
INSERT INTO ENROLLED values(53666, '15-421', 'C');  
INSERT INTO ENROLLED values(53667, '15-415', 'C');  
INSERT INTO ENROLLED values(53666, '15-415', 'C');   
A. 1 and 3  
B. Only 3  
C. 2 and 4  
D. Only 4  
