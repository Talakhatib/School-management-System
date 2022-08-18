all_test_fixtures = */fixtures/*.test.json
python = python3
pip = pip3

backend-server-start:
	$(python) -u manage.py runserver 0.0.0.0:8000
	tail -f django-server.log 
setup:
	$(python) manage.py makemigrations && $(python) manage.py migrate

testing:
	$(python) manage.py loaddata $(all_test_fixtures)

backend-db-refresh:
	rm -rf db.sqlite3 2>/dev/null
	find . -type d -name migrations | xargs -I {} find {} -type f -name "*.py" | grep -v '__init__.py' | xargs rm -f 2>/dev/null
	make backend-server-stop
	make setup
