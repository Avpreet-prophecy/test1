Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    pip1__Reformat_1 = Task(task_id = "pip1__Reformat_1", component = "Model", modelName = "pip1__Reformat_1")
    OrchestrationTarget_1 = Task(
        task_id = "OrchestrationTarget_1", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = {"kind" : "sftp", "type" : "connector", "properties" : {}}, 
        properties = {}, 
        format = {
          "properties": {
            "allowLazyQuotes": False, 
            "allowEmptyColumnNames": True, 
            "separator": ",", 
            "nullValue": "", 
            "encoding": "UTF-8", 
            "header": True
          }, 
          "kind": "csv", 
          "category": "file"
        }, 
        isNew = True
    )
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "OnedriveSource", 
        connector = Connection(kind = "onedrive"), 
        isNew = True, 
        format = CSVFormat(
          allowLazyQuotes = False, 
          allowEmptyColumnNames = True, 
          separator = ",", 
          nullValue = "", 
          encoding = "UTF-8", 
          header = True
        )
    )
    Table_1 = Task(task_id = "Table_1", component = "Dataset", writeOptions = {"writeMode" : "overwrite"})
