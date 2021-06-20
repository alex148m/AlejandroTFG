##MAKEFILE##
##AUTHOR: ALEJANDRO MARTINEZ
##DATE: 26/03/2021

#Verbosity test python2 to python3
verbosity : 
	python3 Python3/hypergraph.py > /home/usuario/Escritorio/TFG/AlejandroTFG/Codigo/tests/hyp3_test.txt
	python2 Python2/hypergraph.py > /home/usuario/Escritorio/TFG/AlejandroTFG/Codigo/tests/hyp2_test.txt
	diff /home/usuario/Escritorio/TFG/AlejandroTFG/Codigo/tests/hyp3_test.txt /home/usuario/Escritorio/TFG/AlejandroTFG/Codigo/tests/hyp2_test.txt > /home/usuario/Escritorio/TFG/AlejandroTFG/Codigo/tests/diff_hyp.txt
#	rm /home/usuario/Escritorio/TFG/AlejandroTFG/Codigo/tests/verb2_test.txt
#	rm /home/usuario/Escritorio/TFG/AlejandroTFG/Codigo/tests/verb3_test.txt

paper.pdf: paper.tex plot-data.png
	pdflatex paper.tex

plot-%.png: %.dat plot.py
	./plot.py -i $*.dat -o $@
