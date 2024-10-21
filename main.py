from fastapi import FastAPI,Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def main_page() -> dict:
    return {"message":"Главная страница"}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user(user_id:int = Path(le=100,ge=1,
                                  description="Enter User ID",
                                  example="12")) -> dict:
    return {"message": f"Вы вошли как пользователь №{user_id}"}

@app.get("/user/{username}/{age}")
async def username_age(username:Annotated[str,Path(min_length=5,
                                                   max_length=20,
                                                   description="Enter username",
                                                   example="UrbanUser")],
                            age:Annotated[int,Path(ge=18,
                                                   le=120,
                                                   description="Enter age",
                                                   example="24")]) -> dict:
    return {"message" :f"Информация о пользователе. Имя:{username}, Возраст:{age}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)