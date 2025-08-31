from odoo import fields, models

class Movie(models.Model):

    _name = "movie_recs.movie"
    _description= "Stores info about movies"

    title = fields.Char(string="Title", required=True)

    genre = fields.Selection(
        string="Genre",
        selection=[
            ('horror', 'Horror'),
            ('drama', 'Drama'),
            ('comedy', 'Comedy')
            ]
    )

    release_year = fields.Selection(
        string="Release Year",
        selection=[
            ('2020', '2020'),
            ('2021', '2021'),
            ('2022', '2022'),
            ('2023', '2023'),
            ('2024', '2024'),
            ]
    )

    lead_actor_gender = fields.Selection(
        string="Lead Actor Gender",
        selection=[
            ('male', 'Male'),
            ('female', 'Female')
            ]
    )

    poster_url = fields.Char(string="Poster URL")