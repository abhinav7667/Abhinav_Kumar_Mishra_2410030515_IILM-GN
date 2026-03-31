### 5.EXP4 – Date Conditions, String Functions, and Derived Columns

- **Q1. List employees hired before 30-06-1980 or after 31-12-1981**

```sql

SELECT * FROM EMPLOYEE
WHERE HIREDATE < '1980-06-30' OR HIREDATE > '1981-12-31';
```

- **Q2. List employees whose second letter of name is 'A'**

```sql

SELECT ENAME FROM EMPLOYEE
WHERE ENAME LIKE '_A%';
```

- **Q3. List employees whose name length is 5 characters**

```sql

SELECT ENAME FROM EMPLOYEE
WHERE LENGTH(ENAME) = 5;
```

- **Q4 Display employees whose names have second alphabet A in their names**

```sql

SELECT*FROM EMPLOYEE
WHERE ENAME LIKE '_A%';
```

- **Q5. List employees whose job is not CLERK, SALESMAN, or ANALYST**

```sql

SELECT * FROM EMPLOYEE
WHERE JOB NOT IN ('CLERK', 'SALESMAN', 'ANALYST');
```

- **Q6. Display EMPNO, ENAME and annual salary (SAL*12) ordered by salary descending**

```sql

SELECT EMPNO, ENAME,
       SAL * 12 AS ANNUAL_SALARY
FROM EMPLOYEE
ORDER BY SAL DESC;
```
- **Q7. Display salary components (HRA, PF, DA) and total salary**

```sql

SELECT ENAME, SAL,
       (SAL * 0.15) AS hra,
       (SAL * 0.05) AS pf,
       (SAL * 0.10) AS da,
       ((SAL + (SAL * 0.15) + (SAL * 0.10)) - (SAL * 0.05)) AS TOTALSALARY
FROM EMPLOYEE
ORDER BY TOTALSALARY DESC;
```

- **Q8. Update salary to 10% of its value where commission is NULL**

```sql

UPDATE EMPLOYEE
SET SAL = 1.10 * SAL
WHERE COMM IS NULL OR COMM=0;
```

- **Q9. List employees whose 120% of salary is greater than 3000**

```sql

SELECT * FROM EMPLOYEE
WHERE SAL * 1.2 > 3000;
```

- **Q10. List employees where length of salary value is at least 3 digits**

```sql

SELECT * FROM EMPLOYEE
WHERE SAL >= 100;
```