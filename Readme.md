### Vehicle Rental Backend

This is the backend application for a vehicle rental service. It exposes a set of REST APIs that enable users to create accounts, browse and book vehicles at different stations, and return vehicles after use.

### Prerequisites

Python 3.6 or later
PostgreSQL

### Installation

`pip install -r requirements.txt`

# Set the environment variables:

```
export FLASK_APP=app
export FLASK_ENV=development
```

# Initialize the database:

```
python -m flask db init
python -m flask db migrate
python -m flask db upgrade
```

### Run the application:
`python -m flask run`

### APIs:

## POST /register:
The POST /register API endpoint allows users to create an account by providing their phone number and a one-time password (OTP - will be used as a password for demo) that has been sent to their phone. When a user makes a POST request to this endpoint with their phone number and OTP in the request body, the server checks if the phone number is already registered. If the phone number is already registered, it returns an error message. If the phone number is not registered, it creates a new user account with the provided phone number and OTP as the password, and returns a success message. This endpoint is used to register a new user for the first time, and is not intended for logging in to an existing account.

## POST /login:
The POST /login API endpoint allows users to log in to their account by providing their phone number and password. When a user makes a POST request to this endpoint with their phone number and password in the request body, the server checks if the phone number is registered. If the phone number is not registered, it returns an error message. If the phone number is registered, it checks if the provided password is correct. If the password is incorrect, it returns an error message. If the phone number and password are correct, it returns a success message. This endpoint is used to log in to an existing account

## POST /vehicles:
The POST /vehicles API endpoint allows the admin to add a new vehicle to the inventory. When the admin makes a POST request to this endpoint with the station ID and status of the vehicle in the request body, the server checks if the specified station exists. If the station does not exist, it returns an error message. If the station exists, it creates a new vehicle with the provided station ID and status, and adds it to the database. It then returns a success message to the client. This endpoint is intended to be used by the admin to add new vehicles to the inventory, and is not intended for use by regular users.

## POST /vehicle-stations:
The POST /vehicle-stations API endpoint allows the admin to create a new vehicle station. When the admin makes a POST request to this endpoint with the location of the station in the request body, the server creates a new vehicle station with the provided location, and adds it to the database. It then returns a success message to the client. This endpoint is intended to be used by the admin to add new vehicle stations, and is not intended for use by regular users.

## POST /vehicles/assign:
The POST /vehicles/assign API endpoint allows the admin to assign a vehicle to a station. When the admin makes a POST request to this endpoint with the vehicle ID and station ID in the request body, the server checks if the specified vehicle and station exist. If either the vehicle or the station does not exist, it returns an error message. If the vehicle and station exist, it updates the vehicle's station ID to the provided station ID, and returns a success message to the client. This endpoint is intended to be used by the admin to manage the assignment of vehicles to stations, and is not intended for use by regular users.

## GET /vehicle-stations/<station_id>/vehicles:
The GET /vehicle-stations/<station_id>/vehicles API endpoint allows users to view the list of available vehicles at a particular station. When a user makes a GET request to this endpoint, the server fetches the list of available vehicles at the specified station from the database, and returns it as a list of dictionaries, with each dictionary representing a vehicle and containing its ID and status. This endpoint is intended to be used by regular users to browse the available vehicles at a station before booking one.

## POST /vehicles/pick:
The POST /vehicles/pick API endpoint allows a user to pick a vehicle from a station. When a user makes a POST request to this endpoint with the vehicle ID and user ID in the request body, the server checks if the specified vehicle is available. If the vehicle is not available, it returns an error message. If the vehicle is available, it updates the vehicle's status to "in use" and returns the vehicle information to the client. This endpoint is intended to be used by regular users to book a vehicle for use.

## POST /vehicles/return:
The POST /vehicles/return API endpoint allows a user to return a vehicle to a station after using it. When a user makes a POST request to this endpoint with the vehicle ID and station ID in the request body, the server checks if the specified vehicle and station exist. If either the vehicle or the station does not exist, it returns an error message. If the vehicle and station exist, it updates the vehicle's status to "available" and assigns it to the specified station. It then returns a success message to the client. This endpoint is intended to be used by regular users to return a vehicle after using it.