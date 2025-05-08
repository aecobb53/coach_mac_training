git fetch origin
# git diff origin/main --name-only --exit-code
# git diff origin/main

NEEDS_UPDATE=$(git diff origin/main --name-only --exit-code)

if [[ $NEEDS_UPDATE ]]; then
    echo "There are changes in the main branch. Redeploying..."
    # git pull origin main
    # Add your redeploy command here, e.g.,:
    # ./deploy.sh
else
    echo "No changes in the main branch. No redeploy needed."
fi
