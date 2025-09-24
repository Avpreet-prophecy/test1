with DAG():
    pip2__category_avg_salary = Task(
        task_id = "pip2__category_avg_salary", 
        component = "Model", 
        modelName = "pip2__category_avg_salary"
    )
