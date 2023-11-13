# from pypika import CustomFunction
from pwncore.db import CTF_Team , CTF_Participant
import asyncio


class Team:

    def __init__(self , create=False , name=None , **kwargs):
        self.name = name
        if create:
            async def create():
                keys_list = ["password",
                             "member1regNo",
                             "current_points",
                             "current_stage",
                             "last_timestamp"]
                if keys_list == [x for x in kwargs.keys()]:
                    team_new = await CTF_Team.create(name=self.name, **kwargs)
                    await team_new.save()
                else:
                    raise SyntaxError
            asyncio.run(create())

    async def check_password(self , pwd: str) -> bool:
        if await self.check_if_exists():
            async for i in CTF_Team.get(name=self.name).values_list("password"):
                return True if i == pwd else False
        return False

    async def check_if_exists(self) -> bool:
        return True if await CTF_Team.filter(name=self.name).exists() else False

    async def current_points(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():
            async for i in CTF_Team.get(name=self.name).values_list("current_points"):
                return i
        elif update and await self.check_if_exists() and new_value:
            CTF_Team.filter(name=self.name).update(current_points=new_value)
            return True
        elif get == update or new_value is None :
            raise SyntaxError
        else:
            return False

    async def last_timestamp(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():
            async for i in CTF_Team.get(name=self.name).values_list("last_timestamp"):
                return i
        elif update and await self.check_if_exists() and new_value:
            CTF_Team.filter(name=self.name).update(last_timestamp=new_value)
            return True
        elif get == update or new_value is None:
            raise SyntaxError
        else:
            return False

    async def current_stage(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():

            async for i in CTF_Team.get(name=self.name).values_list("current_stage"):
                return i

        elif update and await self.check_if_exists() and new_value:
            CTF_Team.filter(name=self.name).update(current_stage=new_value)
            return True
        elif get == update or new_value is None:
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
            CTF_Team.filter(name=self.name).delete()
            return not await self.check_if_exists()
        return False


class Participant:

    def __init__(self , create=False , regNo=None , **kwargs):
        self.regNo = regNo
        if create:
            async def create():
                if ["name", "email", "phoneNo"] == [x for x in kwargs.keys()]:
                    participant = CTF_Participant.create(registrationNo=self.regNo)
                    await participant.save()
                else:
                    raise SyntaxError
            asyncio.run(create())

    async def email(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():

            async for i in CTF_Participant.get(registrationNo=self.regNo).values_list("email"):  # noqa: B950
                return i
        elif update and await self.check_if_exists() and new_value:
            CTF_Participant.filter(registrationNo=self.regNo).update(email=new_value)
        elif get == update:
            raise SyntaxError
        else:
            return False

    async def check_if_exists(self) -> bool:
        participant = await CTF_Participant.filter(registrationNo=self.regNo)
        return True if participant.exists() else False

    async def phone(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():
            async for i in CTF_Participant.get(registrationNo=self.regNo).values_list("phoneNo"):  # noqa: B950
                return i
        elif update and await self.check_if_exists() and new_value:
            CTF_Participant.filter(registrationNo=self.regNo).update(phoneNo=new_value)
            return True
        elif get == update:
            raise SyntaxError
        else:
            return False

    async def name(self , get=False , update=False , new_value=None):
        if get and await self.check_if_exists():

            async for i in CTF_Participant.get(registrationNo=self.regNo).values_list("name"):  # noqa: B950
                return i

        elif update and await self.check_if_exists() and new_value:
            CTF_Participant.filter(registrationNo=self.regNo).update(name=new_value)
            return True
        elif get == update:
            raise SyntaxError
        else:
            return False

    async def delete(self):
        if await self.check_if_exists():
            CTF_Participant.filter(registrationNo=self.regNo).delete()
            return not await self.check_if_exists()
        return False
