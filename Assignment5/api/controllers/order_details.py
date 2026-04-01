# Johnny Chen
# ITSC 3155 - Software Engineering
# Assignment 5 - CRUD Operations in FastAPI
# Controller: order_details.py
# Purpose: Handles all CRUD operations for the order_details table

from sqlalchemy.orm import Session
from fastapi import Response, status
from api.models import models


# ==============================================================================
# FUNCTION 1: CREATE
# Purpose: Add a new order detail record to the database
# ==============================================================================

# Step 1: Define the create function
def create(db: Session, order_detail):

    # Step 2: Create a new OrderDetail model instance
    #         order_id = which order, sandwich_id = which sandwich
    #         amount = how many of that sandwich were ordered
    db_order_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        amount=order_detail.amount
    )

    # Step 3: Stage the new order detail for insertion
    db.add(db_order_detail)

    # Step 4: Commit to save the record
    db.commit()

    # Step 5: Refresh to get auto-generated values like the ID
    db.refresh(db_order_detail)

    # Step 6: Return the newly created order detail
    return db_order_detail


# ==============================================================================
# FUNCTION 2: READ ALL
# Purpose: Retrieve every order detail record from the database
# ==============================================================================

# Step 1: Define the read_all function
def read_all(db: Session):

    # Step 2: Query and return all rows in the OrderDetail table
    return db.query(models.OrderDetail).all()


# ==============================================================================
# FUNCTION 3: READ ONE
# Purpose: Retrieve a single order detail record by its ID
# ==============================================================================

# Step 1: Define the read_one function
def read_one(db: Session, order_detail_id):

    # Step 2: Query filtered by order_detail_id, return first match or None
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()


# ==============================================================================
# FUNCTION 4: UPDATE
# Purpose: Modify an existing order detail record in the database
# ==============================================================================

# Step 1: Define the update function
def update(db: Session, order_detail_id, order_detail):

    # Step 2: Query the database to find the order detail record to update
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)

    # Step 3: Convert request data to dictionary, only including provided fields
    update_data = order_detail.dict(exclude_unset=True)

    # Step 4: Apply the update to the queried record
    db_order_detail.update(update_data, synchronize_session=False)

    # Step 5: Commit the changes
    db.commit()

    # Step 6: Return the updated order detail record
    return db_order_detail.first()


# ==============================================================================
# FUNCTION 5: DELETE
# Purpose: Remove an order detail record from the database
# ==============================================================================

# Step 1: Define the delete function
def delete(db: Session, order_detail_id):

    # Step 2: Query the database to find the order detail record to delete
    db_order_detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id)

    # Step 3: Delete the matched record
    db_order_detail.delete(synchronize_session=False)

    # Step 4: Commit the deletion
    db.commit()

    # Step 5: Return HTTP 204 No Content to confirm successful deletion
    return Response(status_code=status.HTTP_204_NO_CONTENT)