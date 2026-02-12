import uvicorn

if __name__ == "__main__":
    print("Starting CareerLens AI Backend on 0.0.0.0:9000...")
    uvicorn.run("app.main:app", host="0.0.0.0", port=9000, reload=True)
