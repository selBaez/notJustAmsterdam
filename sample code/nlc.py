# Code for usng the natural language classifier service 
# Selene Baez modified from Dhaval R Sonawane et al.

from watson_developer_cloud import NaturalLanguageClassifierV1
import json

natural_language_classifier = NaturalLanguageClassifierV1(
    username='906a2c0e-9711-4e76-8d34-b1576ed67ac9',
    password='qVobl1EwDSXj')

HILTON_CLASSIFIER = "341781x90-nlc-7639"

def train_classifier():
    with open('nlc_template_base.csv', 'rb') as training_data:
        classifier = natural_language_classifier.create(
            training_data=training_data,
            name='Hilton template',
            language='en'
            )
    print(json.dumps(classifier, indent=2))

def get_status(classifier_id):
    status = natural_language_classifier.status(classifier_id)
    print (json.dumps(status, indent=2))

def find_class(classifier_id, text):
    classes = natural_language_classifier.classify(classifier_id, text)
    print(json.dumps(classes, indent=2))
    dump = json.dumps(classes)
    output = json.loads(dump)
    topClass = output['classes']['class_name' == output['top_class']]

    print '\n The class is ',topClass['class_name'],' Confidence: ',topClass['confidence'], '\n'


    return topClass

