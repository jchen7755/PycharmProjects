# Johnny Chen
# ITSC 3155 - Software Engineering
# Assignment 5 - CRUD Operations in FastAPI
# File: main.py
# Purpose: Entry point for the FastAPI application.
#          Defines and registers all API endpoints for every table.
#          Routes each HTTP request to the correct controller function.


# FastAPI core imports for building the app and handling errors
from fastapi import Depends, FastAPI, HTTPException

# SQLAlchemy Session for database interaction
from sqlalchemy.orm import Session

# Import all controller files - each one handles CRUD for one table
from api.controllers import orders, sandwiches, resources, recipes, order_details

# Import models (database table definitions) and schemas (data shapes for API)
from api.models import models, schemas

# Import the database engine and the get_db dependency function
from api.dependencies.database import engine, get_db


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# ORDERS ENDPOINTS (Sample / Reference Implementation)

# Step 1: Register as a POST endpoint for creating a new order
@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
# Step 2: Define the function with order data and database session
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    # Step 3: Call the orders controller create function and return the result
    return orders.create(db=db, order=order)


# Step 1: Register as a GET endpoint that returns a list of all orders
@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
# Step 2: Define the function - only needs the database session
def read_orders(db: Session = Depends(get_db)):
    # Step 3: Call the controller and return all orders
    return orders.read_all(db)


# Step 1: Register as a GET endpoint with a dynamic {order_id} parameter
@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
# Step 2: Define the function - takes order_id from the URL and db session
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    # Step 3: Ask the controller to find the order by ID
    order = orders.read_one(db, order_id=order_id)
    # Step 4: If not found raise a 404 error
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    # Step 5: Return the found order
    return order


# Step 1: Register as a PUT endpoint with a dynamic {order_id} parameter
@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
# Step 2: Define the function - takes the ID, updated data, and db session
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    # Step 3: Confirm the order exists before attempting an update
    order_db = orders.read_one(db, order_id=order_id)
    # Step 4: If not found raise a 404 error
    if order_db is None:
        raise HTTPException(status_code=404, detail="Order not found")
    # Step 5: Call the update function and return the updated order
    return orders.update(db=db, order=order, order_id=order_id)


# Step 1: Register as a DELETE endpoint with a dynamic {order_id} parameter
@app.delete("/orders/{order_id}", tags=["Orders"])
# Step 2: Define the function - takes order_id and the database session
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    # Step 3: Confirm the order exists before attempting deletion
    order = orders.read_one(db, order_id=order_id)
    # Step 4: If not found raise a 404 error
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    # Step 5: Call the delete function and return the result
    return orders.delete(db=db, order_id=order_id)


# Step 1: Register as a POST endpoint for creating a new sandwich
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
# Step 2: Define the function with sandwich data and database session
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    # Step 3: Delegate to the sandwiches controller and return the result
    return sandwiches.create(db=db, sandwich=sandwich)


# Step 1: Register as a GET endpoint that returns a list of all sandwiches
@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
# Step 2: Define the function - only needs the database session
def read_sandwiches(db: Session = Depends(get_db)):
    # Step 3: Return all sandwiches from the controller
    return sandwiches.read_all(db)


# Step 1: Register as a GET endpoint with a dynamic {sandwich_id} parameter
@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
# Step 2: Define the function - takes sandwich_id from the URL and db session
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    # Step 3: Ask the controller to find the sandwich by ID
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    # Step 4: If not found raise a 404 error
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    # Step 5: Return the found sandwich
    return sandwich


# Step 1: Register as a PUT endpoint with a dynamic {sandwich_id} parameter
@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
# Step 2: Define the function - takes the ID, updated data, and db session
def update_one_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    # Step 3: Confirm the sandwich exists before attempting an update
    sandwich_db = sandwiches.read_one(db, sandwich_id=sandwich_id)
    # Step 4: If not found raise a 404 error
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    # Step 5: Call the update function and return the updated sandwich
    return sandwiches.update(db=db, sandwich=sandwich, sandwich_id=sandwich_id)


# Step 1: Register as a DELETE endpoint with a dynamic {sandwich_id} parameter
@app.delete("/sandwiches/{sandwich_id}", tags=["Sandwiches"])
# Step 2: Define the function - takes sandwich_id and the database session
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    # Step 3: Confirm the sandwich exists before attempting deletion
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    # Step 4: If not found raise a 404 error
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    # Step 5: Call the delete function and return the result
    return sandwiches.delete(db=db, sandwich_id=sandwich_id)


# Step 1: Register as a POST endpoint for creating a new resource
@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
# Step 2: Define the function with resource data and database session
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    # Step 3: Delegate to the resources controller and return the result
    return resources.create(db=db, resource=resource)


# Step 1: Register as a GET endpoint that returns a list of all resources
@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
# Step 2: Define the function - only needs the database session
def read_resources(db: Session = Depends(get_db)):
    # Step 3: Return all resources from the controller
    return resources.read_all(db)


# Step 1: Register as a GET endpoint with a dynamic {resource_id} parameter
@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
# Step 2: Define the function - takes resource_id from the URL and db session
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    # Step 3: Ask the controller to find the resource by ID
    resource = resources.read_one(db, resource_id=resource_id)
    # Step 4: If not found raise a 404 error
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    # Step 5: Return the found resource
    return resource


