if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", port=8000, reload=True)
