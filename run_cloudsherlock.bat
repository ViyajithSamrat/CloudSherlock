@echo off
cd /d C:\Users\Asus\CloudSherlock
call venv\Scripts\activate.bat
python detect_anomalies.py
python generate_report.py
