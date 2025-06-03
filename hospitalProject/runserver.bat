@echo off
cd /d C:\Users\Surya\OneDrive\Desktop\SRI-SHANMUGAM-LAB\hospitalProject
call ..\.venv\Scripts\activate
timeout /t 2 >nul
start http://127.0.0.1:8000
python manage.py runserver
pause
