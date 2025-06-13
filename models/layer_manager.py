import ezdxf

class LayerManager:
    def __init__(self, doc, name, color=7, linetype="CONTINUOUS"):
        self.doc = doc
        self.name = name
        self.color = color
        self.linetype = linetype
        self.msp = doc.modelspace()
        if name not in doc.layers:
            layer = doc.layers.new(name=name)
            layer.dxf.color = color
            layer.dxf.linetype = linetype

    def add_lwpolyline(self, points, closed=True):
        self.msp.add_lwpolyline(points, dxfattribs={"layer": self.name, "closed": closed})
