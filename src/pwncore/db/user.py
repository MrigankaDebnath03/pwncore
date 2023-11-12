class Team:
    does_exists=None
    def __init__(self,create=False,name=None,**kwargs):
        #Make arg create=True/False
        self.name=name
        if (create):
            print("Create a new team without checking")
        else:
            if self.check_if_exists():
                print("Pass")
            else:
                print("Raise an exception")

    async def check_password(pwd:str)->bool:
        return True

    async def _check_if_exists()->bool:
        return True

    async def current_points(self,get=False,update=False):
        if get:
            return "list"
        elif update:
            return True
        else:
            raise ValueError

    async def last_timestamp(self,get=False,update=False):
        if get:
            return "list"
        elif update:
            return True
        else:
            raise ValueError

    async def current_stage(self,get=False,update=False):
        if get:
            return "list"
        elif update:
            return True
        else:
            raise ValueError

    async def members_list(self,get=False,update=False):
        if get:
            return {}
        elif update:
            return True
        else:
            raise ValueError

    async def delete(self):
        return True


class Participant:
    does_exist=None
    def __init__(self,create=False,regNo=None,**kwargs):
        self.regNo=regNo

        if create:
            print("Initiate create functions")
        else:
            print("Raise exception if not exists")

    async def email(self,get=False,update=False):
        return True

    async def phone(self,get=False,update=False):
        return True

    async def name(self,get=False,update=False):
        return True

    async def delete(self):
        return True
