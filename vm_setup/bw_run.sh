screen -ls | grep pts | cut -d. -f1 | awk '{print $1}' | xargs kill
killall screen
cd /home/vmuser/wk_dir/BlackWidow
rm -rf logs/*
mkdir logs/
cp -r data/ data-copy/
rm -rf data/*
mkdir data/
mkdir form_files/dynamic
git stash
GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" git pull
date +%s > start_time
screen -dmS pts-bw python3 crawl.py --url $1 --crawler
sleep 15
screen -ls
cat start_time