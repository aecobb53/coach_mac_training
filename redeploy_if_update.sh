#!/bin/bash

LOGFILE="${LOGFILE_HOME}/redeploy_log_coach_mac_training.log"

echo $LOGFILE

echo '' >> $LOGFILE
echo '' >> $LOGFILE
date >> $LOGFILE

cd git/coach_mac_training

# Get current commit hash
local_hash=$(git rev-parse HEAD)

# Fetch latest changes from remote
git fetch origin > /dev/null 2>&1

# Get remote commit hash
remote_hash=$(git rev-parse origin/$(git branch --show-current))

# Compare commit hashes
if [ "$local_hash" != "$remote_hash" ]; then
  echo "Remote changes detected. Pulling and redeploying..." >> $LOGFILE
  git pull origin > /dev/null 2>&1
  # Add your redeployment commands here
  echo "Redeployment complete." >> $LOGFILE
else
  echo "No remote changes detected." >> $LOGFILE
fi


# LOGFILE_HOME=$(pwd)
# LOGFILE="${LOGFILE_HOME}/redeploy_log_coach_mac_training.log"
# echo '' >> $LOGFILE
# date >> $LOGFILE

# # ls >> $LOGFILE

# cd git/coach_mac_training

# # ls >> $LOGFILE

# git fetch origin

# NEEDS_UPDATE=$(git diff origin/main --name-only --exit-code)
# echo $NEEDS_UPDATE >> $LOGFILE

# if [[ -n $NEEDS_UPDATE ]]; then
#     echo "There are changes in the main branch. Redeploying..." >> $LOGFILE
#     ./update.sh
#     echo "Updated" >> $LOGFILE
#     ./restart.sh
#     echo "Restarted" >> $LOGFILE
# else
#     echo "No changes in the main branch. No redeploy needed." >> $LOGFILE
# fi
