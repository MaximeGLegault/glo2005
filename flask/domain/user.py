class User:

    def __init__(self, username, first_name, last_name, country, email, hashed_password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.email = email
        self.hashed_password = hashed_password
