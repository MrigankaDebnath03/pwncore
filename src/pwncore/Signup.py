import jwt
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from tortoise import fields 
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model 

app = FastAPI()

JWT_SECRET = 'myjwtsecret'

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password_hash = fields.CharField(128)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)

User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)

class Team(Model):
    id = fields.IntField(pk=True)
    team_name = fields.CharField(50, unique=True)
    member1 = fields.CharField(50)
    member2 = fields.CharField(50)
    member3 = fields.CharField(50)
    team_password_hash = fields.CharField(128)

Team_Pydantic = pydantic_model_creator(Team, name='Team')
TeamIn_Pydantic = pydantic_model_creator(Team, name='TeamIn', exclude_readonly=True)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


async def authenticate_team(team_name: str, team_password: str):
    team = await Team.get(team_name=team_name)
    if not team or not bcrypt.verify(team_password, team.team_password_hash):
        return False
    return team


async def get_current_team(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        team = await Team.get(id=payload.get('id'))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Invalid team name or password'
        )
    return await Team_Pydantic.from_tortoise_orm(team)

@app.post('/team/token')
async def generate_team_token(team_data: TeamIn_Pydantic):
    team = await authenticate_team(team_data.team_name, team_data.team_password)

    if not team:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Invalid team name or password'
        )

    team_obj = await Team_Pydantic.from_tortoise_orm(team)

    token = jwt.encode(team_obj.dict(), JWT_SECRET)

    return {'access_token': token, 'token_type': 'bearer'}


@app.post('/team/signup', response_model=Team_Pydantic)
async def signup_team(team: TeamIn_Pydantic):
    team_obj = Team(
        team_name=team.team_name,
        member1=team.member1,
        member2=team.member2,
        member3=team.member3,
        team_password_hash=bcrypt.hash(team.team_password)
    )
    await team_obj.save()
    return await Team_Pydantic.from_tortoise_orm(team_obj)

@app.post('/team/login')
async def team_login(team_data: TeamIn_Pydantic, team: Team_Pydantic = Depends(get_current_team)):
    token = jwt.encode(team.dict(), JWT_SECRET)
    return {'access_token': token, 'token_type': 'bearer'}   

# Replace with your actual PostgreSQL database URL
db_url = 'postgres://username:password@localhost/your_database'

register_tortoise(
    app,
    db_url=db_url,
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True
)
