TEXFILE = main
BIBFILE = islands_of_coherence_refs

all: pdf

pdf:
	lualatex $(TEXFILE)
	biber $(TEXFILE)
	lualatex $(TEXFILE)
	lualatex $(TEXFILE)
	mv $(TEXFILE).pdf ../../docs/

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.run.xml *.toc *.lof *.lot
