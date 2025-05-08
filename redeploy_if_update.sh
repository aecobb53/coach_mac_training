git fetch origin
# git diff origin/main --name-only --exit-code
# git diff origin/main

NEEDS_UPDATE=$(git diff origin/main --name-only --exit-code)
LOGFILE="redeploy_log.log"

echo '' >> $LOGFILE
date >> $LOGFILE
echo $NEEDS_UPDATE >> $LOGFILE

if [[ $NEEDS_UPDATE ]]; then
    echo "There are changes in the main branch. Redeploying..." >> $LOGFILE
    ./update.sh
    echo "Updated" >> $LOGFILE
    ./restart.sh
    echo "Restarted" >> $LOGFILE
else
    echo "No changes in the main branch. No redeploy needed." >> $LOGFILE
fi
