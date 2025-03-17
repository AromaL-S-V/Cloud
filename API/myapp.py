from fastapi import FastAPI
app = FastAPI(title="Myapp")

@app.get("/a")
def root():
    return{"Aromal": "S"}

@app.get("/sum")
def sumofnumbers(a: int, b: int):
    return {"sum": a + b}