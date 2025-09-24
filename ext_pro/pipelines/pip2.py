Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    xlxs_file = Task(
        task_id = "xlxs_file", 
        component = "Dataset", 
        table = {
          "name": "xlxs_file", 
          "sourceType": "Source", 
          "sourceName": "avpreet_random_prophecy_io_team.dummy", 
          "alias": ""
        }
    )
