import uvicorn
import os
from crontab import CronTab

def start():
    uvicorn.run("backend.app.app:app", host="0.0.0.0", port=8000, reload=True)

def job():
    os.system("""curl --location --request GET 'http://localhost:8000/covid/list?notify=false'""")

    command = """curl --location --request GET 'http://localhost:8000/covid/list?notify=true'"""

    cron = CronTab(user=True)
    job  = cron.new(command=command)
    job.minute.every(5)
    job.hour.during(14, 18)
    cron.write()

    os.system("crond")
    os.system("crontab -l")
    
