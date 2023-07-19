from docxtpl import DocxTemplate


def EPC_document_creator(EPC_data):
    """Takes data from planit and filters it.
    This filtered data is then populated into a word document table"""

    doc = DocxTemplate("Docx_Templates/EPCTemplate.docx")
    EPCRows = []

    # Collect Relevant Information from Search
    for n in range(len(EPC_data["rows"])):
        address = EPC_data["rows"][n]["address"]
        energy_rating = EPC_data["rows"][n]["current-energy-rating"]
        floor_area = EPC_data["rows"][n]["total-floor-area"]
        inspection_date = EPC_data["rows"][n]["inspection-date"]

        EPCRows.append({"address": address, "energyRating": energy_rating, "date": inspection_date,
                        "floorArea": floor_area})

    context = {
        "EPCRows": EPCRows
    }

    doc.render(context)

    doc.save("Docx_Outputs/EPC_Example.docx")

    print("EPC Document Successfully Populated")
