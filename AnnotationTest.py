from Annotations import *
from Message import *
from Keyboard_Controllers import WSAD_Controller
from Keyboard_Controllers import MyController

keyboardController = WSAD_Controller()
keyboardController = MyController()

#annotations = {['Cranium'] }
#
#for keys in annotations:
#	annotationManager.createAnnotation(keys, viz.Vector(annotations[keys[0]], annotations[keys[1]], annotations[keys[2]])
	
messageManager = MessageManager()

#Create annotation tool
annotationManager = AnnotationManager(messageManager)

annotationManager.createAnnotation( 'Cranium' , viz.Vector(-0.9658, 0.271, 0.0062) )
annotationManager.createAnnotation( 'Mandible' , viz.Vector(-0.629, 0.288, 0.0228) )
annotationManager.createAnnotation( 'Clavical' , viz.Vector(-0.443, 0.0879, 0.1864) )
annotationManager.createAnnotation( 'Manubrium' , viz.Vector(-0.3101, 0.1896, 0.0311) )
annotationManager.createAnnotation( 'Sternum' , viz.Vector(-0.149, 0.275, 0.0171) )
annotationManager.createAnnotation( 'Pelvic Girdle' , viz.Vector(0.6645, 0.0391, 0.2275) )
annotationManager.createAnnotation( 'Sacrum' , viz.Vector(0.804, -0.1745, -0.0294) )
annotationManager.createAnnotation( 'Coccyx' , viz.Vector(0.9217, -0.2063, -0.0325) )
	
annotationManager.setScale( viz.Vector( 0.1, 0.1, 0.1 ) )
annotationManager.radiateMessages()
annotationManager.activate()

viz.go()


