from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Home Page: Hello World"}

@app.get("/about")
async def about():
    return {"message": "About Page: This is the about page"}

@app.get("/help")
async def about():
    return {"message": "Help Page: This is the help page"}
