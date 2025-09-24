with DAG():
    xlxs_file = Task(
        task_id = "xlxs_file", 
        component = "Dataset", 
        table = {"name" : "xlxs_file", "sourceType" : "Table", "sourceName" : "avpreet_random_prophecy_io_team.dummy"}
    )
    support_tickets = Task(
        task_id = "support_tickets", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "support_tickets", "sourceName" : "avpreet_random_prophecy_io_team.dummy", "sourceType" : "Table"}
    )
    rides = Task(
        task_id = "rides", 
        component = "Dataset", 
        table = {"name" : "rides", "sourceType" : "Source", "sourceName" : "avpreet_random_prophecy_io_team.dummy", "alias" : ""}
    )
    pip2__final = Task(task_id = "pip2__final", component = "Model", modelName = "pip2__final")
