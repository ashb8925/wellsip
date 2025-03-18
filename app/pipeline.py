import requests
from django.core.files.base import ContentFile

def save_profile_picture(backend, user, response, *args, **kwargs):
    if backend.name == 'google-oauth2':
        profile_pic_url = response.get('picture')  # Get Google profile pic URL
        if profile_pic_url:
            response = requests.get(profile_pic_url)  # Download the image
            if response.status_code == 200:
                user.profile_picture.save(f"{user.username}_google.jpg", ContentFile(response.content), save=True)
