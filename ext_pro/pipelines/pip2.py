with DAG():
    pip2__employee_annual_salary = Task(
        task_id = "pip2__employee_annual_salary", 
        component = "Model", 
        modelName = "pip2__employee_annual_salary"
    )
