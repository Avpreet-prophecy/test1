Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    avDest1 = Task(
        task_id = "avDest1", 
        component = "Dataset", 
        table = {"name" : "avDest1", "sourceType" : "Source", "sourceName" : "prophecy_databricks_qa.avpreetTables", "alias" : ""}
    )
