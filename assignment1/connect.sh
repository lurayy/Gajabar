if [ -z $1 ]
then
    echo  "Use connect.sh [bandit_level] [passowrd] to login"
    exit
fi
sshpass -p $2 ssh -o StrictHostKeyChecking=no -p 2220 "bandit"$1"@bandit.labs.overthewire.org"
