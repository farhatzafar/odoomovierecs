{
    'name': "Movie Recommendations",
    'version': '18.0.0.1',
    'author': 'Farhat',
    'description': "A module that displays a catalog of movies. And recommends movies based on user preference.",
    'depends': ['base'],
    'application': True,
    'data': ['security/ir.model.access.csv', 'views/movie_views.xml', 'views/movie_menus.xml']
}