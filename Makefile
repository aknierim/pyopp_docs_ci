TeXInputs = TEXINPUTS=$(PWD):$(PWD)/common:


all: build/slides.pdf

build/slides.pdf: FORCE | build
	$(TeXInputs) latexmk -r ./latexmkrc slides.tex

preview: FORCE | build
	$(TeXInputs) latexmk -r ./latexmkrc -pvc slides.tex

FORCE:

build:
	mkdir -p build

clean:
	rm -r build
