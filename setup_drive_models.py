import os
import re
import sys

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the script header."""
    print("=" * 60)
    print("EcoSortAI - Google Drive Model Integration Setup")
    print("=" * 60)
    print("")

def get_file_id_from_url(url):
    """Extract the file ID from a Google Drive sharing URL."""
    match = re.search(r'\/d\/([^\/]+)', url)
    if match:
        return match.group(1)
    return None

def update_app_py(vgg16_id, resnet50_id, inception_id):
    """Update the app.py file with Google Drive file IDs."""
    app_py_path = "app.py"
    
    if not os.path.exists(app_py_path):
        print(f"Error: {app_py_path} not found in the current directory.")
        return False
    
    with open(app_py_path, 'r') as f:
        content = f.read()
    
    # Replace placeholder file IDs with actual IDs
    content = content.replace("'YOUR_VGG16_FILE_ID'", f"'{vgg16_id}'")
    content = content.replace("'YOUR_RESNET50_FILE_ID'", f"'{resnet50_id}'")
    content = content.replace("'YOUR_INCEPTION_FILE_ID'", f"'{inception_id}'")
    
    with open(app_py_path, 'w') as f:
        f.write(content)
    
    return True

def main():
    clear_screen()
    print_header()
    
    print("This script will help you integrate your Google Drive-hosted models with EcoSortAI.")
    print("You'll need to provide the sharing URLs for each model file.\n")
    
    # Get URLs for each model
    print("Step 1: Enter the Google Drive sharing URL for each model file.")
    print("Example URL format: https://drive.google.com/file/d/ABCDEFG1234567890/view?usp=sharing\n")
    
    vgg16_url = input("VGG16 model (vgg16_waste_classification_tf.h5) URL: ")
    resnet50_url = input("ResNet50 model (waste_classification22_model.h5) URL: ")
    inception_url = input("InceptionV3 model (inceptionv3_waste_classification_tf.h5) URL: ")
    
    # Extract file IDs
    vgg16_id = get_file_id_from_url(vgg16_url)
    resnet50_id = get_file_id_from_url(resnet50_url)
    inception_id = get_file_id_from_url(inception_url)
    
    # Validate file IDs
    if not all([vgg16_id, resnet50_id, inception_id]):
        print("\nError: Could not extract valid file IDs from one or more URLs.")
        print("Please make sure you're using the correct sharing URL format.")
        return
    
    # Update app.py with file IDs
    if update_app_py(vgg16_id, resnet50_id, inception_id):
        print("\nSuccess! Your app.py file has been updated with the Google Drive file IDs.")
        print("\nNext steps:")
        print("1. Commit and push these changes to your Git repository")
        print("2. Deploy your application using the instructions in DEPLOYMENT_GUIDE.md")
        print("\nYour application will now download models from Google Drive when needed.")
    else:
        print("\nFailed to update app.py. Please check file permissions and try again.")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
