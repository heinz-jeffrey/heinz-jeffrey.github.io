
all: index.html

index.html: index.md my.css footer.html
	pandoc -s -f markdown -t html -c my.css -A footer.html index.md -o index.html

clean: 
	rm -f *.html
