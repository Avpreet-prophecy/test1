with DAG():
    pipeline_1__rides_with_fare = Task(
        task_id = "pipeline_1__rides_with_fare", 
        component = "Model", 
        modelName = "pipeline_1__rides_with_fare"
    )
