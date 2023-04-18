from os import getenv

import psycopg2
from dotenv import load_dotenv
from fastapi import FastAPI, Response, status
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

import login_proc

app = FastAPI()
load_dotenv()

DB_HOST, DB_NAME, DB_USER, DB_PASSWORD = getenv('DB_HOST'), getenv('DB_NAME'), getenv('DB_USER'), getenv('DB_PASSWORD')
db = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, port=5432)

cursor = db.cursor()
DevMode = getenv("DEV_MODE") == "True"


class IntranetLoginData(BaseModel):
    login_id: str
    login_pw: str


@app.get("/", response_class=HTMLResponse)
async def index():
    return open("pages/index.html", "r").read()


@app.get("/as_personal_code", response_class=HTMLResponse)
async def as_personal_code():
    return open("pages/as_personal_code.html", "r").read()


@app.get("/as_intranet_account", response_class=HTMLResponse)
async def as_intranet_account():
    return open("pages/as_intranet_account.html", "r").read()


@app.get("/inquiry", response_class=HTMLResponse)
async def inquiry():
    return open("pages/inquiry.html", "r").read()


@app.post("/intranet_login")
async def intranet_login(data: IntranetLoginData, response: Response):
    try:
        code = login_proc.get_personal_code(data.login_id, data.login_pw)
        if code == "E html":
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"message": "로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요."}
        else:
            if DevMode:
                return {"code": getenv("DEMO_KEY")}
            else:
                return {"code": code}
    except Exception as e:
        if DevMode:
            return {"message": str(e)}
        else:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return {"message": "로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요."}


@app.get("/query")
async def query(code: str):
    sql_query = "SELECT * FROM examroom WHERE code = %s"
    cursor.execute(sql_query, (code,))
    data = cursor.fetchall()
    return data
