

<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::domain('da.adlynk.in')->group(function () {
    Route::get('/', [App\Http\Controllers\Caller\LoginController::class, 'index']);
    Route::get('login', [App\Http\Controllers\Caller\LoginController::class, 'index'])->name('login');
    Route::post('login', [App\Http\Controllers\Caller\LoginController::class, 'validateUser']);
    Route::get('login/{driver}/start', [App\Http\Controllers\Caller\LoginController::class, 'redirectToProvider']);
    Route::any('login/{driver}/callback', [App\Http\Controllers\Caller\LoginController::class, 'handleProviderCallback']);
    Route::any('logout', [App\Http\Controllers\Caller\LoginController::class, 'Logout']);
    Route::middleware(['auth:web'])->group(function () {
    });
});

// Serve the calendar template from the public directory so asset paths resolve.
// Redirect to the public file (served directly by Laravel's public folder).
Route::get('/html-page', function () {
    $publicPath = '/html/verticle-menu-templet/app-calendar.html';
    return redirect($publicPath);
});

