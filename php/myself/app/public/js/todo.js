let baseUrl = 'http://localhost/Latihan/OOP-php/myself'
$('#addTodo').submit(function (e) {
    e.preventDefault();
    let form = $(this);

    let actionUrl = form.attr(`${baseUrl}/todo.php`);

    $.ajax({
        type: "POST",
        url: actionUrl,
        data: form.serialize(), // serializes the form's elements.
        success: async function () {
            let html = $((await fetch(`${baseUrl}/todo.php`).then(e => e.text()).then(e => e)));
            $('#container-todos').html($('#container-todos',html).html());
        }
    });
});

$("#container-todos").on('click',".deleteTodo", function() {
    //Code here
    let todoId = $(this).data('todoId');
    $.ajax({
        type: "POST",
        url: `${baseUrl}/todo.php`,
        data: {todoId,action:'delete'},
        success: async function (data) {
            let html = $((await fetch(`${baseUrl}/todo.php`).then(e => e.text()).then(e => e)));
            $('#container-todos').html($('#container-todos',html).html())
        }
    });
});

$("#container-todos").on('click',".editTodo", function() {
    //Code here
    let todoId = $(this).data('todoId');
    // display input and save todo
    $($(`.changeTodo[data-todo-id=${todoId}]`)[0]).removeClass('d-none')
    $($(`.disableChangeTodo[data-todo-id=${todoId}]`)[0]).addClass('d-none')    
    $(this).addClass('d-none')
    $($(`.saveEdited[data-todo-id=${todoId}]`)[0]).removeClass('d-none')

    // display input date todo
    $($(`.dueDate[data-todo-id=${todoId}] > h6`)[0]).addClass('d-none')
    $($(`.dueDate[data-todo-id=${todoId}] > input`)[0]).removeClass('d-none')
    
    
});

$("#container-todos").on('click',".checklist", function() {
    //Code here
    let todoId = $(this).data('todoId');
    if($($(`.editTodo[data-todo-id=${todoId}]`)[0]).hasClass('d-none')){
        let status = $(`.checklist[data-todo-id='${todoId}'] > i`).data('status');
        if(status == 'active'){
            $(`.checklist[data-todo-id='${todoId}'] > i`).removeClass('fa-square-o').addClass('fa-check-square-o').data('status','complete')
    
        }else if(status == 'complete'){
            $(`.checklist[data-todo-id='${todoId}'] > i`).removeClass('fa-check-square-o').addClass('fa-square-o').data('status','active')
        }
    }

})

$("#container-todos").on('click',".saveEdited", function() {
    //Code here
    let todoId = $(this).data('todoId');
    let todo = $($(`.changeTodo[data-todo-id=${todoId}]`)[0]).val()
    let status = $(`.checklist[data-todo-id='${todoId}'] > i`).data('status');
    let dueDate = $($(`.dueDate[data-todo-id=${todoId}] > input`)[0]).val()
    // console.log(todo,status)
    $.ajax({
        type: "POST",
        url: `${baseUrl}/todo.php`,
        data: {todo,status,todoId,dueDate,action:'update'},
        success: async function (data) {
            // console.log(data);
            let html = $((await fetch(`${baseUrl}/todo.php`).then(e => e.text()).then(e => e)));
            $('#container-todos').html($('#container-todos',html).html())

        }
    });
});

// change filter 
$('#filter').on('change', function() {
    Object.values($('.checklist')).map(e => {
        let todoId = $(e).data('todoId')
        if(todoId){
            let status = $(`.checklist[data-todo-id='${todoId}'] > i`).data('status')
            if (status == this.value || this.value == 'all'){
                $(`#${todoId}`).removeClass('d-none');
            }else{
                $(`#${todoId}`).addClass('d-none');
            }
        }

    })
    this.value
});

// change sort
// $('#sort').on('change', function() {
//     if(this.value == 'due-date'){
//         Object.values($('.dueDate')).map(e => {

//         })
//     }
// })


$("#container-todos").on('click',".saveTodo", function() {
    //Code here
    let todoId = $(this).data('todoId');
    $.ajax({
        type: "POST",
        url: `${baseUrl}/todo.php`,
        data: {todoId,action:'delete'},
        success: async function (data) {
            let html = $((await fetch(`${baseUrl}/todo.php`).then(e => e.text()).then(e => e)));
            $('#container-todos').html($('#container-todos',html).html())
        }
    });
});
