from main import ma


class RoleSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "actor_id", "movie_id")


role_schema = RoleSchema()
roles_schema = RoleSchema(many=True)