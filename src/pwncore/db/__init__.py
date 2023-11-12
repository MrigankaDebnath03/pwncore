from tortoise import Tortoise,feilds,run_async
from tortoise import Model

class CTF_Participant(Model):
    name = feilds.TextFeild(null=False,unique=True)
    registrationNo = feilds.TextFeild(pk=True)
    email = feilds.TextFeild(null=True,unique=True)
    phoneNo = feilds.Textfeild(null=True,unique=True)

    class Meta:
        table="CTF_Participant"


class CTF_Team(Model):
    name = feilds.TextFeild(pk=True)
    #password to be hashed
    member1regNo : feilds.ForeignKeyRelation[CTF_Participant] = feilds.ForeignKeyFeild("models.CTF_Participant",related_names="Team")
    member2regNo : feilds.ForeignKeyRelation[CTF_Participant] = feilds.ForeignKeyFeild("models.CTF_Participant",related_names="Team")
    member3regNo : feilds.ForeignKeyRelation[CTF_Participant] = feilds.ForeignKeyFeild("models.CTF_Participant",related_namez="Team")
    current_points=feilds.IntFeild(null=True)
    current_stage=feilds.IntFeild(null=True)
    lasttime_stamp=feilds.DatetimeFeild(null=True)

    class Meta:
        table="CTF_Team"

