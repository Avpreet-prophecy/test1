with DAG():
    pip2__category_avg_salary = Task(
        task_id = "pip2__category_avg_salary", 
        component = "Model", 
        modelName = "pip2__category_avg_salary"
    )
    support_tickets = Task(
        task_id = "support_tickets", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "support_tickets", "sourceName" : "avpreet_random_prophecy_io_team.dummy", "sourceType" : "Table"}
    )
    uber_data = Task(
        task_id = "uber_data", 
        component = "Dataset", 
        table = {
          "name": "uber_data", 
          "sourceType": "Source", 
          "sourceName": "avpreet_random_prophecy_io_team.dummy", 
          "alias": ""
        }
    )
    rides = Task(
        task_id = "rides", 
        component = "Dataset", 
        table = {"name" : "rides", "sourceType" : "Source", "sourceName" : "avpreet_random_prophecy_io_team.dummy", "alias" : ""}
    )
