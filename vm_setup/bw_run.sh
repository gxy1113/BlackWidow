screen -ls | grep pts | cut -d. -f1 | awk '{print $1}' | xargs kill
killall screen
cd /home/vmuser/wk_dir/BlackWidow
rm -rf logs/*
git stash
GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" git pull