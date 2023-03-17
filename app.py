# app.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root(name = None):
	
	if name is None:
		text = 'World'
	else:
		text = name
	return {"message": "Hello " + text + "!"}