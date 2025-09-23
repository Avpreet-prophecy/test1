Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    pip1__Reformat_1 = Task(task_id = "pip1__Reformat_1", component = "Model", modelName = "pip1__Reformat_1")
