from main import ma
from marshmallow import fields

#create the Actor Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class ActorSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "first_name", "last_name", "gender", "country", "roles")

    roles = fields.List(fields.Nested("RoleSchema"))
    

#single actor schema, when one actor needs to be retrieved
actor_schema = ActorSchema()
#multiple actor schema, when many actors need to be retrieved
actors_schema = ActorSchema(many=True)