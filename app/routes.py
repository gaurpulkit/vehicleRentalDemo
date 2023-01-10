from flask import request, jsonify
from app import app, db
from app.models import User, Vehicle, VehicleStation


@app.route("/register", methods=["POST"])
def register():
    # Get the phone number and OTP from the request
    phone_number = request.json["phone_number"]
    otp = request.json["otp"]

    # Check if the phone number is already registered
    user = db.session.query(User).filter_by(phone_number=phone_number).first()
    if user:
        # Phone number is already registered
        return jsonify({"error": "Phone number is already registered"}), 400

    # Phone number is not registered, so create a new user
    new_user = User(phone_number=phone_number, password=otp)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Successfully registered"}), 201


@app.route("/login", methods=["POST"])
def login():
    # Get the phone number and password from the request
    phone_number = request.json["phone_number"]
    # Password is the otp in this case
    password = request.json["password"]

    # Check if the phone number is registered
    user = db.session.query(User).filter_by(phone_number=phone_number).first()
    if not user:
        return jsonify({"error": "Phone number is not registered"}), 400

    # Check if the password is correct
    if user.password != password:
        return jsonify({"error": "Incorrect password"}), 400

    # Phone number and password are correct, so return a success message
    return jsonify({"message": "Successfully logged in"}), 200


@app.route("/vehicle-stations", methods=["POST"])
def create_vehicle_station():
    # Get the location from the request
    location = request.json["location"]

    # Create a new vehicle station
    new_station = VehicleStation(location=location)
    db.session.add(new_station)
    db.session.commit()

    return jsonify({"message": "Successfully created vehicle station"}), 201


@app.route("/vehicles", methods=["POST"])
def add_vehicle():
    # Get the station ID and status from the request
    station_id = request.json["station_id"]
    status = request.json["status"]

    # Check if the station exists
    station = VehicleStation.query.filter_by(id=station_id).first()
    if not station:
        return jsonify({"error": "Station does not exist"}), 400

    # Create a new vehicle
    new_vehicle = Vehicle(station_id=station_id, status=status)
    db.session.add(new_vehicle)
    db.session.commit()

    return jsonify({"message": "Successfully added vehicle"}), 201


@app.route("/vehicles/assign", methods=["POST"])
def assign_vehicle():
    # Get the vehicle ID and station ID from the request
    vehicle_id = request.json["vehicle_id"]
    station_id = request.json["station_id"]

    # Check if the vehicle and station exist
    vehicle = Vehicle.query.filter_by(id=vehicle_id).first()
    station = VehicleStation.query.filter_by(id=station_id).first()
    if not vehicle or not station:
        return jsonify({"error": "Vehicle or station does not exist"}), 400

    # Assign the vehicle to the station
    vehicle.station_id = station_id
    db.session.commit()

    return jsonify({"message": "Successfully assigned vehicle"}), 200


@app.route("/vehicle-stations/<station_id>/vehicles", methods=["GET"])
def get_available_vehicles(station_id):
    # Convert the station ID to an integer
    station_id = int(station_id)

    # Get the available vehicles at the station
    vehicles = Vehicle.query.filter_by(
        station_id=station_id, status="available").all()

    # Serialize the vehicles as a list of dictionaries
    vehicles_list = [{"id": vehicle.id, "status": vehicle.status}
                     for vehicle in vehicles]

    return jsonify({"vehicles": vehicles_list}), 200


@app.route("/vehicles/pick", methods=["POST"])
def pick_vehicle():
    # Get the vehicle ID and user ID from the request
    vehicle_id = request.json["vehicle_id"]
    user_id = request.json["user_id"]

    # Check if the vehicle is available
    vehicle = Vehicle.query.filter_by(
        id=vehicle_id, status="available").first()
    if not vehicle:
        return jsonify({"error": "Vehicle is not available"}), 400

    # Update the vehicle's status to "in use"
    vehicle.status = "in use"
    db.session.commit()

    # Return the vehicle information to the user
    return jsonify({"vehicle_id": vehicle.id, "status": vehicle.status}), 200


@app.route("/vehicles/return", methods=["POST"])
def return_vehicle():
    # Get the vehicle ID and station ID from the request
    vehicle_id = request.json["vehicle_id"]
    station_id = request.json["station_id"]

    # Check if the vehicle exists
    vehicle = Vehicle.query.filter_by(id=vehicle_id).first()
    if not vehicle:
        return jsonify({"error": "Vehicle does not exist"}), 400

    # Check if the station exists
    station = VehicleStation.query.filter_by(id=station_id).first()
    if not station:
        return jsonify({"error": "Station does not exist"}), 400

    # Update the vehicle's status to "available" and assign it to the station
    vehicle.status = "available"
    vehicle.station_id = station_id
    db.session.commit()

    return jsonify({"message": "Successfully returned vehicle"}), 200
