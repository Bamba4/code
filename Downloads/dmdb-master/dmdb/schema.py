from dmdbBaseManagement.schema import UserQuery, UserMutation
from graphene import ObjectType, Schema


class Query(UserQuery, ObjectType):
    pass


class Mutation(UserMutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
