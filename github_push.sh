#!/bin/bash

# User credentials
GITHUB_USERNAME="EckTn"
GITHUB_REPO_NAME="Image_Recognition_Flask"
GIT_USER_NAME="EckTn"
GIT_USER_EMAIL="ecktan.065@gmail.com"

# Configures Git user (only needs to be done once)
git config --global user.name "$GIT_USER_NAME"
git config --global user.email "$GIT_USER_EMAIL"

# Initializes a new Git repos (to be skipped if already initialized)
git init

# Adds all project files to the Git repository
git add .

# Commits project files
git commit -m "Automated commit"

# Checks if the remote repository is already added
if ! git remote | grep -q "origin"; then
  git remote add origin "https://github.com/$GITHUB_USERNAME/$GITHUB_REPO_NAME.git"
fi

# Pushes the project files to the GitHub
git push -u origin master

echo "Project pushed to GitHub successfully!"
