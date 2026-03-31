### EXP-1 – Basic DDL, DML, and Simple Queries

- **Q1. Create `Employee_master` from `EMPLOYEE`**

```sql
  CREATE TABLE Employee_master AS
  SELECT * FROM EMPLOYEE;
  ```

- **Q2. Display all records from `Employee_master`**

  ```sql
  SELECT * FROM Employee_master;
  ```

- **Q3. Delete all employees of department 10 from `Employee_master`**

  ```sql
  DELETE FROM Employee_master
  WHERE DEPTNO = 10;
  ```

- **Q4. Display `Employee_master` after deletion**

  ```sql
  SELECT * FROM Employee_master;
  ```

- **Q5. Increase salary by 10% for department `20` in `Employee_master`**

  ```sql
  UPDATE Employee_master
  SET SAL = SAL + (SAL * 0.10)
  WHERE DEPTNO = 20;
  ```

- **Q6. Display EMPNO, ENAME, SAL, DEPTNO for department 20 from `Employee_master`**

  ```sql
  SELECT EMPNO, ENAME, SAL, DEPTNO
  FROM Employee_master
  WHERE DEPTNO = 20;
  ```

- **Q7. Modify data type of `SAL` column in `Employee_master`**

  ```sql
  ALTER TABLE Employee_master
  MODIFY SAL DECIMAL(10,2);
  ```

- **Q8. Display all records from `Employee_master` after modification**

  ```sql
  SELECT * FROM Employee_master;
  ```

- **Q9. Drop the table `Employee_master`**

  ```sql
  DROP TABLE Employee_master;
  ```

---