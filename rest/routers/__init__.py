from fastapi import APIRouter
from rest.routers import product

router = APIRouter()

router.include_router(router=product.router, prefix="/product" , tags=["Product Service"])