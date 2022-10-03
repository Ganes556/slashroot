@extends('layouts.main')

@section('content')
    <main class="container-fluid d-flex flex-column vh-100">
        @include('layouts.sections.authForms',['title'=>$title])
    </main>
@endsection