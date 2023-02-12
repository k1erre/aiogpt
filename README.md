# Homepage
https://t.me/gpt_unlimited_bot
# Installation
1. Clone project
2. Create new virtual enviroment in project folder ```python3 -m venv venv```
3. Activate virtual enviroment ```source venv/bin/activate```
4. Run ```pip install -r requirements.txt```
5. Create .env file in project folder for storing api keys (your telegram bot token & openai key) ```touch .env```
6. Edit .env using .env.example as template (there are fictional keys, use your own)
# Usage
Run ```python3 bot.py``` or ```nohup python3 bot.py &``` to run in background.
To deactivate venv, use ```deactivate``` command. To kill process running in background, use ```pkill -f bot.py```
