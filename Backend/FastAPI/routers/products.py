from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"], responses={404: {"description": "Not found"}}) 

products_list = ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"]

# Get products
@router.get("/")
async def get_products():
    return products_list

# Get product by id
@router.get("/{id}")
async def get_product_by_id(id: int):
    return products_list[id]