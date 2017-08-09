.PHONY: clean

deploy.zip: free_stuff_bot.py requirements.txt
	mkdir deploy/
	pip install -t deploy/ -r requirements.txt
	cp free_stuff_bot.py deploy/
	cd deploy/; zip -r ../deploy.zip *

clean:
	rm -rf deploy/
	rm -rf deploy.zip
