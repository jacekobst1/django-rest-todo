**Execute below commands to begin:**

    python3 manage.py migrate
    python3 manage.py runserver

<br>
<br>
<br>

**Available endpoints:**

    - GET /todo-lists/
    - POST /todo-lists/     [_title_]
    - GET /todo-lists/1
    - PUT /todo-lists/1     [_title_]
    - DELETE /todo-lists/1
    
    - GET /todo-items/
    - POST /todo-items/      [_list_id_, _name_, _done_at_]
    - GET /todo-items/1
    - PATCH /todo-items/1    [_name_, _done_at_]
    - DELETE /todo-items/1
