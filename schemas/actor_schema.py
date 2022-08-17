from main import ma

#create the Actor Schema with Marshmallow, it will provide the serialization needed for converting the data into JSON
class ActorSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description", "date", "status", "priority")

#single actor schema, when one actor needs to be retrieved
actor_schema = ActorSchema()
#multiple actor schema, when many actors need to be retrieved
actors_schema = ActorSchema(many=True)