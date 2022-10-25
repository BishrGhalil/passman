all:

run:
	python3 passman.py

install:
	pip3 install -r requirements.txt
	python3 setup.py install_exec install --optimize=1 --record=install_log.log

clean:
	find passman -depth -name __pycache__ -type d -exec rm -r -- {} \;
	find -depth -name "*.log" -type f -exec rm -rf -- {} \;
	find -depth -name "*.pyc" -type f -exec rm -rf -- {} \;
	rm -rf passman.egg-info dist build

.PHONE: clean
