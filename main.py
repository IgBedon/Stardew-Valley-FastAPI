from fastapi import FastAPI, HTTPException, Response
from fastapi.encoders import jsonable_encoder
from models import Character
from typing import Optional

app = FastAPI()

characters = {
    "1": {
        "name": "Pierre",
        "profession": "Seller",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/7/7e/Pierre.png"
    },
    "2": {
        "name": "Caroline",
        "profession": "Gym Teacher",
        "gender": "Female",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/8/87/Caroline.png"
    },
    "3": {
        "name": "Jas",
        "profession": "Child",
        "gender": "Female",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/5/55/Jas.png"
    },
    "4": {
        "name": "Vincent",
        "profession": "Child",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/f/f1/Vincent.png"
    },
    "5": {
        "name": "Lewis",
        "profession": "Mayor",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/2/2b/Lewis.png"
    },
    "6": {
        "name": "Robin",
        "profession": "Carpenter",
        "gender": "Female",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/1/1b/Robin.png"
    },
    "7": {
        "name": "Demetrius",
        "profession": "Scientist",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/f/f9/Demetrius.png"
    },
    "8": {
        "name": "Maru",
        "profession": "Scientist",
        "gender": "Female",
        "marriageable": True,
        "image": "https://stardewvalleywiki.com/mediawiki/images/f/f8/Maru.png"
    },
    "9": {
        "name": "Sebastian",
        "profession": "Programmer",
        "gender": "Male",
        "marriageable": True,
        "image": "https://stardewvalleywiki.com/mediawiki/images/a/a8/Sebastian.png"
    },
    "10": {
        "name": "Abigail",
        "profession": "Adventurer",
        "gender": "Female",
        "marriageable": True,
        "image": "https://stardewvalleywiki.com/mediawiki/images/8/88/Abigail.png"
    },
    "11": {
        "name": "Alex",
        "profession": "Athlete",
        "gender": "Male",
        "marriageable": True,
        "image": "https://stardewvalleywiki.com/mediawiki/images/0/04/Alex.png"
    },
    "12": {
        "name": "Evelyn",
        "profession": "Grandma",
        "gender": "Female",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/8/8e/Evelyn.png"
    },
    "13": {
        "name": "George",
        "profession": "Retired",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/7/78/George.png"
    },
    "14": {
        "name": "Penny",
        "profession": "Teacher",
        "gender": "Female",
        "marriageable": True,
        "image": "https://stardewvalleywiki.com/mediawiki/images/a/ab/Penny.png"
    },
    "15": {
        "name": "Gus",
        "profession": "Saloon Owner",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/5/52/Gus.png"
    },
    "16": {
        "name": "Clint",
        "profession": "Blacksmith",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/3/31/Clint.png"
    },
    "17": {
        "name": "Willy",
        "profession": "Fisherman",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/8/82/Willy.png"
    },
    "18": {
        "name": "Sandy",
        "profession": "Oasis Owner",
        "gender": "Female",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/4/4e/Sandy.png"
    },
    "19": {
        "name": "Emily",
        "profession": "Seamstress",
        "gender": "Female",
        "marriageable": True,
        "image": "https://stardewvalleywiki.com/mediawiki/images/2/28/Emily.png"
    },
    "20": {
        "name": "Shane",
        "profession": "Laborer",
        "gender": "Male",
        "marriageable": True,
        "image": "https://stardewvalleywiki.com/mediawiki/images/8/8b/Shane.png"
    },
    "21": {
        "name": "Pam",
        "profession": "Bus Driver",
        "gender": "Female",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/d/da/Pam.png"
    },
    "22": {
        "name": "Harvey",
        "profession": "Doctor",
        "gender": "Male",
        "marriageable": True,
        "image": "https://stardewvalleywiki.com/mediawiki/images/9/95/Harvey.png"
    },
    "23": {
        "name": "Marlon",
        "profession": "Adventurer's Guild",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/3/37/Marlon.png"
    },
    "24": {
        "name": "Wizard",
        "profession": "Wizard",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/c/c7/Wizard.png"
    },
    "25": {
        "name": "Gil",
        "profession": "Traveler",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/6/64/Gil.png"
    },
    "26": {
        "name": "Linus",
        "profession": "Wilderness",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/3/31/Linus.png"
    },
    "27": {
        "name": "Krobus",
        "profession": "Shadow Guy",
        "gender": "Unknown",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/7/71/Krobus.png"
    },
    "28": {
        "name": "Haley",
        "profession": "Photographer",
        "gender": "Female",
        "marriageable": True,
        "image": "https://stardewvalleywiki.com/mediawiki/images/1/1b/Haley.png"
    },
    "29": {
        "name": "Helper",
        "profession": "Does tasks",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/2/21/Henchman_Portrait_1.png"
    },
    "30": {
        "name": "Grandpa",
        "profession": "Unknown",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/8/88/Grandpa.png"
    },
    "31": {
        "name": "Sam",
        "profession": "Musician",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/9/94/Sam.png"
    },
    "32": {
        "name": "Elliott",
        "profession": "Author",
        "gender": "Male",
        "marriageable": True,
        "image": "https://stardewvalleywiki.com/mediawiki/images/b/bd/Elliott.png"
    },
    "33": {
        "name": "Jodi",
        "profession": "Home Maker",
        "gender": "Female",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/4/41/Jodi.png"
    },
    "34": {
        "name": "Kent",
        "profession": "Soldier",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/9/99/Kent.png"
    },
    "35": {
        "name": "Marnie",
        "profession": "Rancher",
        "gender": "Female",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/5/52/Marnie.png"
    },
    "36": {
        "name": "Leah",
        "profession": "Artist",
        "gender": "Female",
        "marriageable": True,
        "image": "https://stardewvalleywiki.com/mediawiki/images/e/e6/Leah.png"
    },
    "37": {
        "name": "Governor",
        "profession": "Mayor",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/4/46/Governor.png"
    },
    "38": {
        "name": "Gunther",
        "profession": "Museum Curator",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/3/3d/Gunther.png"
    },
    "39": {
        "name": "Dwarf",
        "profession": "Adventurer",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/e/ed/Dwarf.png"
    },
    "40": {
        "name": "Morris",
        "profession": "JojaMart Manager",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/9/90/Morris.png"
    },
    "41": {
        "name": "Profesor Snail",
        "profession": "Scientist",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/d/d4/Professor_Snail.png"
    },
    "42": {
        "name": "Security Guard",
        "profession": "Security Guard",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/f/f5/Bouncer.png"
    },
    "43": {
        "name": "Mr. Qi",
        "profession": "Unknown",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/b/b4/Mr._Qi.png"
    },
    "44": {
        "name": "Leo",
        "profession": "Artist",
        "gender": "Male",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/1/1d/Leo.png"
    },
    "45": {
        "name": "Birdie",
        "profession": "Unknown",
        "gender": "Female",
        "marriageable": False,
        "image": "https://stardewvalleywiki.com/mediawiki/images/4/46/Birdie.png"
    }
}

@app.get('/characters')
async def get_characters():
    return characters


@app.get('/characters/{character_id}')
async def get_character(character_id: str):
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
async def put_character(character_id : str, character: Character):
    if character_id in characters:
        characters[character_id] = character
        character.id = character_id
        del character.id
        return character

    else:
        raise HTTPException(status_code=409, detail="This character isn't in the list!")


@app.delete('/characters/{character_id}')
async def delete_character(character_id: str):
    if character_id in characters:
        del characters[character_id]
        return Response(status_code=204)
    else:
        raise HTTPException(status_code=409, detail="This character isn't in the list!")
    

@app.patch('/characters/{character_id}', response_model=Character)
async def patch_character(character_id : str, character: Character):
    if character_id in characters:
        stored_character = characters[character_id]
        stored_character_model = Character(**stored_character)
        del stored_character_model.id
        update_character = character.model_dump(exclude_unset=True)
        updated_character = stored_character_model.model_copy(update=update_character)
        characters[character_id] = jsonable_encoder(updated_character)
        return updated_character

    else:
        raise HTTPException(status_code=409, detail="This character isn't in the list!")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host="127.0.0.1", port=8000, log_level="info", reload=True) #host="10.234.84.41"