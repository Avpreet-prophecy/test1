with DAG():
    uber_data = Task(
        task_id = "uber_data", 
        component = "Dataset", 
        table = {"name" : "uber_data", "sourceType" : "Table", "sourceName" : "avpreet_random_prophecy_io_team.dummy"}
    )
    pipeline_1__customer_tickets_and_spend_rank = Task(
        task_id = "pipeline_1__customer_tickets_and_spend_rank", 
        component = "Model", 
        modelName = "pipeline_1__customer_tickets_and_spend_rank"
    )
