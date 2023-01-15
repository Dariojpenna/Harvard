from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newlisting", views.createlisting, name="newlisting"),
    path("watchlist/<int:id>", views.Watchlist, name="watchlist"),
    path("watchlist", views.Watchlist, name="watchlist"),
    path("error", views.Error, name="error"),
    path("auction/<article>", views.Product, name="product"),
    path('categories',views.categories,name='categories'),
    path('delete/<Article>',views.delete,name='delete'),
    path('create',views.create,name='create')
    
]
