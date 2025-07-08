import logging
import re


   
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s|%(levelname)s|%(name)s.%(funcName)s:%(lineno)d|%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
   
logger=logging.getLogger(__name__)

p={
    ",",
    ".",
    ":",
    ";"
}

def main():
    sentence = input("Enter Sentence")
    cleaned=sentence
    tokens=set()
    for item in p:
         if item is cleaned:
             tokens.add(item)
         cleaned=cleaned.replace(item,'')
    logger.info(f'User typed in htis sentence: {sentence}')
    #tokens=re.findall(r'[A-Ca-z]+[0-9]+[^A-Za-z0-9\s]",sentence)')
    t=tokens.unionset(cleaned.split(''))
    print(t)


if __name__ == "__main__":
    main()
