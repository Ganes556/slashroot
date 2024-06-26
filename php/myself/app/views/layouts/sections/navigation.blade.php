<header class="sticky-top ">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary py-3">
        <div class="container-fluid">
        <a class="navbar-brand text-decoration-underline" href="#">My Todo-s</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="{{ ($active == 'home') ? 'nav-link active': 'nav-link' }}" aria-current="page" href='/home.php'>Home</a>
                </li>
                <li class="nav-item">
                    <a class="{{ ($active == 'todo') ? 'nav-link active': 'nav-link' }}" aria-current="page" href='/todo.php'>Todo</a>
                </li>
            </ul>
            <a href='/logout.php' type="button" class="btn btn-danger">Logout</a>
        </div>
        </div>
    </nav>
</header>