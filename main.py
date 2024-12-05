from fastapi import FastAPI

app = FastAPI()



@app.get('/user/admin')
async def admin():
    return {'message': "Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def id(user_id: int):
    return {'message': f"Вы вошли как пользователь № {user_id}"}

@app.get('/user')
async def user_id(username: str, age: int):
    return {'message': f"Информация о пользователе. Имя: {username}, Возраст: {age}."}

@app.get('/')
async def main():
    return {'message': "Главная страница"}


#uvicorn src.main:app --reload