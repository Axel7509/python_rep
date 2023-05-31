from argo.serialize import JSONSerializer, XMLSerializer


def main():
    """Carries out the subtasks of Lab_3"""

    json_ser = JSONSerializer()
    json_ser.loads(json_ser.dumps({1: 2, 2: 3, 3: 4}))
    print(globals())
    a = {
        1: 2,
        "3": [4, -1, "aboba {([sus])} imposter"],
        5: {
            6: '7',
            8: {
                9: None,
                'None': (True, False)
            },
        }
    }
    print(json_ser.loads(json_ser.dumps((a))))
    print(a == json_ser.loads(json_ser.dumps(a)))

    xml_ser = XMLSerializer()
    print(type(xml_ser.loads(xml_ser.dumps(True))))
    print(type(xml_ser.loads(xml_ser.dumps("None"))))
    print(type(xml_ser.loads(xml_ser.dumps(None))))
    print(type(xml_ser.loads(xml_ser.dumps("14"))))
    print(type(xml_ser.loads(xml_ser.dumps(14))))
    print(type(xml_ser.loads(xml_ser.dumps("14+9j"))))
    print(type(xml_ser.loads(xml_ser.dumps(14 + 9j))))


if __name__ == '__main__':
    main()