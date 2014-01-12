__author__ = 'Perun'

if __name__ == "__main__":
    from app import app#, db
    #db.create_all()
    app.run(debug=True)
