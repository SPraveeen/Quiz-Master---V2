from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def temp():
    return {'message':'Hi!'}