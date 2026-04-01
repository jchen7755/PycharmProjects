# Johnny Chen
# ITSC 3155 - Software Engineering
# Assignment 5 - CRUD Operations in FastAPI
# Controller: resources.py
# Purpose: Handles all CRUD operations for the resources table

from sqlalchemy.orm import Session
from fastapi import Response, status
from api.models import models


# ==============================================================================
# FUNCTION 1: CREATE
# Purpose: Add a new resource (ingredient) record to the database
# ==============================================================================

# Step 1: Define the create function
#         Takes a database session and the resource data as parameters
def create(db: Session, resource):

    # Step 2: Create a new Resource model instance
    #         item = the name of the ingredient, amount = quantity available
    db_resource = models.Resource(
        item=resource.item,
        amount=resource.amount
    )

    # Step 3: Add the new resource object to the database session
    db.add(db_resource)

    # Step 4: Commit the session to permanently save the record
    db.commit()

    # Step 5: Refresh the object to get any auto-generated values like the ID
    db.refresh(db_resource)

    # Step 6: Return the newly created resource
    return db_resource


# ==============================================================================
# FUNCTION 2: READ ALL
# Purpose: Retrieve every resource record from the database
# ==============================================================================

# Step 1: Define the read_all function
def read_all(db: Session):

    # Step 2: Query the Resource table and return all rows as a list
    return db.query(models.Resource).all()


# ==============================================================================
# FUNCTION 3: READ ONE
# Purpose: Retrieve a single resource record by its ID
# ==============================================================================

# Step 1: Define the read_one function
def read_one(db: Session, resource_id):

    # Step 2: Query filtered by resource_id, return first match or None
    return db.query(models.Resource).filter(models.Resource.id == resource_id).first()


# ==============================================================================
# FUNCTION 4: UPDATE
# Purpose: Modify an existing resource record in the database
# ==============================================================================

# Step 1: Define the update function
def update(db: Session, resource_id, resource):

    # Step 2: Query the database to find the resource record to update
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)

    # Step 3: Convert request data to dictionary, only including provided fields
    update_data = resource.dict(exclude_unset=True)

    # Step 4: Apply the update to the queried record
    db_resource.update(update_data, synchronize_session=False)

    # Step 5: Commit the changes to the database
    db.commit()

    # Step 6: Return the updated resource record
    return db_resource.first()


# ==============================================================================
# FUNCTION 5: DELETE
# Purpose: Remove a resource record from the database
# ==============================================================================

# Step 1: Define the delete function
def delete(db: Session, resource_id):

    # Step 2: Query the database to find the resource record to delete
    db_resource = db.query(models.Resource).filter(models.Resource.id == resource_id)

    # Step 3: Delete the matched record
    db_resource.delete(synchronize_session=False)

    # Step 4: Commit the deletion
    db.commit()

    # Step 5: Return HTTP 204 No Content to confirm successful deletion
    return Response(status_code=status.HTTP_204_NO_CONTENT)