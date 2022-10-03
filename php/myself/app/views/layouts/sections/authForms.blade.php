@php
    $links = ['Register','Login'];
    $currentLink = $links[key(array_diff($links,[$title]))];
@endphp
<form class="w-50 m-auto p-5 d-flex flex-column gap-3 rounded shadow-lg" method="POST">
    <div class="p-1 h2 text-primary text-center mx-auto display-inline-block">
        <h1 class="text-center text-primary fw-bold mb-3 text-uppercase">{{$title}}</h1>
        <i class="fa fa-check bg-primary text-white rounded p-2"></i>
        <u>My Todo-s</u>
    </div>
    <div>
        @if (isset($_SESSION['error']) && !empty($_SESSION['error']))
            <div class="alert alert-danger" role="alert">
                {{ $_SESSION['error'] }}
            </div>
        @endif
        @if (isset($_SESSION['msg']) && !empty($_SESSION['msg']))
            <div class="alert alert-success" role="alert">
                {{ $_SESSION['msg'] }}
            </div>
        @endif
        <div class="form-floating">
            <input type="text" name="username" class="form-control" id="floatingInput" placeholder="example">
            <label for="floatingInput">Username</label>
        </div>
    </div>
    <div class="form-floating">
        <input type="password" name='password' class="form-control" id="floatingPassword" placeholder="Password">
        <label for="floatingPassword">Password</label>
    </div>
    <button type="submit" class="w-50 btn btn-primary fw-bold mx-auto">{{$title}}</button>
    <a href="$currentLink.php" class="link-primary fw-bold text-center">{{ $currentLink }}</a>
</form>