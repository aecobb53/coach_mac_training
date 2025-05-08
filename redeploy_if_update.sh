LOGFILE_HOME=$(pwd)
LOGFILE="${LOGFILE_HOME}/redeploy_log_coach_mac_training.log"
echo '' >> $LOGFILE
date >> $LOGFILE

# ls >> $LOGFILE

cd git/coach_mac_training

# ls >> $LOGFILE

git fetch origin

NEEDS_UPDATE=$(git diff origin/main --name-only --exit-code)
echo $NEEDS_UPDATE >> $LOGFILE

if [[ -n $NEEDS_UPDATE ]]; then
    echo "There are changes in the main branch. Redeploying..." >> $LOGFILE
    ./update.sh
    echo "Updated" >> $LOGFILE
    ./restart.sh
    echo "Restarted" >> $LOGFILE
else
    echo "No changes in the main branch. No redeploy needed." >> $LOGFILE
fi
