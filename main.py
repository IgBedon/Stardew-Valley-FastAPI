from fastapi import FastAPI, HTTPException, Response
from fastapi.encoders import jsonable_encoder
from models import Character
from typing import Optional

app = FastAPI()

characters = {
    1: {
        "name": "Pierre",
        "profession": "Seller",
        "gender" : "Male",
        "married": True,
        "image": "url"
    },
    2: {
        "name": "Caroline",
        "profession": "Gym Teacher",
        "gender" : "Female",
        "married": True,
        "image": "url"
    },
    3: {
        "name": "Pierre2",
        "profession": "Fire",
        "gender" : "Male",
        "married": True,
        "image": "url"
    },
    4: {
        "name": "Pierre3",
        "profession": "Fire",
        "gender" : "Male",
        "married": True,
        "image": "url"
    },
    5: {
        "name": "Pierre4",
        "profession": "Fire",
        "gender" : "Male",
        "married": True,
        "image": "url"
    },
    6: {
        "name": "Pierre5",
        "profession": "Fire",
        "gender" : "Male",
        "married": True,
        "image": "url"
    },
    7: {
        "name": "Pierre6",
        "profession": "Fire",
        "gender" : "Male",
        "married": True,
        "image": "url"
    },
    8: {
        "name": "Pierre7",
        "profession": "Fire",
        "gender" : "Male",
        "married": True,
        "image": "url"
    },
    9: {
        "name": "Pierre8",
        "profession": "Fire",
        "gender" : "Male",
        "married": True,
        "image": "url"
    },
    10: {
        "name": "Pierre9",
        "profession": "Fire",
        "gender" : "Male",
        "married": True,
        "image": "url"
    }
}

@app.get('/characters')
async def get_characters():
    return characters


@app.get('/characters/{character_id}')
async def get_character(character_id: int):
    try:
        character = characters[character_id]
        return character
    except:
        raise HTTPException(status_code=404, detail="ID not found!")
    

@app.post('/characters', status_code=201)
async def post_characters(character: Optional[Character]=None):
    if character.id not in characters:
        next_id = len(characters)+1
        characters[next_id] = character
        del character.id
        return character
    else:
        raise HTTPException(status_code=409, detail="We already have this character!")


@app.put('/characters/{character_id}')
async def put_character(character_id : int, character: Character):
    if character_id in characters:
        characters[character_id] = character
        character.id = character_id
        del character.id
        return character

    else:
        raise HTTPException(status_code=409, detail="This character isn't in the list!")


@app.delete('/characters/{character_id}')
async def delete_character(character_id: int):
    if character_id in characters:
        del characters[character_id]
        return Response(status_code=204)
    else:
        raise HTTPException(status_code=409, detail="This character isn't in the list!")
    

@app.patch('/characters/{character_id}', response_model=Character)
async def patch_character(character_id : int, character: Character):
    if character_id in characters:
        stored_character = characters[character_id]
        stored_character_model = Character(**stored_character)
        update_character = character.model_dump(exclude_unset=True)
        updated_character = stored_character_model.model_copy(update=update_character)
        characters[character_id] = jsonable_encoder(updated_character)
        return updated_character

    else:
        raise HTTPException(status_code=409, detail="This character isn't in the list!")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host="10.234.84.41", port=8000, log_level="info", reload=True) #host="10.234.84.41"