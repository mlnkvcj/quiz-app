# Podešavanje okruženja

Klonirajte repozitorijum - git clone (putanja ka rep)

## Frontend
Nakon kloniranja repozitorijuma:
```Shell
cd frontend
npm install
npm run dev -- --host
```

## Backend
```Shell
cd backend
Set-ExecutionPolicy Unrestricted -Scope Process
python -m virtualenv env
./env/Scripts/activate
pip install -r reqirements.txt
```


flask(rest api,single page),sql lite baza pitanja 
svelte spa --------------> flask rest api
       	     getQuestion
	   <--------------
            question json
ili preuzmi sva pitanja odjednom pa ispisuj na sajtu ili sve redom
render template zaboravi

svaki task ima svoj branch pa se on konektuje ako je ispravan na main/master branch

## Komande za upravljanje taskovima

git branch task/schema
git checkout task/schema
git branch -d task/schema (brisanje)
git status (stanje repozitorijuma)


trivia api
google translate api

cron-job
 u flask-u (izbrisi sva pitanja koja imaju 30% ili više loših ocena na pitanju

ui zahtevi:
 -ulazak u kviz
 -prikaz highscore tabele
 -stranica za unos pitanja u bazu
