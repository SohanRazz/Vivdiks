if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/SohanRazz/bulk.git /bulk
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /bulk
fi
cd /bulk
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
