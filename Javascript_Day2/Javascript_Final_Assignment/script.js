document.getElementById('addBtn').addEventListener('click', function() {
    var taskInput = document.getElementById('taskInput');
    var newTask = taskInput.value.trim();

    if (newTask !== "") {
        var li = document.createElement('li');
        
        
        var completeCheckbox = document.createElement('input');
        completeCheckbox.type = 'checkbox';
        completeCheckbox.addEventListener('change', function() {
            if (this.checked) {
                li.style.textDecoration = 'line-through';
            } else {
                li.style.textDecoration = 'none';
            }
        });

        var taskText = document.createTextNode(newTask);

        var deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.onclick = function() {
            li.remove();
        };

        li.appendChild(completeCheckbox);
        li.appendChild(taskText);
        li.appendChild(deleteBtn);

        document.getElementById('taskList').appendChild(li);
        taskInput.value = '';
    } else {
        alert("Please enter a task!");
    }
});
