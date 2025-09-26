Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    rides = Task(
        task_id = "rides", 
        component = "Dataset", 
        table = {"name" : "rides", "sourceType" : "Table", "sourceName" : "avpreet_random_prophecy_io_team.dummy", "alias" : ""}
    )
