LATEST_VERSION=$(shell curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)
GECKODRIVE_URL=$(shell curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | python -c "import sys, json; print(next(item['browser_download_url'] for item in json.load(sys.stdin)['assets'] if 'linux64' in item.get('browser_download_url', '')))")
INSTALL_DIR="/usr/local/bin"

install:
	wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(LATEST_VERSION)/chromedriver_linux64.zip
	sudo unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/;
	sudo chmod 755 /usr/local/bin/chromedriver
	curl -s -L $(GECKODRIVE_URL) | tar -xz
	chmod +x geckodriver
	sudo mv geckodriver $(INSTALL_DIR)
	pip install --upgrade pip
	pip install --upgrade setuptools
	pip install -r requirements.txt
