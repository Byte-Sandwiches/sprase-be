from src.helper.worker import csr
from src.helper.ws import ws

async def check_service(data):
    res = {"pincode": data['pincode']}
    res["does"] = csr.is_there(data['merchid'], data['pincode'])

    ws.publish(f"csr_{data['pincode']}", res)

async def add_data(data):
    csr.row_pointers = data[0]["data"].split(",")
    csr.column_indices = data[1]["data"].split(",")
    csr.values = data[2]["data"].split(",")

async def get_merchants(pin):
    csr.based_merchants(pin)
