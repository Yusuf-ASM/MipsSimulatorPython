ddi $s0,$0,-5
addi $s1,$05,5
bgtz $s0,add2
j end
end:
addi $s2,$0,20
add2:
addi $s3,$0,10