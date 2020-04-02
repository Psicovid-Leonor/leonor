install:
	npm install

deploy:
	./node_modules/.bin/sls deploy

test-request-assistance:
	./node_modules/.bin/sls invoke local -f request-assistance --path ./fixtures/request-assistance.json
