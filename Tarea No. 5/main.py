from bitmap import *
# Universidad del Valle de Guatemala
# Grafica por Computadora
# Nombre: Marcos Gutierrez
# Carne: 17909

def reyBoo():
	renderizando = Bitmap(1000,1000)
	glViewPort(0,0,800,800)
	#renderizando.renderer(./modelos/test3.obj, scale=(0,0,0), translate=(0,0,0))
	renderizando.renderer('./modelos/test2.obj',(100,100,100),(3,3,3))
	renderizando.archivo('output.bmp')

print("Renderizando los modelos obj")

print("Renderizando Modelo de blender")
print(reyBoo())
