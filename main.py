import json

def read_file(file_name : str) -> tuple:
    try:
        # read from the json file and retrieve task_data
        with open(file_name, mode='r', encoding='utf-8') as file:
            task_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # structure an empty task data structure
        task_data = {
            'next_id' : 1,
            'tasks' : [],
        }
        # dump the empty task data into the newly created json file
        with open(file_name, mode='w', encoding='utf-8') as file:
            json.dump(task_data, file, indent=4)

    next_id = task_data['next_id']
    tasks = task_data['tasks']

    return tasks, next_id

def add_task(
        tasks : list, 
        next_id : int, 
        title : str
) -> tuple:
    new_task = {
        "id" : next_id,
        "title" : title,
        "completed" : False
    }

    tasks.append(new_task)
    print(f'Task created successfully! ID: {next_id}')
    next_id += 1

    return tasks, next_id

def view_tasks(tasks : list):
    print("YOUR TASKS")

    for task in tasks:
        print(f"[{task['id']}] [{'x' if task['completed'] else ' '}] {task['title']}")

def edit_task(
        tasks : list, 
        edit_id : int,
        new_title : str
):
    for index, task in enumerate(tasks):
        if task['id'] == edit_id:
            tasks[index]['title'] = new_title
            break

    print(f'Task {edit_id} edited successfully!')

    return tasks

def complete_task(
        tasks : list,
        completed_id : int,
):
    for index, task in enumerate(tasks):
        if task['id'] == completed_id:
            # if tasks[index]['completed'] == True:
            #     print(f'Task {task['id']} is already completed.')
            # else:
            tasks[index]['completed'] = True
            break

    print(f'Task {completed_id} marked as completed!')

    return tasks

def delete_task(
        tasks : list,
        delete_id : int,
):
    for task in tasks:
        if task['id'] == delete_id:
            tasks.remove(task)
            break
    
    return tasks

def write_file(
        file_name : str, 
        tasks : list, 
        next_id : int,
):
    task_data = {
        'next_id' : next_id,
        'tasks' : tasks,
    }
    # write the updated tasks back to the file
    with open(file_name, mode='w', encoding='utf-8') as file:
        json.dump(task_data, file, indent=4)

def display_task_manager():
    print('\n======== TASK MANAGER ========')
    print('1. Add Task\n2. View Tasks\n3. Edit Task\n4. Complete Task')
    print('5. Delete Task\n6. Exit')
    print('==============================')

def main():
    file_name = 'tasks.json'
    tasks, next_id = read_file(file_name)
    user_input = 0

    display_task_manager()

    while user_input != 6:
        try:
            user_input = int(input('\nEnter your choice: '))
            if user_input < 1 or user_input > 6:
                print('Please enter a valid choice ranging from 1 to 6')
                continue
        except ValueError:
            print('Please enter a number representing the choice (ex. 1)')
            continue
            
        if user_input == 1:
            description = ''

            while not description:
                description = input('Task description: ').strip()
                if not description:
                    print('Please enter a valid description.')

            tasks, next_id = add_task(tasks=tasks, next_id=next_id, 
                                      title=description)

        elif user_input == 2:
            view_tasks(tasks=tasks)

        # if the user wants to modify or delete an existing task
        elif user_input in [3, 4, 5]:
            # make sure a task exists
            if not tasks:
                print('There are no tasks to modify or delete.')
                continue

            task_id = -1
            # attempt to retrieve the requested task
            while task_id < 0:
                try:
                    task_id = int(input('Enter task ID: '))
                    existing_ids = [task['id'] for task in tasks]
                    if task_id not in existing_ids:
                        # print('Please enter an existing task id.')
                        raise ValueError
                        # print('Existing Tasks')
                        # view_tasks(tasks=tasks)
                        # task_id = -1
                except ValueError:
                    print('Please enter an existing task id\n')
                    view_tasks(tasks=tasks)
                    task_id = -1

            # if the user wants to edit a task
            if user_input == 3:
                new_description = ''

                while not new_description:
                    new_description = input('Enter new description: ').strip()
                    if not new_description:
                        print('Please enter a valid description.')

                tasks = edit_task(tasks, task_id, new_description)
                continue

            incomplete_ids = [task['id'] for task in tasks if not task['completed']]

            # if the user wants to complete the task
            if user_input == 4:
                if task_id not in incomplete_ids:
                    print(f'Task {task_id} is already complete.')
                    continue
                tasks = complete_task(tasks, task_id)

            # if the user wants to delete the task
            elif user_input == 5:
                tasks = delete_task(tasks, task_id)

                if task_id in incomplete_ids:
                    incomplete_ids.remove(task_id)

    # user has exited
    print('Goodbye!')
    write_file(file_name, tasks, next_id)

if __name__ == '__main__':
    main()