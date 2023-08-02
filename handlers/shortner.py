import requests
from database import udb as db

async def get_shorturl(link, u_id: int):
    try:
        shortener_url = await db.get_shortner(u_id)
        shortener_api = await db.get_api(u_id)
        if shortener_url == "None" or shortener_api == "None":
            return link
        api_url = f'https://{shortener_url}/api'
        params = {'api': shortener_api, 'url': link}
        response = requests.get(api_url, params=params)
        response_data = response.json()
        if 'status' in response_data and response_data['status'] == 'success' and 'shortenedUrl' in response_data:
            return response_data['shortenedUrl']
        else:
            return link
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while accessing the shortening service: {e}")
        return link
    except ValueError as ve:
        print(f"Invalid response data from shortening service: {ve}")
        return link
