 .PHONY: generate eda test

 generate:
 	python src/generate.py --n 500 --out data/synthetic_customers_v1.csv

 eda:
 	python src/eda.py --input data/synthetic_customers_v1.csv --outdir reports/

 test:
	pytest -q
