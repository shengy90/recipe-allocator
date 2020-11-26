echo -e "\n Installing virtual environment.. ⏳"
pyenv virtualenv 3.7.6 recipe-allocator

pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

pyenv local recipe-allocator
echo -e "\n All done! 👍"