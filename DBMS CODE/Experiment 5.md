### 6. EXP5 – Aggregate and String Functions

- **Q1. Count total number of employees**
  
```sql

SELECT COUNT(*) AS TOTAL_EMPLOYEES FROM EMPLOYEE;
```

- **Q2. Display sum of salaries of all employees**
  
```sql

SELECT SUM(SAL) AS TOTAL_SALARY FROM EMPLOYEE;
```

- **Q3. Display maximum salary**

```sql

SELECT MAX(SAL) AS MAX_SALARY FROM EMPLOYEE;
```

- **Q4. Display minimum salary**
 
```sql

SELECT MIN(SAL) AS MIN_SALARY FROM EMPLOYEE;
```

- **Q5. Display average salary**
 
```sql

SELECT AVG(SAL) AS AVG_SALARY FROM EMPLOYEE;
```

- **Q6. Display maximum salary paid to clerk**
  
```sql

SELECT MAX(SAL) AS MAX_CLERK_SALARY FROM EMPLOYEE
WHERE JOB = 'CLERK';
```

- **Q7. Display maximum salary in department 20**
 
```sql

SELECT MAX(SAL) AS MAX_DEPT20_SALARY FROM EMPLOYEE
WHERE DEPTNO = 20;
```

- **Q8. Display minimum salary among salesmen**
 
```sql

SELECT MIN(SAL) AS MIN_SALESMAN_SALARY FROM EMPLOYEE
WHERE JOB = 'SALESMAN';
```

- **Q9. Display average salary of managers**

```sql

SELECT AVG(SAL) AS AVG_MANAGER_SALARY FROM EMPLOYEE
WHERE JOB = 'MANAGER';
```

- **Q10. Display total salary of analysts in department 40**
  
```sql

SELECT SUM(SAL) AS TOTAL_ANALYST_DEPT40 FROM EMPLOYEE
WHERE JOB = 'ANALYST' AND DEPTNO = 40;
```

- **Q11. Display employee names in uppercase**
  
```sql

SELECT UPPER(ENAME) AS NAME_IN_UPPER
FROM EMPLOYEE;
```

- **Q12. Display employee names in lowercase**
  
```sql

SELECT LOWER(ENAME) AS NAME_IN_LOWER
FROM EMPLOYEE;
```

- **Q13. Display employee names in proper case (first letter capital, rest small)**

```sql

SELECT CONCAT(UPPER(SUBSTRING(ENAME, 1, 1)), LOWER(SUBSTRING(ENAME, 2))) AS NAME_IN_PROPER
FROM EMPLOYEE;
```

- **Q14. Display length of the string 'PRIYANSHU KUMAR YADAV'**

```sql

SELECT LENGTH('ABHINAV') AS NAME_LENGTH;
```

- **Q15. Display length of each employee name along with EMPNO and ENAME**

```sql

SELECT ENAME,LENGTH(ENAME) AS NAME_LENGTH
FROM EMPLOYEE;
```

