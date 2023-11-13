from tortoise import fields
from tortoise import Model
#from passlib.hash import bcrypt


class Participant(Model):
    name : str = fields.TextField(null=False)
    registrationNo : fields.CharField = fields.CharField(max_length=40, pk=True)
    email : fields.CharField = fields.CharField(max_length=255, null=True, unique=True)
    phoneNo : fields.CharField = fields.CharField(max_length=32, null=True, unique=True)

    async def email_fn(self, get=False, update=False, new_value=None):
        if get and await self.check_if_exists():
            async for i in self.get(registrationNo=self.registrationNo).values_list("email"):
                return i

        elif update and await self.check_if_exists() and new_value :
            return True if await self.filter(registrationNo=self.registrationNo).update(email=new_value) == new_value else False
        elif (get == update) or (update and new_value is None):
            raise Exception
        else:
            return False

    async def check_if_exists(self) -> bool:
        return True if await self.filter(registrationNo=self.registrationNo).exists() else False

    async def phone_fn(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():
            async for i in self.get(registrationNo=self.registrationNo).values_list("phoneNo"):
                return i
        elif update and await self.check_if_exists() and new_value :
            return True if self.filter(registrationNo=self.registrationNo).update(phoneNo=new_value) == new_value else False

        elif (get == update) or (update and new_value is None):
            raise Exception
        else:
            return False

    async def name_fn(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():
            async for i in self.get(registrationNo=self.registrationNo).values_list("name"):
                return i

        elif update and await self.check_if_exists() and new_value  :
            return True if self.filter(registrationNo=self.registrationNo).update(name=new_value) == new_value else False

        elif (get == update) or (update and new_value is None):
            raise Exception
        else:
            return False

    class Meta:
        table = "Participant"


class Team(Model):
    name : fields.CharField = fields.CharField(max_length=255, pk=True)
    password : fields.CharField = fields.CharField(max_length=255, unique=True, null=False)
    member1regNo : fields.CharField = fields.CharField(max_length=255, unique=True, null=False)
    member2regNo : fields.CharField = fields.CharField(max_length=255, unique=True, null=False)
    member3regNo : fields.CharField = fields.CharField(max_length=255, unique=True, null=False)
    current_points : int = fields.IntField(null=True)
    current_stage : int = fields.IntField(null=True)
    last_timestamp : fields.DatetimeField = fields.DatetimeField(null=True)

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
        elif update and await self.check_if_exists() and new_value :
            return True if await self.filter(name=self.name).update(current_points=new_value) == new_value else False

        elif (get == update) or (update and new_value is None):
            raise Exception
        else:
            return False

    async def last_timestamp_fn(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():
            async for i in self.get(name=self.name).values_list("lasttime_stamp"):
                return i
        elif update and await self.check_if_exists() and new_value :
            return True if self.filter(name=self.name).update(lasttime_stamp=new_value) == new_value else False

        elif (get == update) or (update and new_value is None):
            raise Exception
        else:
            return False

    async def current_stage_fn(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():

            async for i in self.get(name=self.name).values_list("current_stage"):
                return i

        elif update and await self.check_if_exists() and new_value :
            return True if self.filter(name=self.name).update(current_stage=new_value) == new_value else False

        elif (get == update) or (update and new_value is None):
            raise Exception
        else:
            return False

    async def members(self , get=False , update=False , **kwargs):
        if get and await self.check_if_exists():
            return await self.get(name=self.name).values(member1="member1regNo", member2="member2regNo", member3="member3regNo")
                

        elif update and await self.check_if_exists() and any(i in ["member1regNo", "member2regNo", "member3regNo"] for i in kwargs.keys()) :
            return await self.filter(name=self.name).update(**kwargs)
        elif (get == update) or (update and any(i in ["member1regNo", "member2regNo", "member3regNo"] for i in kwargs.keys())):
            raise Exception
        else:
            return False

    class Meta:
        table = "Team"
