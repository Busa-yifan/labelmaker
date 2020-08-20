from xml.dom.minidom import Document
import math

def generate(SAVE_PATH, pos1, pos2, name, ration, shape):

    doc = Document()
    annotatoin = doc.createElement('annotation')
    doc.appendChild(annotatoin)

    size = doc.createElement('size')
    annotatoin.appendChild(size)
    size_width = doc.createElement('width')
    size_height = doc.createElement('height')
    size_depth = doc.createElement('depth')
    size_width_text = doc.createTextNode(str(shape[0]))
    size_height_text = doc.createTextNode(str(shape[1]))
    size_depth_text = doc.createTextNode(str(shape[2]))
    size_width.appendChild(size_width_text)
    size_height.appendChild(size_height_text)
    size_depth.appendChild(size_depth_text)
    size.appendChild(size_width)
    size.appendChild(size_height)
    size.appendChild(size_depth)


    pos = zip(pos1, pos2, name)
    for p1, p2, NAME in pos:
        XMIN = min(p1[0], p2[0])
        XMAX = max(p1[0], p2[0])
        YMIN = min(p1[1], p2[1])
        YMAX = max(p1[1], p2[1])
        # XMIN, YMIN = p1
        # XMAX, YMAX = p2
        XMIN = math.floor(XMIN * ration)
        YMIN = math.floor(YMIN * ration)
        XMAX = math.floor(XMAX * ration)
        YMAX = math.floor(YMAX * ration)
        object = doc.createElement('object')
        annotatoin.appendChild(object)

        name = doc.createElement('name')
        name_text = doc.createTextNode(NAME)
        name.appendChild(name_text)
        object.appendChild(name)

        bndbox = doc.createElement('bndbox')
        bndbox_xmin = doc.createElement('xmin')
        bndbox_xmin_text = doc.createTextNode(str(XMIN))
        bndbox_xmin.appendChild(bndbox_xmin_text)
        bndbox_ymin = doc.createElement('ymin')
        bndbox_ymin_text = doc.createTextNode(str(YMIN))
        bndbox_ymin.appendChild(bndbox_ymin_text)
        bndbox_xmax = doc.createElement('xmax')
        bndbox_xmax_text = doc.createTextNode(str(XMAX))
        bndbox_xmax.appendChild(bndbox_xmax_text)
        bndbox_ymax = doc.createElement('ymax')
        bndbox_ymax_text = doc.createTextNode(str(YMAX))
        bndbox_ymax.appendChild(bndbox_ymax_text)
        bndbox.appendChild(bndbox_xmin)
        bndbox.appendChild(bndbox_ymin)
        bndbox.appendChild(bndbox_xmax)
        bndbox.appendChild(bndbox_ymax)
        object.appendChild(bndbox)

    f = open(SAVE_PATH, 'w')
    f.write(doc.toprettyxml(indent=''))
    f.close()