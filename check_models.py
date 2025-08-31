import os
import sys
import requests
import re

# Define model paths
MODEL_FOLDER = "models"
MODEL_FILES = [
    "vgg16_waste_classification_tf.h5",
    "waste_classification22_model.h5",
    "inceptionv3_waste_classification_tf.h5"
]

def check_local_models():
    """Check if models exist locally."""
    missing_models = []
    for model_file in MODEL_FILES:
        model_path = os.path.join(MODEL_FOLDER, model_file)
        if not os.path.exists(model_path):
            missing_models.append(model_file)
    
    return missing_models

def extract_drive_ids_from_app_py():
    """Extract Google Drive file IDs from app.py."""
    try:
        with open("app.py", "r") as f:
            content = f.read()
        
        # Extract the drive_file_ids dictionary
        match = re.search(r"drive_file_ids = \{([^}]+)\}", content, re.DOTALL)
        if not match:
            return None
        
        drive_ids = {}
        dict_content = match.group(1)
        
        # Extract each file ID
        for model_file in MODEL_FILES:
            id_match = re.search(fr"'{model_file}':\s*'([^']+)'", dict_content)
            if id_match:
                drive_ids[model_file] = id_match.group(1)
            else:
                drive_ids[model_file] = None
        
        return drive_ids
    except Exception as e:
        print(f"Error reading app.py: {e}")
        return None

def check_drive_accessibility(file_id):
    """Check if a Google Drive file is accessible."""
    if not file_id or file_id == "YOUR_VGG16_FILE_ID" or file_id == "YOUR_RESNET50_FILE_ID" or file_id == "YOUR_INCEPTION_FILE_ID":
        return False
    
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except:
        return False

def main():
    print("=" * 60)
    print("EcoSortAI - Model Verification Tool")
    print("=" * 60)
    print("")
    
    # Check for local model files
    missing_models = check_local_models()
    
    if not missing_models:
        print("✅ All required models are available locally.")
        print("   Your application is ready to run with local models.")
        return
    
    print(f"⚠️ {len(missing_models)} model(s) are missing locally:")
    for model in missing_models:
        print(f"   - {model}")
    
    # Check Google Drive configuration
    print("\nChecking Google Drive configuration...")
    drive_ids = extract_drive_ids_from_app_py()
    
    if not drive_ids:
        print("❌ Could not find Google Drive configuration in app.py.")
        print("   Please run setup_drive_models.py to configure Google Drive integration.")
        return
    
    # Check each missing model's Drive accessibility
    drive_accessible = 0
    for model in missing_models:
        file_id = drive_ids.get(model)
        if check_drive_accessibility(file_id):
            print(f"✅ {model} is configured correctly on Google Drive.")
            drive_accessible += 1
        else:
            print(f"❌ {model} is not accessible on Google Drive. Check your sharing settings.")
    
    # Summary
    print("\n" + "=" * 60)
    if drive_accessible == len(missing_models):
        print("✅ VERIFICATION SUCCESSFUL")
        print("   All missing models are properly configured on Google Drive.")
        print("   Your application will download these models when needed.")
    else:
        print("❌ VERIFICATION FAILED")
        print(f"   {len(missing_models) - drive_accessible} model(s) are not properly configured.")
        print("   Please run setup_drive_models.py again with correct sharing URLs.")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
