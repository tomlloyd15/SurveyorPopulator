from docxtpl import DocxTemplate, InlineImage


def combined_document_creator(user_address, planning_data, EPC_data):
    doc = DocxTemplate("Docx_Templates/combinedTemplate.docx")

    EPCRows = []
    planningRows = []

    # Collect Relevant Information from planning Search
    for n in range(len(planning_data["records"])):
        address = planning_data["records"][n]["address"]
        area_name = planning_data["records"][n]["area_name"]
        description = planning_data["records"][n]["description"]
        consulted_date = planning_data["records"][n]["consulted_date"]
        decided_date = planning_data["records"][n]["decided_date"]
        try:
            decision = planning_data["records"][n]["other_fields"]["decision"]
        except KeyError:
            decision = ""

        planningRows.append({"address": address, "areaName": area_name, "description": description,
                             "consultDate": consulted_date, "decideDate": decided_date, "decision": decision})

    # Collect Relevant Information from EPC Search
    for n in range(len(EPC_data["rows"])):
        address = EPC_data["rows"][n]["address"]
        energy_rating = EPC_data["rows"][n]["current-energy-rating"]
        floor_area = EPC_data["rows"][n]["total-floor-area"]
        inspection_date = EPC_data["rows"][n]["inspection-date"]

        EPCRows.append({"address": address, "energyRating": energy_rating, "date": inspection_date,
                        "floorArea": floor_area})

    context = {
        "userAddress": user_address,
        "planningRows": planningRows,
        "EPCRows": EPCRows,
        "mapImage": InlineImage(doc, "Tools/Map_Images/map.png")
    }

    doc.render(context)

    doc.save("Docx_Outputs/combinedExample.docx")

    print("Document Successfully Populated")