import requests
import json

def make_post_request(merchant_id, city_pincodes, url):
   

 
    if not merchant_id or not city_pincodes:
        raise ValueError("Missing merchant ID or city pincodes.")


    data = {
        "merchant_id": merchant_id,
        "city_pincodes": city_pincodes,
        "source": "User_Input", 
        "use_case": "Delivery_Estimation",  
        "anonymized": True,  
    }

   
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  
        return response
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error sending POST request: {e}")