# Step 1: Register as a PUT endpoint with a dynamic {resource_id} parameter
@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
# Step 2: Define the function - takes the ID, updated data, and db session
def update_one_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    # Step 3: Confirm the resource exists before attempting an update
    resource_db = resources.read_one(db, resource_id=resource_id)
    # Step 4: If not found raise a 404 error
    if resource_db is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    # Step 5: Call the update function and return the updated resource
    return resources.update(db=db, resource=resource, resource_id=resource_id)


# Step 1: Register as a DELETE endpoint with a dynamic {resource_id} parameter
@app.delete("/resources/{resource_id}", tags=["Resources"])
# Step 2: Define the function - takes resource_id and the database session
def delete_one_resource(resource_id: int, db: Session = Depends(get_db)):
    # Step 3: Confirm the resource exists before attempting deletion
    resource = resources.read_one(db, resource_id=resource_id)
    # Step 4: If not found raise a 404 error
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    # Step 5: Call the delete function and return the result
    return resources.delete(db=db, resource_id=resource_id)


# Step 1: Register as a POST endpoint for creating a new recipe
@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
# Step 2: Define the function with recipe data and database session
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    # Step 3: Delegate to the recipes controller and return the result
    return recipes.create(db=db, recipe=recipe)


# Step 1: Register as a GET endpoint that returns a list of all recipes
@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipes"])
# Step 2: Define the function - only needs the database session
def read_recipes(db: Session = Depends(get_db)):
    # Step 3: Return all recipes from the controller
    return recipes.read_all(db)


# Step 1: Register as a GET endpoint with a dynamic {recipe_id} parameter
@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
# Step 2: Define the function - takes recipe_id from the URL and db session
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    # Step 3: Ask the controller to find the recipe by ID
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    # Step 4: If not found raise a 404 error
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    # Step 5: Return the found recipe
    return recipe


# Step 1: Register as a PUT endpoint with a dynamic {recipe_id} parameter
@app.put("/recipes/{recipe_id}", response_model=schemas.Recipe, tags=["Recipes"])
# Step 2: Define the function - takes the ID, updated data, and db session
def update_one_recipe(recipe_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    # Step 3: Confirm the recipe exists before attempting an update
    recipe_db = recipes.read_one(db, recipe_id=recipe_id)
    # Step 4: If not found raise a 404 error
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    # Step 5: Call the update function and return the updated recipe
    return recipes.update(db=db, recipe=recipe, recipe_id=recipe_id)


# Step 1: Register as a DELETE endpoint with a dynamic {recipe_id} parameter
@app.delete("/recipes/{recipe_id}", tags=["Recipes"])
# Step 2: Define the function - takes recipe_id and the database session
def delete_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    # Step 3: Confirm the recipe exists before attempting deletion
    recipe = recipes.read_one(db, recipe_id=recipe_id)
    # Step 4: If not found raise a 404 error
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    # Step 5: Call the delete function and return the result
    return recipes.delete(db=db, recipe_id=recipe_id)


# ==============================================================================
# ORDER DETAILS ENDPOINTS
# ==============================================================================

# Step 1: Register as a POST endpoint for creating a new order detail
@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["Order Details"])
# Step 2: Define the function with order_detail data and database session
def create_order_detail(order_detail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    # Step 3: Delegate to the order_details controller and return the result
    return order_details.create(db=db, order_detail=order_detail)


# Step 1: Register as a GET endpoint that returns a list of all order details
@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["Order Details"])
# Step 2: Define the function - only needs the database session
def read_order_details(db: Session = Depends(get_db)):
    # Step 3: Return all order detail records from the controller
    return order_details.read_all(db)


# Step 1: Register as a GET endpoint with a dynamic {order_detail_id} parameter
@app.get("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["Order Details"])
# Step 2: Define the function - takes order_detail_id from the URL and db session
def read_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    # Step 3: Ask the controller to find the order detail by ID
    order_detail = order_details.read_one(db, order_detail_id=order_detail_id)
    # Step 4: If not found raise a 404 error
    if order_detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    # Step 5: Return the found order detail
    return order_detail


# Step 1: Register as a PUT endpoint with a dynamic {order_detail_id} parameter
@app.put("/order_details/{order_detail_id}", response_model=schemas.OrderDetail, tags=["Order Details"])
# Step 2: Define the function - takes the ID, updated data, and db session
def update_one_order_detail(order_detail_id: int, order_detail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    # Step 3: Confirm the order detail exists before attempting an update
    order_detail_db = order_details.read_one(db, order_detail_id=order_detail_id)
    # Step 4: If not found raise a 404 error
    if order_detail_db is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    # Step 5: Call the update function and return the updated order detail
    return order_details.update(db=db, order_detail=order_detail, order_detail_id=order_detail_id)


# Step 1: Register as a DELETE endpoint with a dynamic {order_detail_id} parameter
@app.delete("/order_details/{order_detail_id}", tags=["Order Details"])
# Step 2: Define the function - takes order_detail_id and the database session
def delete_one_order_detail(order_detail_id: int, db: Session = Depends(get_db)):
    # Step 3: Confirm the order detail exists before attempting deletion
    order_detail = order_details.read_one(db, order_detail_id=order_detail_id)
    # Step 4: If not found raise a 404 error
    if order_detail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    # Step 5: Call the delete function and return the result
    return order_details.delete(db=db, order_detail_id=order_detail_id)