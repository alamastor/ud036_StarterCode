import fresh_tomatoes
import media

# Create list of movies.
movies = [
    media.Movie(
        'Mullholland Drive',
        'http://lugerlondon.com/wp-content/uploads/2015/07/mulholland-drive-1.jpeg',
        'https://www.youtube.com/watch?v=XQ5Q0CHQ0EU'
    ),
    media.Movie(
        '24 Hour Party People',
        'https://upload.wikimedia.org/wikipedia/en/d/d0/24_Hour_Party_People_quad_poster.jpg',
        'https://www.youtube.com/watch?v=q2PYyvGFHD8'
    ),
    media.Movie(
        'The Grand Budapest Hotel',
        'https://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg',
        'https://www.youtube.com/watch?v=1Fg5iWmQjwk'
    ),
    media.Movie(
        'Trainspotting',
        'https://walter.trakt.us/images/movies/000/000/503/posters/thumb/fbc7ed133a.jpg',
        'https://www.youtube.com/watch?v=R2GKVtWsXKY'
    )
]

# Create & open movies page.
fresh_tomatoes.open_movies_page(movies)
