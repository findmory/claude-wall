# GitHub Pages Deployment Guide

Follow these steps to host your Image Wall on GitHub Pages:

## Step 1: Create a GitHub Repository

1. Go to https://github.com/new
2. Name your repository (e.g., "image-wall")
3. Keep it public (required for free GitHub Pages)
4. Don't initialize with README (we already have one)
5. Click "Create repository"

## Step 2: Initialize Git and Push

Open your terminal in the repository folder and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Image wall app"

# Add your GitHub repository as remote
# Replace YOUR-USERNAME and YOUR-REPO with your actual GitHub username and repo name
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on "Settings" tab
3. Scroll down to "Pages" in the left sidebar
4. Under "Source", select "Deploy from a branch"
5. Under "Branch", select "main" and "/ (root)"
6. Click "Save"

## Step 4: Wait for Deployment

- GitHub will build and deploy your site (takes 1-2 minutes)
- Your site will be available at: `https://YOUR-USERNAME.github.io/YOUR-REPO/`
- You'll see a green checkmark when it's ready

## Step 5: Add Your Images

1. Add your PNG files to the `images/` folder
2. **IMPORTANT**: Generate the image list file:

```bash
python3 generate-images-list.py
```

Or if you prefer Node.js:

```bash
node generate-images-list.js
```

3. Commit and push the changes:

```bash
git add images/ images.json
git commit -m "Add images"
git push
```

**Note**: You must run the generate script every time you add or remove images!

## Updating Your Site

Whenever you make changes:

```bash
git add .
git commit -m "Description of your changes"
git push
```

GitHub Pages will automatically rebuild and deploy your site!

## Troubleshooting

**Images not loading?**
- Make sure PNG files are in the `images/` folder
- Check browser console (F12) for errors
- Verify the images folder is being served correctly

**Site not loading?**
- Wait 2-3 minutes after enabling Pages
- Check the Actions tab on GitHub for build status
- Make sure the repository is public

**Need a custom domain?**
- In Settings → Pages, add your custom domain
- Configure DNS settings with your domain provider
