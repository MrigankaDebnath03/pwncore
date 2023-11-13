from tortoise import fields
from tortoise import Model
#from passlib.hash import bcrypt

class CTF_Participant(Model):
    name = fields.TextField(null=False)
    registrationNo = fields.CharField(max_length=40, pk=True)
    email = fields.CharField(max_length=255, null=True, unique=True)
    phoneNo = fields.CharField(max_length=32, null=True, unique=True)
    team : fields.ReverseRelation["CTF_Team"]

    #obj=self

    async def email_fn(self, get=False, update=False, new_value=None):
        if get and await self.check_if_exists():

            async for i in self.get(registrationNo=self.registrationNo).values_list("email"):  # noqa: B950
                return i
        elif update and await self.check_if_exists() and new_value:
            return True if await self.filter(registrationNo=self.registrationNo).update(email=new_value)==new_value else False
        elif (get == update) or (update and new_value is None):
            raise SyntaxError
        else:
            return False

    async def check_if_exists(self) -> bool:
        return True if await self.filter(registrationNo=self.registrationNo).exists() else False  # noqa: B950

    async def phone_fn(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():
            async for i in self.get(registrationNo=self.registrationNo).values_list("phoneNo"):  # noqa: B950
                return i
        elif update and await self.check_if_exists() and new_value:
            return True if self.filter(registrationNo=self.registrationNo).update(phoneNo=new_value)==new_value else False
            
        elif (get == update) or (update and new_value is None):
            raise SyntaxError
        else:
            return False

    async def name_fn(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():

            async for i in self.get(registrationNo=self.registrationNo).values_list("name"):  # noqa: B950
                return i

        elif update and await self.check_if_exists() and new_value:
            return True if self.filter(registrationNo=self.registrationNo).update(name=new_value)==new_value else False
            
        elif (get == update) or (update and new_value is None):
            raise SyntaxError
        else:
            return False

    async def delete(self):
        if await self.check_if_exists():
            return await self.filter(registrationNo=self.registrationNo).delete()
            
        return False

    class Meta:
        table = "CTF_Participant"


class CTF_Team(Model):
    name = fields.CharField(max_length=255, pk=True)
    password = fields.CharField(max_length=255, unique=True, null=False)
    """
    member1regNo : fields.ManyToManyRelation[CTF_Participant] = fields.ManyToManyField("models.CTF_Participant",related_names="team")
    member2regNo : fields.ManyToManyRelation[CTF_Participant] = fields.ManyToManyField("models.CTF_Participant",related_names="team")
    member3regNo : fields.ManyToManyRelation[CTF_Participant] = fields.ManyToManyField("models.CTF_Participant",related_names="team")
    """
    member1regNo : fields.ForeignKeyRelation[CTF_Participant] = fields.ForeignKeyField("models.CTF_Participant", related_names="team")
#    member2regNo : fields.ForeignKeyRelation[CTF_Participant] = fields.ForeignKeyField("models.CTF_Participant",related_names="team")
#    member3regNo : fields.ForeignKeyRelation[CTF_Participant] = fields.ForeignKeyField("models.CTF_Participant",related_names="team")
    current_points = fields.IntField(null=True)
    current_stage = fields.IntField(null=True)
    last_timestamp = fields.DatetimeField(null=True)


    async def check_password(self , pwd: str):
        if await self.check_if_exists():
            async for i in self.get(name=self.name).values_list("password"):
                return True if i == pwd else False
        return False

    async def check_if_exists(self) -> bool:
        return True if await self.filter(name=self.name).exists() else False

    async def current_points_fn(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():
            async for i in self.get(name=self.name).values_list("current_points"):
                return i
        elif update and await self.check_if_exists() and new_value:
            return True if await self.filter(name=self.name).update(current_points=new_value)==new_value else False
            
        elif (get == update) or (update and new_value is None):
            raise SyntaxError
        else:
            return False

    async def last_timestamp_fn(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():
            async for i in self.get(name=self.name).values_list("lasttime_stamp"):
                return i
        elif update and await self.check_if_exists() and new_value:
            return True if self.filter(name=self.name).update(lasttime_stamp=new_value)==new_value else False

        elif (get == update) or (update and new_value is None):
            raise SyntaxError
        else:
            return False

    async def current_stage_fn(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():

            async for i in self.get(name=self.name).values_list("current_stage"):
                return i

        elif update and await self.check_if_exists() and new_value:
            return True if self.filter(name=self.name).update(current_stage=new_value)==new_value else False

        elif (get == update) or (update and new_value is None):
            raise SyntaxError
        else:
            return False

    async def members(self , get=False , update=False , **kwargs):
        if get and await self.check_if_exists():
            return {}
        elif update and await self.check_if_exists():
            return True
        elif get == update:
            raise SyntaxError
        else:
            return False

    async def delete(self):
        if await self.check_if_exists():
            return await self.filter(name=self.name).delete()
            
        return False

    class Meta:
        table = "CTF_Team"
