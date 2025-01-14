from typing import Union

from fastapi import FastAPI

from transformers import pipeline

app = FastAPI()


MODEL = "jy46604790/Fake-News-Bert-Detect"
clf = pipeline("text-classification", model=MODEL, tokenizer=MODEL)

@app.get("/")
def read_root():
    text = "Indonesian police have recaptured a U.S. citizen who escaped a week ago from an overcrowded prison on the holiday island of Bali, the jail s second breakout of foreign inmates this year.  Cristian Beasley from California was rearrested on Sunday, Badung Police chief Yudith Satria Hananta said, without providing further details.  Beasley was a suspect in crimes related to narcotics but had not been sentenced when he escaped from Kerobokan prison in Bali last week. The 32-year-old is believed to have cut through bars in the ceiling of his cell before scaling a perimeter wall of the prison in an area being refurbished. The Kerobokan prison, about 10 km (six miles) from the main tourist beaches in the Kuta area, often holds foreigners facing drug-related charges. Representatives of Beasley could not immediately be reached for comment. In June, an Australian, a Bulgarian, an Indian and a Malaysian tunneled to freedom about 12 meters (13 yards) under Kerobokan prison s walls. The Indian and the Bulgarian were caught soon after in neighboring East Timor, but Australian Shaun Edward Davidson and Malaysian Tee Kok King remain at large. Davidson has taunted authorities by saying he was enjoying life in various parts of the world, in purported posts on Facebook.  Kerobokan has housed a number of well-known foreign drug convicts, including Australian Schappelle Corby, whose 12-1/2-year sentence for marijuana smuggling got huge media attention."
    result = clf(text)
    return {"Hello": result}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
