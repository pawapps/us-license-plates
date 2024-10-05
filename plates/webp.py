import os
from PIL import Image

def convert_images_to_webp():
    # Get the current working directory
    root_dir = os.getcwd()

    # Walk through all directories and subdirectories
    for subdir, _, files in os.walk(root_dir):
        for filename in files:
            filepath = os.path.join(subdir, filename)
            
            # Skip if it's already a WebP file
            if filename.lower().endswith(".webp"):
                # print(f"Skipping WebP file: {filepath}")
                continue

            # Generate the corresponding WebP filename
            webp_filename = os.path.splitext(filepath)[0] + ".webp"
            
            # Check if the WebP file already exists
            if os.path.exists(webp_filename):
                print(f"WebP file already exists for {filename}, deleting original.")
                os.remove(filepath)
                continue
            
            # Try to convert the image to WebP
            try:
                with Image.open(filepath) as img:
                    # Convert the image to RGB to handle all modes
                    img = img.convert("RGB")
                    
                    # Save the image in WebP format
                    img.save(webp_filename, "WEBP")
                    print(f"Converted: {filepath} to {webp_filename}")
                    
                    # Remove the original file after successful conversion
                    os.remove(filepath)
                    print(f"Deleted original file: {filepath}")
            
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    convert_images_to_webp()
