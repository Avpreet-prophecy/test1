Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    dummy = Task(
        task_id = "dummy", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "dummy", "sourceType" : "Seed", "alias" : ""}
    )
    pip1__find_duplicates_in_m1 = Task(
        task_id = "pip1__find_duplicates_in_m1", 
        component = "Model", 
        modelName = "pip1__find_duplicates_in_m1"
    )
    pip1__parse_person_details = Task(
        task_id = "pip1__parse_person_details", 
        component = "Model", 
        modelName = "pip1__parse_person_details"
    )
    model1_1 = Task(task_id = "model1_1", component = "Model", modelName = "model1")
    dummy.out >> pip1__find_duplicates_in_m1.in_0
