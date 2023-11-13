from __future__ import annotations
from pwncore.db import CTF_Team as Team
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
    is_true = await team.check_password("testing")
    return {"status": is_true}

@router.get("/update/test/{current_points}")
async def team_change_password(current_points:int):
    team = Team(name="test")
    is_true = await team.check_password("testing")
    update = await team.current_points_fn(update=True,new_value=current_points)
    return {"status":update}

@router.get("/get/current_points")
async def get_test():
    team=Team(name="test")
    val=await team.current_points_fn(get=True)
    return {"status":val}

@router.get("/delete")
async def delete():
    team=Team(name="test")
    is_true=await team.delete()
    return {"status":is_true}

@router.get("/members/{team_id}")
async def team_members(team_id: int):
    # Get team members from team_id
    return [{"name": "ABC", "user_id": 3432}, {"name": "DEF", "user_id": 3422}]
