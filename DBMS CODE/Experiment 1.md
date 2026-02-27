### 1. Database and Schema Setup (Setup Only – No Questions)

- **Create the database**

  ```sql
  CREATE DATABASE 2cse21_0515;
  ```

- **Select the database**

  ```sql
  USE 2cse21_0515;
  ```

- **Create table `DEPARTMENT`**

  ```sql
  CREATE TABLE DEPARTMENT (
      DEPTNO INT PRIMARY KEY,
      DNAME VARCHAR(15) NOT NULL
  );
  ```

- **Create table `EMPLOYEE`**

  ```sql
  CREATE TABLE EMPLOYEE (
      EMPNO INT PRIMARY KEY,
      ENAME VARCHAR(20) NOT NULL,
      JOB VARCHAR(20),
      MGR INT,
      HIREDATE DATE,
      SAL DECIMAL(10,2),
      COMM DECIMAL(7,2),
      DEPTNO INT,
      FOREIGN KEY (DEPTNO) REFERENCES DEPARTMENT(DEPTNO)
  );
  ```

- **Insert records into `DEPARTMENT`**

  ```sql
  INSERT INTO DEPARTMENT VALUES
  (10,'RESEARCH'),
  (20,'ACCOUNTING'),
  (30,'SALES'),
  (40,'OPERATIONS');
  ```

- **Insert records into `EMPLOYEE`**

  ```sql
  INSERT INTO EMPLOYEE VALUES
  (7369,'SMITH','CLERK',7902,'1980-12-17',800,NULL,20),
  (7499,'ALLEN','SALESMAN',7698,'1981-02-20',1600,300,30),
  (7521,'WARD','SALESMAN',7698,'1981-02-22',1250,300,30),
  (7566,'JONES','MANAGER',7839,'1981-04-02',2975,NULL,20),
  (7654,'MARTIN','SALESMAN',7698,'1981-09-28',1250,1400,30),
  (7698,'BLAKE','MANAGER',7839,'1981-05-01',2850,NULL,30),
  (7782,'CLARK','MANAGER',7839,'1981-06-09',2450,NULL,20),
  (7788,'SCOTT','ANALYST',7566,'1982-12-09',3000,NULL,40),
  (7839,'KING','PRESIDENT',NULL,'1981-11-17',5000,NULL,20),
  (7844,'TURNER','SALESMAN',7698,'1981-09-08',1500,0,30),
  (7876,'ADAMS','CLERK',7788,'1983-01-12',1100,NULL,20),
  (7900,'JAMES','CLERK',7698,'1981-12-03',950,NULL,30),
  (7902,'FORD','ANALYST',7566,'1981-12-03',3000,NULL,20),
  (7934,'MILLER','CLERK',7782,'1982-01-23',1300,NULL,10);
  ```

- **Display all departments**

  ```sql
  SELECT * FROM DEPARTMENT;
  ```

- **Display all employeess**

  ```sql
  SELECT * FROM EMPLOYEE;
  ```

---

### 2. EXP1 – Basic DDL, DML, and Simple Queries

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

- **Q5. Increase salary by 10% for department 20 in `Employee_master`**

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