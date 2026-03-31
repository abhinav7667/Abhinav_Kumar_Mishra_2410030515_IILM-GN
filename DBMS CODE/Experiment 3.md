### 4. EXP3 – Ordering, Advanced LIKE, and Logical Operators

- **Q1. List `Employees` of department 30 ordered by salary (descending)**
  
```sql

SELECT ENAME, JOB, SAL
FROM EMPLOYEE
WHERE DEPTNO = 30
ORDER BY SAL DESC;
```

- **Q2. List `Employees` whose name starts with 'A', matches the pattern, and ends with 'N'**
  
```sql

SELECT ENAME, JOB, DEPTNO
FROM EMPLOYEE
WHERE ENAME LIKE 'A%____%N';
```

- **Q3. List `Employees` whose name starts with 'S'**

```sql

SELECT *
FROM EMPLOYEE
WHERE ENAME LIKE 'S%';
```

- **Q4. List `Employees` whose name ends with 'S'**

```sql

SELECT *
FROM EMPLOYEE
WHERE ENAME LIKE '%S';
```

- **Q5. List `Employees` who are in department 10, 20, or 30 OR whose job is CLERK, SALESMAN, or ANALYST**

```sql

SELECT ENAME, JOB, DEPTNO
FROM EMPLOYEE
WHERE DEPTNO IN (10,20,30)
OR JOB IN ('CLERK', 'SALESMAN', 'ANALYST');
```

- **Q6. List `Employees` having non-null commission**

```sql

SELECT ENAME
FROM EMPLOYEE
WHERE COMM IS NOT NULL;
```
- **Q7. Find total salary (salary + commission) for each `Employee`**

```sql

SELECT EMPNO,
       SUM(SAL + IFNULL(COMM, 0)) AS TOTAL_SALARY
FROM EMPLOYEE
GROUP BY EMPNO;
```

- **Q8. Display department number and annual salary (SAL*12) for each `Employee`**

```sql

SELECT DEPTNO, SAL * 12 AS ANNUAL_SALARY
FROM EMPLOYEE
GROUP BY EMPNO;
```

- **Q9. List clerks whose salary is greater than 3000**

```sql

SELECT ENAME
FROM EMPLOYEE
WHERE JOB IN ('CLERK') AND SAL > 3000;
```

- **Q10. List `Employees` whose job is CLERK, SALESMAN, or ANALYST and salary is greater than 3000**

```sql

SELECT ENAME
FROM EMPLOYEE
WHERE JOB IN ('CLERK', 'SALESMAN', 'ANALYST') AND SAL > 3000;
```