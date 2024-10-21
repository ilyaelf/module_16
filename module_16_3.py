from fastapi import FastAPI,Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return {"users":f"{users.items()}"}

@app.post('/user/{username}/{age}')
async def add_user(username:str=Path(min_length=5,
                                    max_length=20),
                        age:int=Path(le=120,
                                    ge=10)) -> str:
    username_age = (f'Имя: {username}, возраст: {age}')
    id_new = str(int(max(users,key=int))+1)
    users[id_new]=username_age
    return f"User {id_new} is registred"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id:str=Path(
                                   description=f'choice from {users.keys()}'
                                            ),
                        username:str=Path(min_length=5,
                                        max_length=20),
                            age:int=Path(le=120,
                                        ge=10)) -> str:
    username_age = f'Имя: {username}, возраст: {age}'
    users[user_id]=username_age
    return f"User {user_id} has been updated"

@app.delete('/user/{user_id}')
async def delete_user(user_id:str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)