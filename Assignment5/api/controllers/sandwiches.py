# Johnny Chen
# ITSC 3155 - Software Engineering
# Assignment 5 - CRUD Operations in FastAPI
# Controller: sandwiches.py
# Purpose: Handles all CRUD operations for the sandwiches table

from sqlalchemy.orm import Session
from fastapi import Response, status
from api.models import models


# FUNCTION 1: CREATE
# Purpose: Add a new sandwich record to the database

# Step 1: Define the create function
#         It takes a database session and the sandwich data as parameters
def create(db: Session, sandwich):

    # Step 2: Create a new Sandwich model instance
    #         Map the incoming request fields to the database model fields
    db_sandwich = models.Sandwich(
        sandwich_name=sandwich.sandwich_name,
        price=sandwich.price
    )

    # Step 3: Add the new sandwich object to the database session
    #         This stages it for insertion but does NOT save it yet
    db.add(db_sandwich)

    # Step 4: Commit the session to permanently save the record to the database
    db.commit()

    # Step 5: Refresh the object so it reflects the latest data from the database
    #         This is important for capturing auto-generated values like the ID
    db.refresh(db_sandwich)

    # Step 6: Return the newly created sandwich so the API can send it back
    return db_sandwich


# FUNCTION 2: READ ALL
# Purpose: Retrieve every sandwich record from the database


# Step 1: Define the read_all function
#         It only needs the database session as a parameter
def read_all(db: Session):

    # Step 2: Query the Sandwich table and fetch all rows
    #         .all() returns a list of Sandwich objects (empty list if none exist)
    return db.query(models.Sandwich).all()


# FUNCTION 3: READ ONE
# Purpose: Retrieve a single sandwich record by its ID


# Step 1: Define the read_one function
#         Takes the database session and the sandwich_id to look up
def read_one(db: Session, sandwich_id):

    # Step 2: Query the Sandwich table
    #         Use .filter() to match only the row where id == sandwich_id
    #         Use .first() to return that one record, or None if not found
    return db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()



# FUNCTION 4: UPDATE
# Purpose: Modify an existing sandwich record in the database


# Step 1: Define the update function
#         Takes the session, the sandwich_id to find, and the new sandwich data
def update(db: Session, sandwich_id, sandwich):

    # Step 2: Query the database to find the sandwich record that needs updating
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)

    # Step 3: Convert the incoming sandwich data into a dictionary
    #         exclude_unset=True means only include fields that were actually provided
    #         This allows partial updates (e.g., update price without changing name)
    update_data = sandwich.dict(exclude_unset=True)

    # Step 4: Apply the update to the queried record
    #         synchronize_session=False improves performance for bulk updates
    db_sandwich.update(update_data, synchronize_session=False)

    # Step 5: Commit the changes to permanently save them to the database
    db.commit()

    # Step 6: Return the updated sandwich record
    return db_sandwich.first()



# FUNCTION 5: DELETE
# Purpose: Remove a sandwich record from the database


# Step 1: Define the delete function
#         Takes the database session and the sandwich_id to remove
def delete(db: Session, sandwich_id):

    # Step 2: Query the database to find the sandwich record to delete
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)

    # Step 3: Delete the matched record from the database
    #         synchronize_session=False skips session sync for better performance
    db_sandwich.delete(synchronize_session=False)

    # Step 4: Commit the deletion to permanently remove it from the database
    db.commit()

    # Step 5: Return HTTP 204 No Content
    #         This is the standard REST response to confirm a successful deletion
    return Response(status_code=status.HTTP_204_NO_CONTENT)