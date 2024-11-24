# creche-api

## Introduction

This project is a REST API for managing operations related to creches, children, caregivers, and enrollments. The API allows for creating, reading, updating, and deleting records in a database.

![creche-api](images/api.png)

## Dependencies

Make sure to install the following dependencies:

- FastAPI
- Uvicorn
- SQLAlchemy

You can install these dependencies using pip:

```bash
pip install "fastapi[standard]" uvicorn sqlalchemy
```

## Architecture

The API is organized into several layers:

- **Lower Level: Database**  
  The database stores all information related to crèches, children, caregivers, and enrollments.

- **Operations on Database**  
  This layer contains the business logic for interacting with the database, including creating, reading, updating, and deleting records.

- **API Router Layer**  
  This layer allows us to choose which type of operations to perform based on the HTTP request. It manages the routes and endpoints of the API.

## Endpoints

### Crèches

- **Create a Crèche**
  ```bash
  curl -X POST "http://localhost:8000/creches" -H "Content-Type: application/json" -d '{"name": "Crèche A", "address": "123 Rue Exemple", "capacity": 30}'
  ```

- **Get a Crèche by ID**
  ```bash
  curl -X GET "http://localhost:8000/creches/1"
  ```

### Children

- **Create a Child**
  ```bash
  curl -X POST "http://localhost:8000/children" -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "date_of_birth": "2020-01-01", "parent_email_address": "parent@example.com", "parent_phone_number": "+666666666"}'
  ```

- **Get a Child by ID**
  ```bash
  curl -X GET "http://localhost:8000/children/1"
  ```

### Caregivers

- **Create a Caregiver**
  ```bash
  curl -X POST "http://localhost:8000/caregivers" -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "qualifications": "Bachelor Degree in Early Childhood Education", "years_of_experience": 5, "caregiver_email_address": "caregiver@example.com", "caregiver_phone_number": "+666666666"}'
  ```

- **Get a Caregiver by ID**
  ```bash
  curl -X GET "http://localhost:8000/caregivers/1"
  ```

### Enrollments

- **Create an Enrollment**
  ```bash
  curl -X POST "http://localhost:8000/enrollments" -H "Content-Type: application/json" -d '{"start_date": "2024-01-01", "end_date": "2024-01-05", "child_id": 1, "caregiver_id": 1, "creche_id": 1, "price": 100}'
  ```

- **Get an Enrollment by ID**
  ```bash
  curl -X GET "http://localhost:8000/enrollments/1"
  ```

- **Delete an Enrollment by ID**
  ```bash
  curl -X DELETE "http://localhost:8000/enrollments/1"
  ```

- **Get Enrollments by Creche and Price**
  ```bash
  curl -X GET "http://localhost:8000/enrollments/creche/1/price/100"
  ```

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

- `main` refers to the name of your main Python file (without the `.py` extension).
- `app` is the FastAPI instance created in your `main.py` file.
- The `--reload` option allows the server to automatically reload when you make changes to the code.

## Accessing the API Documentation

You can access the interactive API documentation provided by FastAPI by navigating to the following URL in your web browser:

```
http://127.0.0.1:8000/docs
```

This documentation allows you to test the endpoints directly from your browser.
```