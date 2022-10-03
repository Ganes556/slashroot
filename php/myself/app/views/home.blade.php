@extends('layouts.main')
@section('content')
    @include('layouts.sections.navigation',['active' => 'home'])
    <main class="d-flex" style="height: 80vh">
        <div class="m-auto h1">
            | Welcome {{$_SESSION['username']}}
        </div>
    </main>
@endsection
