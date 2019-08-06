::切換至程式目錄
cd C:\Users\johnson.l\Desktop\py_se
::設定要執行次數, count從1開始, 每次遞增1, 終止條件為5
for /L %%i in (1 1 5) do python ph_offline_login.py count: %%i
pause