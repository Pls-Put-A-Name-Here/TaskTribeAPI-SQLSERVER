from requests import post

# move key to an environment variable



import requests

import requests
import base64


def store_image(image) -> str:
    """
    This function takes an image and uploads it to the imgbb API.
    :param image: image to upload
    :return: URL of the uploaded image
    """

    url = 'https://api.imgbb.com/1/upload'
    apikey = 'e20be0a219120d5d9fc5ae85c1e715c9'

    # Read the image file content
    image_data = image.read()

    # Encode the image file content in base64
    image_base64 = base64.b64encode(image_data).decode('utf-8')

    payload = {
        'key': apikey,
        'image': image_base64
    }

    try:
        response = requests.post(url, data=payload)
        # Raise an error if the response is not ok
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error uploading image: {e}")
        return None

    response_data = response.json()
    if response_data['status'] == 200:
        return response_data['data']['url']
    else:
        print(f"Error in response: {response_data}")
        return None


