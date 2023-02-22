echo "Hostname of the BW VM:"
read bwID
echo "Password of the BW VM: "
read password

sshpass -p $password ssh -o StrictHostKeyChecking=no -t vmuser@$bwID.csl.toronto.edu "rm -rf wk_dir/*; mkdir wk_dir; cd wk_dir; git clone https://github.com/gxy1113/BlackWidow.git"