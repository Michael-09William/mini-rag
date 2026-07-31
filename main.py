from fastapi import FastAPI

app=FastAPI()

@app.get('/welcome')
async def welcome():
    return{'Message':'Hello There'}