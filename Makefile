.PHONY: run

run:
	python3 -m uvicorn src.main:app --reload --port 8000

# 设置默认目标为 run
.DEFAULT_GOAL := run

