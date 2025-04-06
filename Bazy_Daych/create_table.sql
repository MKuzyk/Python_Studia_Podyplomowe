--CREATE DATABASE BD_PODYPLOMOWE

CREATE TABLE department (
    department_id INT IDENTITY(1,1) PRIMARY KEY,  -- Klucz główny, autoinkrementacja
    name VARCHAR(1000)
);

CREATE TABLE employees (
    employee_id INT IDENTITY(1,1) PRIMARY KEY,   -- Klucz główny, autoinkrementacja
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    hire_date DATE,
    salary DECIMAL(10, 2),
    department_id INT,
    CONSTRAINT FK_department FOREIGN KEY (department_id) REFERENCES department(department_id)
);

CREATE TABLE contracts (
    contract_id INT IDENTITY(1,1) PRIMARY KEY,  -- Klucz główny, autoinkrementacja
    start_date DATE,
    end_date DATE,
    type VARCHAR(100),
    employee_id INT,
    CONSTRAINT FK_employee FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

CREATE TABLE address (
    address_id INT IDENTITY(1,1) PRIMARY KEY,  -- Klucz główny, autoinkrementacja
    street VARCHAR(255),
    city VARCHAR(255),
    country VARCHAR(255),
    employee_id INT,
    CONSTRAINT FK_employee_address FOREIGN KEY (employee_id) REFERENCES employees(employee_id)  -- Klucz obcy do tabeli employees
);

CREATE TABLE business_trip(
    trip_id INT IDENTITY(1,1) PRIMARY KEY,     -- Klucz główny, autoinkrementacja
    start_time DATETIME,
    end_time DATETIME,
    destination VARCHAR(255),
    title VARCHAR(255),
    description VARCHAR(4000)
);

CREATE TABLE business_trip_employees (
    employee_id INT,                        -- ID pracownika (klucz obcy)
    trip_id INT,
    CONSTRAINT FK_employee_trip FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    CONSTRAINT FK_trip FOREIGN KEY (trip_id) REFERENCES business_trip(trip_id)
);

CREATE TABLE cars (
    car_id INT IDENTITY(1,1) PRIMARY KEY,      -- Klucz główny, autoinkrementacja
    millage bigint,
    brand VARCHAR(100),
    engine_type VARCHAR(100),
    employee_id INT,
    CONSTRAINT FK_employee_car FOREIGN KEY (employee_id) REFERENCES employees(employee_id)  -- Klucz obcy do tabeli employees
);

