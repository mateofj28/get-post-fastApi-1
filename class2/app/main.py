from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routes.user import user_route
from app.routes.publisher import publisher_route
from app.routes.loan import loan_route
from app.routes.category import category_route
from app.routes.book import book_route


app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

app.include_router(user_route, prefix="/users", tags=["users"])
app.include_router(publisher_route, prefix="/publishers", tags=["publishers"])
app.include_router(loan_route, prefix="/loans", tags=["loans"])
app.include_router(category_route, prefix="/categories", tags=["categories"])
app.include_router(book_route, prefix="/books", tags=["books"])


