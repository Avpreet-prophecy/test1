with DAG():
    pipeline_1__customer_spend_rank = Task(
        task_id = "pipeline_1__customer_spend_rank", 
        component = "Model", 
        modelName = "pipeline_1__customer_spend_rank"
    )
