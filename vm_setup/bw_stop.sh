echo "Hostname of the BW VM:"
read bwID
echo "Password of the BW VM: "
read password

sshpass -p $password ssh -o StrictHostKeyChecking=no -t vmuser@$bwID.csl.toronto.edu "screen -ls | grep pts | cut -d. -f1 | awk '{print $1}' | xargs kill"
sshpass -p $password ssh -o StrictHostKeyChecking=no -t vmuser@$bwID.csl.toronto.edu "screen -ls"