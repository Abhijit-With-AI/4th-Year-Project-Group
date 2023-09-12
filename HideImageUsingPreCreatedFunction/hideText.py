from stegano import lsb
from PIL import Image

# Function to hide text inside an image
def hide_text_in_image(cover_image_path, hidden_text, output_image_path):
    # Open the cover image
    cover_image = Image.open(cover_image_path)

    # Hide the text inside the cover image using LSB steganography
    secret_image = lsb.hide(cover_image, hidden_text)

    # Save the resulting image with the hidden text
    secret_image.save(output_image_path)

# Function to reveal hidden text from an image
def reveal_text_from_image(secret_image_path):
    # Open the secret image
    secret_image = Image.open(secret_image_path)

    # Extract the hidden text using LSB steganography
    hidden_text = lsb.reveal(secret_image)

    return hidden_text

# Example usage
cover_image_path = "docker.png"
hidden_text = "This is a hidden message."
output_image_path = "secret_image.png"

# Hide the text inside the cover image
hide_text_in_image(cover_image_path, hidden_text, output_image_path)
print("Text hidden successfully.")

# Reveal the hidden text from the secret image
revealed_text = reveal_text_from_image(output_image_path)
print("\nRevealed Text:")
print(revealed_text)
