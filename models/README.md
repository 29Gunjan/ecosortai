# EcoSortAI Model Files

This directory contains the trained machine learning models used by EcoSortAI for waste classification.

## Required Models

Three models are required for the application to function properly:

### VGG16 Model
- Filename: `vgg16_waste_classification_tf.h5`
- Size: ~85MB

### ResNet50 Model
- Filename: `waste_classification22_model.h5` 
- Size: ~97MB

### InceptionV3 Model
- Filename: `inceptionv3_waste_classification_tf.h5`
- Size: ~90MB

## Google Drive Hosting Instructions

For deployment on platforms with storage limitations, we recommend hosting the models on Google Drive:

1. **Upload models to Google Drive**:
   - Create a folder called "EcoSortAI-Models"
   - Upload all three model files to this folder

2. **Make models accessible**:
   - Right-click each model file → Share → "Anyone with the link" → "Viewer"
   - Copy the sharing link for each model

3. **Configure your application**:
   - Run the setup script: `python setup_drive_models.py`
   - Paste the sharing URLs when prompted
   - The script will automatically update your application

4. **Deploy your application**:
   - Follow the deployment instructions in DEPLOYMENT_GUIDE.md
   - Your application will download models from Google Drive when needed

## Local Development

For local development, you can either:

1. **Place model files directly in this directory**:
   - The application will use local files if available

2. **Configure Google Drive integration**:
   - Run `python setup_drive_models.py` as described above
   - Models will be downloaded from Google Drive on first run

## Verification

To verify that your models are correctly configured, run:

```python
python check_models.py
```

This script will check if models are available locally or can be downloaded from Google Drive.

## How to Set Up the Models

### Option 1: Run the Setup Script

The easiest way to set up the models is to use the provided setup script:

```
python setup_models.py
```

This script will guide you through the process of obtaining the models through:
- Downloading from a remote server
- Copying from a local directory
- Extracting from a ZIP file
- Creating dummy models for testing

### Option 2: Manual Setup

If you prefer to set up the models manually:

1. Obtain the model files from the official source
2. Place them directly in this directory
3. Verify the models have the exact filenames listed above

## Model Sources

If you're a project contributor, you can obtain the official models from:

1. [Project Google Drive](https://drive.google.com/drive/folders/your-folder-id)
2. [Project GitHub Releases](https://github.com/yourusername/ecosortai/releases)

## Creating Your Own Models

If you're interested in training your own models, refer to the training scripts in the 
`training` directory. The models need to:

1. Accept 224x224x3 RGB images as input
2. Output a binary classification (recyclable vs organic)
3. Use the same architecture as the original models
4. Be saved in the TensorFlow SavedModel format

## Troubleshooting

If you encounter any issues with the models:

1. Verify file integrity by comparing MD5 checksums
2. Ensure TensorFlow version compatibility (TensorFlow 2.8+ recommended)
3. Check that you have sufficient disk space
4. Try running with the `--debug` flag for more information
