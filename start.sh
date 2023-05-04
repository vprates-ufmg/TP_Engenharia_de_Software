#!/bin/bash

if [ "$1" == "--production" ]; then
  cd backend || exit
  python3 -m uvicorn main:app
  cd ..

  cd frontend || exit
  npm start
else
  cd backend || exit
  python3 main.py &
  cd ..

  cd frontend || exit
  npm start
fi