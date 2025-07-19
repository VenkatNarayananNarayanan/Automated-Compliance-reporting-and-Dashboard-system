@echo off

REM Set Alteryx path
set "ALTERYX_PATH=C:\Program Files\Alteryx\bin\AlteryxEngineCmd.exe"

REM Set workflow path
set "WORKFLOW_PATH=C:\Users\VENKAT\Desktop\Compliance_project\ETL_compliance_rule.yxmd"

REM Set log file path
set "LOG_FILE=C:\Users\VENKAT\Desktop\Compliance_project\run_log.txt"

REM Run the workflow
"%ALTERYX_PATH%" "%WORKFLOW_PATH%"

REM Log the time
echo [%DATE% %TIME%] Automatic Compliance job executed successfully. >> "%LOG_FILE%"
