import requests
import PIL as Image

# Replace YOUR_API_KEY with your actual API key
API_KEY = 'API_KEY'

# Set the text that you want to generate an image for
text = 'text to image'

# Set the size of the generated image
size = '1024x1024'

# Set the response format to 'png'
response_format = 'png'

# Set the DALL-E endpoint URL
endpoint_url = f'https://api.openai.com/v1/images/generations'

# Set the headers for the request
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {API_KEY}'
}

def generate_image(text, size, response_format):
  # Set the payload for the request
  payload = {
    'model': 'image-alpha-001',
    'prompt': text,
    'size': size,
    'response_format': response_format
  }

  # Send the POST request
  response = requests.post(endpoint_url, json=payload, headers=headers)

  # Open the image using the Pillow library
  image = Image.open(requests.get(response.json()['data'][0]['url'], stream=True).raw)

  # Display the image
  image.show()

def main():
  # Get the text input from the user
  text = input("Enter the text that you want to generate an image for: ")

  # Get the size input from the user
  size = input("Enter the size of the generated image (e.g. 1024x1024): ")

  # Call the generate_image function with the user-provided text and size
  generate_image(text, size, response_format)

if __name__ == "__main__":
  main()