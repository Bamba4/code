from graphene import ObjectType, List, Mutation, Field, String, InputObjectType, Int, Argument
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model


class UserType(DjangoObjectType):
    """
        User generate by django
    """
    class Meta:
        model = get_user_model()

# Query for user


class UserQuery(ObjectType):
    """
        The query for the user
        @method: GET
    """
    users = List(UserType)
    user = Field(UserType, user_id=Argument(Int))
    
    def resolve_user(self, root, user_id):
        return get_user_model().objects.get(id=user_id)
    
    def resolve_users(self, root):
        return get_user_model().objects.all()

# Mutation for user


class InputUser(InputObjectType):
    """
        Input for to create and update a user
    """
    username = String()
    password = String()
    email = String()
    first_name = String()
    last_name = String()


class CreateUser(Mutation):
    """
        Create a new user
        @method: Post in REST API
    """
    user = Field(UserType)

    class Arguments:
        user = InputUser(required=True)
    
    def mutate(self, info, user=None):
        user = get_user_model()(username=user.username, email=user.email, first_name=user.first_name, last_name=user.last_name)
        user.set_password(user.password)
        user.save()
        return CreateUser(user=user)


class UpdateUser(Mutation):
    """
        Update a user
        @method: Put in REST API
    """
    user = Field(UserType)
    
    class Arguments:
        user_id = Int()
        user = InputUser()
    
    def mutate(self, info, user_id, user=None):
        old_user = get_user_model().objects.get(id=user_id)
        old_user.username = user.username if user.username else old_user.username
        old_user.email = user.email if user.email else old_user.email
        old_user.set_password(user.password) if user.password else old_user.set_password(old_user.password)
        old_user.first_name = user.first_name if user.first_name else old_user.first_name
        old_user.last_name = user.last_name if user.last_name else old_user.last_name
        old_user.save()
        return UpdateUser(user=old_user)


class DeleteUser(Mutation):
    """
        Delete a user existing
        @DELETE in Rest API
    """
    user_id = Int()
    
    class Arguments:
        user_id = Int()
    
    def mutate(self, info, user_id):
        user = get_user_model().objects.get(id=user_id)
        user.delete()
        return DeleteUser(user_id=user_id)
    
    
class UserMutation(ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
