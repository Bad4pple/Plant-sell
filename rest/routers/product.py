from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_products():
    return {"product": "osld"}

@router.get("/{id}")
async def get_product_from_id(id: int):
    return {'id': id}


@router.get("/{title}")
async def get_product_from_title(title: str):
    return {'title': str}

@router.post("/create")
async def create_product():
    return "product"

@router.put('/{id}')
async def update_product(id: int):
    return {'id': id}

@router.delete('/{id}')
async def delete_product(id: int):
    return {'id': id}