from PIL import Image

def encode_image(image_path, secret_message):
    image = Image.open(image_path)
    width, height = image.size

    if len(secret_message) * 3 > width * height:
        print("Error: The secret message is too large to fit in the image.")
        return

    secret_message += "###"  # Add a delimiter to mark the end of the message

    encoded_image = image.copy()

    index = 0
    for i in range(width):
        for j in range(height):
            pixel = list(image.getpixel((i, j)))

            if index < len(secret_message):
                ascii_value = ord(secret_message[index])

                # Encode each character in the R, G, and B components of the pixel
                pixel[0] = (pixel[0] & 0xFE) | ((ascii_value >> 7) & 1)
                pixel[1] = (pixel[1] & 0xFE) | ((ascii_value >> 6) & 1)
                pixel[2] = (pixel[2] & 0xFE) | ((ascii_value >> 5) & 1)

                encoded_image.putpixel((i, j), tuple(pixel))

            index += 1

    encoded_image.save("encoded_image.png")
    print("Steganography completed successfully. Encoded image saved as 'encoded_image.png'")


def decode_image(encoded_image_path):
    encoded_image = Image.open(encoded_image_path)
    width, height = encoded_image.size

    decoded_message = ""
    index = 0

    for i in range(width):
        for j in range(height):
            pixel = encoded_image.getpixel((i, j))

            # Extract the LSB from each component of the pixel and reconstruct the ASCII value
            ascii_value = (pixel[0] & 1) << 7 | (pixel[1] & 1) << 6 | (pixel[2] & 1) << 5

            if chr(ascii_value) == "#":
                return decoded_message

            decoded_message += chr(ascii_value)

            index += 1

    return decoded_message


# Example usage
image_path = "./img/1.png"
secret_message = "This is a secret message!"

encode_image(image_path, secret_message)

decoded_message = decode_image("encoded_image.png")
print("Decoded Message:", decoded_message)
