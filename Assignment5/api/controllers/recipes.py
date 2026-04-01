# Johnny Chen
# ITSC 3155 - Software Engineering
# Assignment 5 - CRUD Operations in FastAPI
# Controller: recipes.py
# Purpose: Handles all CRUD operations for the recipes table

from sqlalchemy.orm import Session
from fastapi import Response, status
from api.models import models



# FUNCTION 1: CREATE
# Purpose: Add a new recipe record to the database


# Step 1: Define the create function
def create(db: Session, recipe):

    # Step 2: Create a new Recipe model instance
    #         sandwich_id = which sandwich, resource_id = which ingredient
    #         amount = how much of that ingredient is needed
    db_recipe = models.Recipe(
        sandwich_id=recipe.sandwich_id,
        resource_id=recipe.resource_id,
        amount=recipe.amount
    )

    # Step 3: Stage the new recipe for insertion
    db.add(db_recipe)

    # Step 4: Commit to save the record
    db.commit()

    # Step 5: Refresh to get auto-generated values like the ID
    db.refresh(db_recipe)

    # Step 6: Return the newly created recipe
    return db_recipe



# FUNCTION 2: READ ALL
# Purpose: Retrieve every recipe record from the database


# Step 1: Define the read_all function
def read_all(db: Session):

    # Step 2: Query and return all rows in the Recipe table
    return db.query(models.Recipe).all()



# FUNCTION 3: READ ONE
# Purpose: Retrieve a single recipe record by its ID


# Step 1: Define the read_one function
def read_one(db: Session, recipe_id):

    # Step 2: Query filtered by recipe_id, return first match or None
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()



# FUNCTION 4: UPDATE
# Purpose: Modify an existing recipe record in the database


# Step 1: Define the update function
def update(db: Session, recipe_id, recipe):

    # Step 2: Query the database to find the recipe record to update
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)

    # Step 3: Convert request data to dictionary, only including provided fields
    update_data = recipe.dict(exclude_unset=True)

    # Step 4: Apply the update to the queried record
    db_recipe.update(update_data, synchronize_session=False)

    # Step 5: Commit the changes
    db.commit()

    # Step 6: Return the updated recipe record
    return db_recipe.first()



# FUNCTION 5: DELETE
# Purpose: Remove a recipe record from the database


# Step 1: Define the delete function
def delete(db: Session, recipe_id):

    # Step 2: Query the database to find the recipe record to delete
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)

    # Step 3: Delete the matched record
    db_recipe.delete(synchronize_session=False)

    # Step 4: Commit the deletion
    db.commit()

    # Step 5: Return HTTP 204 No Content to confirm successful deletion
    return Response(status_code=status.HTTP_204_NO_CONTENT)