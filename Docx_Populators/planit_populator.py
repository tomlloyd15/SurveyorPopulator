from docxtpl import DocxTemplate


def planit_document_creator(planning_data):
    """Takes data from planit and filters it.
    This filtered data is then populated into a word document table"""

    doc = DocxTemplate("Docx_Templates/planningTemplate.docx")
    planningRows = []

    # Collect Relevant Information from Search
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

    context = {
        "planningRows": planningRows
    }

    doc.render(context)

    doc.save("Docx_Outputs/Example.docx")

    print("Document Successfully Populated")
