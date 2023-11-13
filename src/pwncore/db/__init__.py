from tortoise import fields
from tortoise import Model


class CTF_Participant(Model):
    name = fields.TextField(null=False)
    registrationNo = fields.CharField(max_length=40, pk=True)
    email = fields.CharField(max_length=255, null=True, unique=True)
    phoneNo = fields.CharField(max_length=32, null=True, unique=True)
    team : fields.ReverseRelation["CTF_Team"]

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
    member1regNo : fields.ForeignKeyRelation[CTF_Participant] = fields.ForeignKeyField("models.CTF_Participant",
                                                                                       related_names="team")
#    member2regNo : fields.ForeignKeyRelation[CTF_Participant] = fields.ForeignKeyField("models.CTF_Participant",related_names="team")
#    member3regNo : fields.ForeignKeyRelation[CTF_Participant] = fields.ForeignKeyField("models.CTF_Participant",related_names="team")
    current_points = fields.IntField(null=True)
    current_stage = fields.IntField(null=True)
    lasttime_stamp = fields.DatetimeField(null=True)

    class Meta:
        table = "CTF_Team"
