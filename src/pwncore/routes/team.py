from __future__ import annotations
from pwncore.db import Team
from fastapi import APIRouter

# Metadata at the top for instant accessibility
metadata = {"name": "team", "description": "Operations with teams"}

router = APIRouter(prefix="/team", tags=["team"])


@router.get("/list")
async def team_list():
    # Do login verification here
    all_list = await Team.all()
    return [{"team_name": "CID Squad"}, {"team_name": "Astra"}]


@router.get("/login")
async def team_login():
    # Do login verification here
    team = Team(name="test")
    is_true = await team.check_password("testing") # bool
    return {"status": is_true}

@router.get("/update/test/{current_points}")
async def team_change_password(current_points:int):
    team = Team(name="test")
    is_true = await team.check_password("testing")
    update = await team.current_points_fn(update=True,new_value=current_points) #bool
    return {"status":update}

@router.get("/get/current_points")
async def get_test():
    team=Team(name="test")
    val=await team.current_points_fn(get=True)
    return {"status":val} # int

@router.get("/members/")
async def team_members():
    team=Team(name="test")
    val=await team.members(get=True) # a dict of members with keys ['member1','member2','member3']
    return {'status':val}

@router.get("/members/update")
async def update():
    team=Team(name="test")
    val=await team.members(update=True,member1regNo="22BCE",member2regNo='23BEE')
    return {'status':val} # 1 and breaks for any other keys
