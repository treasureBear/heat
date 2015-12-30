# heat
Housing temperature control/supervision using RPi/Thingspeak and the entire Adafruit store

#Example git actions
git init						Skapa lokal rep där du är
git status						Kolla status
git add *.txt					Lägg till alla txt-filer, även i nya underfoldrar
git commit -m "Bla bla bla"		Commita inkl meddelande
git log							Visa alla commit
git remote add origin https://github.com/try-git/try_git.git	Peka ut github rep och kalla den origin
git push -u origin master		Skicka upp alla lokala commits till origins master branch. Kom ihåg med -u
git pull origin master			Ladda ner andras bidrag
git diff HEAD					Visa diff relativt vår senaste commit (HEAD) OBS stora bokstäver
git diff --staged				Visa adderade ändringar som är redo för commit.
git reset octofamily/octodog.txt Revert
git checkout -- octocat.txt		Backa filen till före förra commit dvs skriv över med commitad version
git branch clean_up				Skapa en branch döpt till clean_up
git branch 						Visa de existerande branches och vilken som är aktiv (master).
git checkout clean_up			Byt till branchen clean_up
git rm '*.txt'					Ta bort alla txt filer från disk och "stagea" händelsen. (OBS! '' behövs).
git commit -m "Remove all the cats" 	Commit mot lokal rep
git checkout master				Byt tillbaka
git merge clean_up				Ta alla ändringar som förts in i clean_up och för in dem i den branch vi står i
git branch -d clean_up			Ta bort branchen clean_up
git push						Skriv alla ändringar in i github
