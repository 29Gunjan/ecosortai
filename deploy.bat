@echo off
echo ==========================================
echo EcoSortAI - Automatic Deployment Script
echo ==========================================

echo.
echo This script will help you automatically deploy your 
echo EcoSortAI application to Render.com's free tier.
echo.

echo Step 1: Checking requirements...
where git >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Git is not installed or not in PATH. Please install Git and try again.
    goto :end
)

echo Git is installed. Good!
echo.

echo Step 2: Ensuring directories exist...
mkdir static\uploads 2>nul
echo Created upload directory.
echo.

echo Step 3: Initializing git repository...
git init
if %ERRORLEVEL% neq 0 (
    echo Failed to initialize git repository.
    goto :end
)
echo.

echo Step 4: Adding files to git...
git add .
if %ERRORLEVEL% neq 0 (
    echo Failed to add files to git.
    goto :end
)
echo.

echo Step 5: Committing changes...
git commit -m "Prepare for deployment"
if %ERRORLEVEL% neq 0 (
    echo Failed to commit changes.
    goto :end
)
echo.

echo Step 6: Deployment instructions
echo.
echo Your application is now ready for deployment to Render.com!
echo.
echo Please follow these steps:
echo 1. Create an account on Render.com (no credit card required)
echo 2. Go to https://dashboard.render.com/select-repo
echo 3. Connect your GitHub/GitLab account
echo 4. Select the repository you pushed this code to
echo 5. Render will automatically detect the render.yaml configuration
echo 6. Click "Apply"
echo.
echo Your application will be deployed automatically!
echo The deployment process takes about 5-10 minutes.
echo.
echo Once deployed, you can access your application at:
echo https://ecosortai.onrender.com
echo.

:end
pause
