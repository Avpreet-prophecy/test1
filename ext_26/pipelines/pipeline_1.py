with DAG():
    uber_data = Task(
        task_id = "uber_data", 
        component = "Dataset", 
        table = {"name" : "uber_data", "sourceType" : "Table", "sourceName" : "avpreet_random_prophecy_io_team.dummy"}
    )
    pipeline_1__customer_spend_rank = Task(
        task_id = "pipeline_1__customer_spend_rank", 
        component = "Model", 
        modelName = "pipeline_1__customer_spend_rank"
    )
    pipeline_1__total_tickets_per_customer = Task(
        task_id = "pipeline_1__total_tickets_per_customer", 
        component = "Model", 
        modelName = "pipeline_1__total_tickets_per_customer"
    )
