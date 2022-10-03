@foreach ($todos as $todo)
    <div class="row mx-1 px-5 pb-3 w-80 container-todo" id={{$todo['todo_id']}}>
        <div class="col mx-auto">
            {{-- item 1 --}}
            <div class="row px-3 align-items-center todo-item rounded">
                {{-- check list --}}
                <div class="col-auto m-1 p-0 d-flex align-items-center">
                    <h2 class="m-0 p-0 checklist" data-todo-id={{$todo['todo_id']}} >
                        @if ($todo['status'] === 'complete')
                            {{-- done --}}
                            <i class="fa fa-check-square-o text-primary btn m-0 p-0" data-toggle="tooltip"
                                data-placement="bottom" data-status='complete' title="Mark as complete" ></i>
                        @else
                            {{-- in progress --}}
                            <i class="fa fa-square-o text-primary btn m-0 p-0" data-toggle="tooltip"
                                data-placement="bottom" data-status='active' title="Mark as todo" ></i>
                        @endif
                    </h2>
                </div>    
                <div class="col px-1 m-1 d-flex align-items-center">
                    {{-- only view --}}
                    <input type="text"
                        class="form-control fw-light form-control-lg border-0 edit-todo-input bg-transparent rounded px-3 disableChangeTodo"
                        readonly value={{$todo['todo']}} title={{$todo['todo']}} data-todo-id={{$todo['todo_id']}} />
                    {{-- can input --}}
                    <input type="text"
                        class="form-control form-control-lg border-0 edit-todo-input rounded px-3 d-none changeTodo"
                        value={{$todo['todo']}} data-todo-id={{$todo['todo_id']}} />
                </div>

                
                {{-- info status has due date --}}
                <div class="col-auto m-1 p-0 px-3">
                    <div class="row">
                        <div class="col-auto d-flex align-items-center rounded bg-white border border-warning dueDate" data-time={{strtotime($todo['due_date'])}} data-todo-id={{$todo['todo_id']}} >
                            <i class="fa fa-hourglass-2 my-2 px-2 text-warning btn" data-toggle="tooltip" data-placement="bottom" title="" data-original-title="Due on date"></i>
                            <h6 class="text my-2 pr-2">{{ date("d-m-Y",strtotime($todo['due_date']))}}</h6>
                            <input type="date" name='dueDate' class="d-none my-2 pr-2" value={{$todo['due_date']}}>
                        </div>
                    </div>
                </div>

                {{-- actions --}}
                <div class="col-auto m-1 p-0 todo-actions">
                    <div class="row">
                        <div class="col d-flex justify-content-end">
                            <h5 class="m-0 p-0 px-2 editTodo" data-todo-id={{$todo['todo_id']}}>
                                <i class="fa fa-pencil text-info btn m-0 p-0" data-toggle="tooltip"
                                    data-placement="bottom" title="Edit todo"></i>
                            </h5>
                            <h5 class="m-0 p-0 px-2 d-none saveEdited" data-todo-id={{$todo['todo_id']}}>
                                <i class="fa fa-floppy-o text-info btn m-0 p-0" data-toggle="tooltip"
                                    data-placement="bottom" title="Save todo"></i>
                            </h5>
                            <h5 class="m-0 p-0 px-2 deleteTodo" data-todo-id={{$todo['todo_id']}}>
                                <i class="fa fa-trash-o text-danger btn m-0 p-0" data-toggle="tooltip"
                                    data-placement="bottom" title="Delete todo"></i>
                            </h5>
                        </div>
                    </div>
        
                    <div class="row todo-created-info">
                        <div class="col-auto d-flex align-items-center pr-2 createdDate" data-time={{strtotime($todo['created_date'])}} data-todo-id={{$todo['todo_id']}} >
                            <i class="fa fa-info-circle my-2 px-2 text-black-50 btn" data-toggle="tooltip"
                                data-placement="bottom" title="" data-original-title="Created date"></i>
                            <label class="date-label my-2 text-black-50">{{ date("dS-M-Y",strtotime($todo['created_date'])) }}</label>                            
                        </div>
                    </div>
                </div>
                {{-- end actions --}}
        
            </div>
        </div>
        {{-- end item --}}
    </div>
@endforeach