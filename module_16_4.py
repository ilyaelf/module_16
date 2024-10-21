from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_users() -> str:
    return f'{users}'


@app.post('/user/{username}/{age}')
async def add_user(user: User) -> str:
    if users == []:
        user.id = 1
    else:
        user.id = users[-1].id + 1
    users.append(user)
    return (f'user_id:{user.id}, name:{user.username}, age:{user.age}, was created')


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> str:
    flag = False
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            flag = True
    if flag:
        return f'User {user_id} has been updated to Username:{user.username},age:{user.age}'
    else:
        raise HTTPException(status_code=404, detail='user not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    flag = False
    for user in users:
        if user.id == user_id:
            users.remove(user)
            flag = True
    if flag:
        return f"User {user_id} has been deleted"
    else:
        raise HTTPException(status_code=404, detail='user not found')


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
