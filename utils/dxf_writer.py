import ezdxf
from models.layer_manager import LayerManager

def create_dxf_from_json(data):
    doc = ezdxf.new("R2000", setup=True)
    doc.header["$INSUNITS"] = 1  # Inches

    # Create layers
    building_layer = LayerManager(doc, "Building")
    setbacks_layer = LayerManager(doc, "Setbacks", color=4)
    modules_layer = LayerManager(doc, "Modules", color=6)
    vents_layer = LayerManager(doc, "Vents", color=30)

    layer_managers = {
        "Building": building_layer,
        "Setbacks": setbacks_layer,
        "Modules": modules_layer,
        "Vents": vents_layer
    }

    # Add polylines to corresponding layers
    for layer in data["layers"]:
        manager = layer_managers.get(layer["name"])
        if manager:
            for polyline in layer["polylines"]:
                manager.add_lwpolyline(polyline, closed=layer.get("closed", True))
        else:
            print(f"Warning: Layer '{layer['name']}' not predefined.")

    return doc
