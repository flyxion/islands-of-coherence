.PHONY: all pdf sim lab site clean

all: pdf sim site

pdf:
	cd src/latex && make

sim:
	cd src/python && python run_all_simulations.py

lab:
	docker-compose up jupyter

site:
	cp -r output/* docs/output/
	cp src/python/notebooks/*.pdf docs/output/ 2>/dev/null || true

clean:
	cd src/latex && make clean
	rm -rf output/*
