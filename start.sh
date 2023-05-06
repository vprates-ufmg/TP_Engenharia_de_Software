#!/bin/bash

if [ "$1" == "--production" ]; then
  cd backend || exit
  python3 -m uvicorn main:app
  cd ..

  cd frontend || exit
  npm start
else
  cd backend || exit
  python main.py &
  cd ..

  cd frontend/review-profs || exit
  npm start
fi