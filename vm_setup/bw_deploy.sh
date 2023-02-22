echo "Hostname of the BW VM:"
read bwID
echo "Password of the BW VM: "
read password
echo "Target Web application URL: "
read webapp
sshpass -p $password scp -o StrictHostKeyChecking=no bw_run.sh vmuser@$bwID.csl.toronto.edu:/home/vmuser/wk_dir/
sshpass -p $password ssh -o StrictHostKeyChecking=no -t vmuser@$bwID.csl.toronto.edu "/home/vmuser/wk_dir/bw_run.sh $webapp"