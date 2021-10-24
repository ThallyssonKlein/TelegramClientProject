#!/bin/bash
pipenv run python init_db.py
pipenv run python init_sample_params.py
pipenv run python init_chats.py