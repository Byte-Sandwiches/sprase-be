from fastapi import FastAPI, Depends
from utils import make_post_request

app = FastAPI()

# Access user ID from middleware (replace with your authentication logic)
async def get_user_id(request):
    
    return 12345  

@app.post("/collect_data")
async def collect_data(
    city_pincodes: list[str] = Body(..., embed=True),
    user_id: str = Depends(get_user_id),
):
    
    merchant_id = "your_merchant_id"  
    url = "https://your_api_endpoint/collect_data"  
    response = make_post_request(merchant_id, city_pincodes, url)

   
    if response.status_code == 200:
        return {"message": "Data collected successfully"}
    else:
        return {"error": f"API error: {response.status_code}"}
