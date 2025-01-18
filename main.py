from os import getenv

from dotenv import load_dotenv

load_dotenv()
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", port=getenv("PORT_NUMBER", 8000), reload=True)
