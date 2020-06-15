#!/bin/bash
var=(111 93 183 77 113 12 145 30 124 151 53 98 160 45 14 188 38 39 17 176 216 23 160 74 195 27 240 218 57 116 233 22)
vari=(9 16)
imprimir() {
	     for n in $*
		do
			echo $n
		done
	     
		}
imprimir ${var[*]}
#echo $value
		
