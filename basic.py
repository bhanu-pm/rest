# REST basic file 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class RequestStructure(BaseModel):
	num1: float
	num2: float

@app.post("/add")
def add(request: RequestStructure):
	result = request.num1 + request.num2
	return {"num1": request.num1, "num2": request.num2, "result": result}

@app.post("/minus")
def subtract(request: RequestStructure):
	result = request.num1 - request.num2
	return {"num1": request.num1, "num2": request.num2, "result": result}

@app.post("/multiply")
def product(request: RequestStructure):
	result = request.num1 * request.num2
	return {"num1": request.num1, "num2": request.num2, "result": result}

@app.post("/divide")
def division(request: RequestStructure):
	if request.num2 != 0:
		result = request.num1 / request.num2
		return {"num1": request.num1, "num2": request.num2, "result": result}

	raise HTTPException(status_code=400, detail="Divide by 0 error")

if __name__ == "__main__":
	pass
