import outlines

from transformers import BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

args ={}
args["quantization_config"] = bnb_config

# model = outlines.models.exl2(model_path="models/CapybaraHermes-2.5-Mistral-7B-GPTQ", device="cuda")

# model = outlines.models.llamacpp(model_path="models/mistral-7b-instruct-v0.2.Q2_K.gguf", device="cuda", model_kwargs={"verbose":False})
model = outlines.models.transformers("mistralai/Mistral-7B-Instruct-v0.2", device="cuda", model_kwargs=args)

prompt = """You are a sentiment-labelling assistant.
Is the following review positive or negative?

Review: This restaurant is just awesome! its was so good, i love it!
"""

# generator = outlines.generate.choice(model, ["Positive", "Negative"])
# answer = generator(prompt)
# print(answer)

schema = '''{
    "title": "Character",
    "type": "object",
    "properties": {
        "name": {
            "title": "Name",
            "maxLength": 10,
            "type": "string"
        },
        "age": {
            "title": "Age",
            "type": "integer"
        },
        "armor": {"$ref": "#/definitions/Armor"},
        "weapon": {"$ref": "#/definitions/Weapon"},
        "strength": {
            "title": "Strength",
            "type": "integer"
        }
    },
    "required": ["name", "age", "armor", "weapon", "strength"],
    "definitions": {
        "Armor": {
            "title": "Armor",
            "description": "An enumeration.",
            "enum": ["leather", "chainmail", "plate"],
            "type": "string"
        },
        "Weapon": {
            "title": "Weapon",
            "description": "An enumeration.",
            "enum": ["sword", "axe", "mace", "spear", "bow", "crossbow"],
            "type": "string"
        }
    }
}'''

generator = outlines.generate.json(model, schema)

for index in range(0, 10):
    character = generator("Give me a weak young character description")
    print(character)
