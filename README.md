# Flask associations challenge

Taking if from the previous challenge (Refactor the ripe tomatoes app to a )
- Create a new Director model (id, name, country)
- Create a one to many relationship between one director - many movies. Adapt the schemas to show the director's information when a movie is retrieved.
- Adapt the post movie to add the director id (this id needs to be included in the request body)
- Create a many to many relationship as users write reviews about movies. Review will be a new model including a message, and the foreign keys of user and movie.
- Create and adapt the existing schemas so a user can post a review on a movie
- Create and adapt the existing schemas so movies will show their list of reviews

Extra challenge:
- Create a many to many relationship as actors perform in movies.
- When showing an actor also include a list of movies where the actor has performed.

