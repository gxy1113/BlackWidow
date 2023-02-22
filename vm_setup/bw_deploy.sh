echo "Hostname of the AuthZee VM:"
read bwID
echo "Target Web application: "
read webapp
sshpass -p "vmuser" scp -o StrictHostKeyChecking=no bw_run.sh vmuser@$bwID.csl.toronto.edu:/home/vmuser/wk_dir/
sshpass -p "vmuser" ssh -o StrictHostKeyChecking=no -t vmuser@$bwID.csl.toronto.edu "/home/vmuser/wk_dir/bw_run.sh $webapp"