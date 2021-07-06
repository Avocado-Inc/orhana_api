#!/bin/bash

source env/bin/activate


uvicorn orhana_api:app --reload --log-level debug
