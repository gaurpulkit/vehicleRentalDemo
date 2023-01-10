from app import app, db

if __name__ == "__main__":
    # Initialize the database
    db.create_all()

    # Run the app
    app.run(debug=True)
