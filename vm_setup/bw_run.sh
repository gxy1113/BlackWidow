screen -ls | grep pts | cut -d. -f1 | awk '{print $1}' | xargs kill
killall screen
cd /home/vmuser/wk_dir/BlackWidow
rm -rf logs/*
cp -r data/ data-copy/
rm -rf data/*
mkdir data/
git stash
GIT_SSH_COMMAND="ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no" git pull
screen -dmS python3 crawl.py --url $1 --crawler
sleep 15
screen -ls