#listas compostas
pc = ['processador','mouse','teclado',{'memoria ram','hd','ssd'},'webcam']
print("item 1: ", pc[0])
print("item 4: ", pc[3])
print("item 4.1: ",pc[3][0])
print("ultimo item da subilista:", pc[3][-1])
#
pc[0] = "fonte"
print(pc)
#substituir memoria ram por memoria flash
pc[3][0] = "memoria flash"
print(pc)
