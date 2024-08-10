from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import config
from routes import GET_endpoints as GET
from routes import POST_endpoints as POST

app = FastAPI(docs_url=False)

app.include_router(router=POST.app, prefix="/post")

app.include_router(router=GET.app, prefix="/get")

origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)