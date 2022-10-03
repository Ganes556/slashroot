@extends('layouts.main')
@section('scripts')
    <script src="https://code.jquery.com/jquery-3.6.1.js" integrity="sha256-3zlB5s2uwoUzrXK3BT7AX3FyvojsraNFxCc2vC/7pNI=" crossorigin="anonymous"></script>
    <script src='/public/js/todo.js' defer></script>
@endsection
@section('content')
    @include('layouts.sections.navigation', ['active' => 'todo'])
    <main>
        <div class="container m-5 p-2 rounded mx-auto bg-light shadow">
            <!-- App title section -->
            <div class="row m-1 p-4">
                <div class="col">
                    <div class="p-1 h1 text-primary text-center mx-auto display-inline-block">
                        <i class="fa fa-check bg-primary text-white rounded p-2"></i>
                        <u>My Todo-s</u>
                    </div>
                </div>
            </div>
            <!-- Create todo section -->
            <div class="row m-1 p-3">
                <form class="col col-11 mx-auto" id="addTodo" method="POST">
                    <div
                        class="row bg-white rounded shadow-sm p-2 add-todo-wrapper align-items-center justify-content-center">
                        <div class="col">
                            <input class="form-control form-control-lg border-0 add-todo-input bg-transparent rounded"
                                name="todo" type="text" placeholder="Add new ..">
                        </div>
                        <div class="col-auto px-0 mx-0">
                            <input type="date" class="btn btn-light" name="date" value={{date('Y-m-d')}}>
                        </div>
                        <div class="col-auto px-0 mx-0 mr-2">
                            <button  type="submit" class="btn btn-primary">Add</button>
                        </div>
                        <input type="hidden" name="action" value="add">
                    </div>
                </form>
            </div>
            <div class="p-2 mx-4 border-black-25 border-bottom"></div>

            <!-- View options section -->
            <div class="row m-1 p-3 px-5 justify-content-end">
                <div class="col-auto d-flex align-items-center">
                    <label class="text-secondary my-2 pr-2 view-opt-label">Filter</label>
                    <select class="custom-select custom-select-sm btn my-2" id="filter">
                        <option value="all" selected>All</option>
                        <option value="complete">Completed</option>
                        <option value="active">Active</option>
                    </select>
                </div>
                {{-- <div class="col-auto d-flex align-items-center px-1 pr-3">
                    <label class="text-secondary my-2 pr-2 view-opt-label">Sort</label>
                    <select class="custom-select custom-select-sm btn my-2" id="sort">
                        <option value="added-date" selected>Added date</option>
                        <option value="due-date">Due date</option>
                    </select>
                    <i class="fa fa fa-sort-amount-asc text-info btn mx-0 px-0 pl-1" data-toggle="tooltip"
                        data-placement="bottom" title="Ascending"></i>
                    <i class="fa fa fa-sort-amount-desc text-info btn mx-0 px-0 pl-1 d-none" data-toggle="tooltip"
                        data-placement="bottom" title="Descending"></i>
                </div> --}}
            </div>

            {{-- todo list --}}
            <div id="container-todos">
                @if (empty($todos))
                    <h3 id="todoEmpty" class="text-center text-info">| Your TODO is empty!</h3>
                @else
                    @include('layouts.sections.itemTodo',$todos)
                @endif            
            </div>
            {{-- endsection --}}
            
        </div>
    </main>
@endsection
