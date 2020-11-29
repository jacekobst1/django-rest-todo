**Execute below commands to begin:**

    python3 manage.py migrate
    python3 manage.py runserver

<br>
<br>
<br>

**Documentation is available under _/docs_ URL. Available endpoints:**

    - GET /todo-lists/
    - POST /todo-lists/     [title]
    - GET /todo-lists/1
    - PUT /todo-lists/1     [title]
    - DELETE /todo-lists/1
    
    - GET /todo-items/
    - POST /todo-items/      [list_id, name, done_at]
    - GET /todo-items/1
    - PATCH /todo-items/1    [name, done_at]
    - DELETE /todo-items/1
