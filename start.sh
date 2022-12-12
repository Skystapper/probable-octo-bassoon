echo "Cloning Repo...."
git clone https://github.com/Skystapper/probable-octo-bassoon /probable-octo-bassoon
cd /probable-octo-bassoon
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
