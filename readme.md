raw folder is for data

code folder is for python code

envoyer les données sur osf:
    $env:OSF_TOKEN = "8QSngUKA8bnXgynSWfmRWBZvUPlUbQKnyowpvWeQxjf8xmYT07KK7eDJqXt0WUe9fQBrQT"

    osf -p k65yb upload -r raw/ raw/    

configurer les pointeurs grace à git annex:
    git annex init "pc-acquisition"
    git annex add raw/
    git commit -m "add raw EEG as annex pointers" 
    git push -u origin main git-annex