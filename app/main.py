from typing import Union
from datetime import datetime
from fastapi import FastAPI


app = FastAPI()


def test_ipfs_hash():
    curr_dt = datetime.now()
    timestamp = int(round(curr_dt.timestamp()))
    return str(timestamp)


@app.get("/")
def read_root():
    return "OK"


@app.post("/pinning/pinFileToIPFS")
def pin_file():
    return {"IpfsHash": test_ipfs_hash()}


@app.post("/pinning/pinJSONToIPFS")
def pin_json():
    return {"IpfsHash": test_ipfs_hash()}
