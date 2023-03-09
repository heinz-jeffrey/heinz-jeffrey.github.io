
all: index.html schedule.html

index.html: index.md my.css footer.html
	pandoc -s -f markdown -t html -c my.css -A footer.html index.md -o index.html

schedule.html: schedule.md my.css footer.html
	pandoc -s -f markdown -t html -c my.css -A footer.html schedule.md -o schedule.html

clean: 
	rm -f *.html
