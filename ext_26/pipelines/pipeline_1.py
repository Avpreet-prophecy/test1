with DAG():
    pipeline_1__rides_aggregation_ordered = Task(
        task_id = "pipeline_1__rides_aggregation_ordered", 
        component = "Model", 
        modelName = "pipeline_1__rides_aggregation_ordered"
    )
