# Write your MySQL query statement below
SELECT firstname,lastname,city,state FROM PERSON
left JOIN ADDRESS
ON PERSON.personID = ADDRESS.personID;