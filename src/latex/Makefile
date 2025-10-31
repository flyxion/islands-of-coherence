TEX = main
BIB = islands_of_coherence_refs

all: pdf

pdf:
	lualatex $(TEX)
	biber $(TEX)
	lualatex $(TEX)
	lualatex $(TEX)
	mkdir -p ../../output
	cp $(TEX).pdf ../../output/islands_of_coherence.pdf

clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk *.bcf *.run.xml