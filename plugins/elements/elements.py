from pyrogram import Client, types, filters
import json
import os
import pandas as pd


current_file_path = os.path.abspath(__file__)
parent_folder = os.path.dirname(current_file_path)

with open(f"{parent_folder}/elements.json", "r") as e:
    elements = json.load(e)


def query(query):
    results = []
    try:
        if len(query.strip()) == 0:
            results.append({
                "Title": "Enter the element you want",
                "SubTitle": "you can use element name, atomic number and symbol",
            })
            results.append({
                "Title": "Enter the Data you want",
                "SubTitle": "you can use names, groups and numbers"
            })

        elif query.isdigit():
            query = int(query)

            EleNam_AtoNum = [element["name"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Name: {EleNam_AtoNum}",


            })
            EleSym_AtoNum = [element["symbol"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Symbol: {EleSym_AtoNum}",


            })
            EleNum_AtoNum = [element["atomicNumber"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Atomic Number: {EleNum_AtoNum}",


            })
            EleMas_AtoNum = [element["atomicMass"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Atomic Mass: {EleMas_AtoNum}",


            })
            ElePer_AtoNum = [element["period"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Period: {ElePer_AtoNum}",


            })
            EleGer_AtoNum = [element["group"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Group: {EleGer_AtoNum}",


            })
            EleBlo_AtoNum = [element["block"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Block: {EleBlo_AtoNum}",


            })
            EleCon_AtoNum = [element["electronicConfiguration"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Electronic Configuration: {EleCon_AtoNum}",


            })
            EleOxi_AtoNum = [element["oxidationStates"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Oxidation States: {EleOxi_AtoNum}",


            })
            EleGrb_AtoNum = [element["groupBlock"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Group Block: {EleGrb_AtoNum}",


            })
            EleSts_AtoNum = [element["standardState"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Standard State: {EleSts_AtoNum}",


            })
            EleEcg_AtoNum = [element["electronegativity"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Electronegativity: {EleEcg_AtoNum}",


            })
            EleAtr_AtoNum = [element["atomicRadius"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Atomic Radius: {EleAtr_AtoNum}",


            })
            EleIoR_AtoNum = [element["ionRadius"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Ion Radius: {EleIoR_AtoNum}",


            })
            EleVDR_AtoNum = [element["vanDerWaalsRadius"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Van Der Waals Radius: {EleVDR_AtoNum}",


            })
            EleIEn_AtoNum = [element["ionizationEnergy"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Ionization Energy: {EleIEn_AtoNum}",


            })
            EleEAf_AtoNum = [element["electronAffinity"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Electron Affinity: {EleEAf_AtoNum}",


            })
            EleBot_AtoNum = [element["bondingType"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Bonding Type: {EleBot_AtoNum}",


            })
            EleMep_AtoNum = [element["meltingPoint"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Melting Point: {EleMep_AtoNum}",


            })
            EleBop_AtoNum = [element["boilingPoint"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Boiling Point: {EleBop_AtoNum}",


            })
            EleDen_AtoNum = [element["density"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Density: {EleDen_AtoNum}",


            })
            EleDis_AtoNum = [element["yearDiscovered"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Year Discovered: {EleDis_AtoNum}",


            })

            EleCol_AtoNum = [element["cpkHexColor"]
                             for element in elements if element["atomicNumber"] == query][0]
            results.append({
                "Title": f"Color: {EleCol_AtoNum}",


            })

        elif query == "names":
            for eleNa in [element["name"] for element in elements]:
                results.append({
                    "Title": f"{eleNa}"})
        elif query == "numbers":
            for eleNa in [element["atomicNumber"] for element in elements]:
                results.append({
                    "Title": f"{eleNa}"})
        elif query == "groups":
            results.append({
                "Title": 'alkaline earth metal'})
            results.append({
                "Title": 'lanthanoid'})
            results.append({
                "Title": 'metalloid'})
            results.append({
                "Title": 'post-transition metal'})
            results.append({
                "Title": 'noble gas'})
            results.append({
                "Title": 'alkali metal'})
            results.append({
                "Title": 'halogen'})
            results.append({
                "Title": 'actinoid'})
            results.append({
                "Title": 'metal'})
            results.append({
                "Title": 'transition metal'})
            results.append({
                "Title": 'nonmetal'})

        elif query in ['alkaline earth metal', 'lanthanoid', 'metalloid', 'post-transition metal', 'noble gas', 'alkali metal', 'halogen', 'actinoid', 'metal', 'transition metal', 'nonmetal']:
            for ex in [element["name"] for element in elements if element["groupBlock"] == query]:
                results.append({
                    "Title": f"{ex}"
                })

        elif query.isalpha and len(query) in [1, 2]:

            EleNam_AtoNum = [element["name"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Name: {EleNam_AtoNum}",


            })
            EleSym_AtoNum = [element["symbol"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Symbol: {EleSym_AtoNum}",


            })
            EleNum_AtoNum = [element["atomicNumber"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Atomic Number: {EleNum_AtoNum}",


            })
            EleMas_AtoNum = [element["atomicMass"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Atomic Mass: {EleMas_AtoNum}",


            })
            ElePer_AtoNum = [element["period"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Period: {ElePer_AtoNum}",


            })
            EleGer_AtoNum = [element["group"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Group: {EleGer_AtoNum}",


            })
            EleBlo_AtoNum = [element["block"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Block: {EleBlo_AtoNum}",


            })
            EleCon_AtoNum = [element["electronicConfiguration"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Electronic Configuration: {EleCon_AtoNum}",


            })
            EleOxi_AtoNum = [element["oxidationStates"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Oxidation States: {EleOxi_AtoNum}",


            })
            EleGrb_AtoNum = [element["groupBlock"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Group Block: {EleGrb_AtoNum}",


            })
            EleSts_AtoNum = [element["standardState"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Standard State: {EleSts_AtoNum}",


            })
            EleEcg_AtoNum = [element["electronegativity"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Electronegativity: {EleEcg_AtoNum}",


            })
            EleAtr_AtoNum = [element["atomicRadius"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Atomic Radius: {EleAtr_AtoNum}",


            })
            EleIoR_AtoNum = [element["ionRadius"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Ion Radius: {EleIoR_AtoNum}",


            })
            EleVDR_AtoNum = [element["vanDerWaalsRadius"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Van Der Waals Radius: {EleVDR_AtoNum}",


            })
            EleIEn_AtoNum = [element["ionizationEnergy"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Ionization Energy: {EleIEn_AtoNum}",


            })
            EleEAf_AtoNum = [element["electronAffinity"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Electron Affinity: {EleEAf_AtoNum}",


            })
            EleBot_AtoNum = [element["bondingType"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Bonding Type: {EleBot_AtoNum}",


            })
            EleMep_AtoNum = [element["meltingPoint"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Melting Point: {EleMep_AtoNum}",


            })
            EleBop_AtoNum = [element["boilingPoint"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Boiling Point: {EleBop_AtoNum}",


            })
            EleDen_AtoNum = [element["density"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Density: {EleDen_AtoNum}",


            })
            EleDis_AtoNum = [element["yearDiscovered"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Year Discovered: {EleDis_AtoNum}",


            })

            EleCol_AtoNum = [element["cpkHexColor"]
                             for element in elements if element["symbol"] == query][0]
            results.append({
                "Title": f"Color: {EleCol_AtoNum}",


            })

        elif query.isalpha and len(query) > 2:

            EleNam_AtoNum = [element["name"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Name: {EleNam_AtoNum}",


            })
            EleSym_AtoNum = [element["symbol"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Symbol: {EleSym_AtoNum}",


            })
            EleNum_AtoNum = [element["atomicNumber"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Atomic Number: {EleNum_AtoNum}",


            })
            EleMas_AtoNum = [element["atomicMass"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Atomic Mass: {EleMas_AtoNum}",


            })
            ElePer_AtoNum = [element["period"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Period: {ElePer_AtoNum}",


            })
            EleGer_AtoNum = [element["group"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Group: {EleGer_AtoNum}",


            })
            EleBlo_AtoNum = [element["block"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Block: {EleBlo_AtoNum}",


            })
            EleCon_AtoNum = [element["electronicConfiguration"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Electronic Configuration: {EleCon_AtoNum}",


            })
            EleOxi_AtoNum = [element["oxidationStates"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Oxidation States: {EleOxi_AtoNum}",


            })
            EleGrb_AtoNum = [element["groupBlock"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Group Block: {EleGrb_AtoNum}",


            })
            EleSts_AtoNum = [element["standardState"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Standard State: {EleSts_AtoNum}",


            })
            EleEcg_AtoNum = [element["electronegativity"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Electronegativity: {EleEcg_AtoNum}",


            })
            EleAtr_AtoNum = [element["atomicRadius"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Atomic Radius: {EleAtr_AtoNum}",


            })
            EleIoR_AtoNum = [element["ionRadius"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Ion Radius: {EleIoR_AtoNum}",


            })
            EleVDR_AtoNum = [element["vanDerWaalsRadius"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Van Der Waals Radius: {EleVDR_AtoNum}",


            })
            EleIEn_AtoNum = [element["ionizationEnergy"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Ionization Energy: {EleIEn_AtoNum}",


            })
            EleEAf_AtoNum = [element["electronAffinity"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Electron Affinity: {EleEAf_AtoNum}",


            })
            EleBot_AtoNum = [element["bondingType"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Bonding Type: {EleBot_AtoNum}",


            })
            EleMep_AtoNum = [element["meltingPoint"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Melting Point: {EleMep_AtoNum}",


            })
            EleBop_AtoNum = [element["boilingPoint"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Boiling Point: {EleBop_AtoNum}",


            })
            EleDen_AtoNum = [element["density"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Density: {EleDen_AtoNum}",


            })
            EleDis_AtoNum = [element["yearDiscovered"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Year Discovered: {EleDis_AtoNum}",


            })

            EleCol_AtoNum = [element["cpkHexColor"]
                             for element in elements if element["name"] == query][0]
            results.append({
                "Title": f"Color: {EleCol_AtoNum}",


            })
        else:
            results.append({
                "Title": "Enter a valid value"})

    except:
        results.append({
                       "Title": "Enter a valid value"})

    return results


@Client.on_inline_query(filters.regex(r'^!ce '))
async def element(app: Client, qu: types.InlineQuery):
    quer = qu.query.split(None, 1)[1]
    results = query(quer)
    try:
        table = pd.DataFrame(results)
        table[['Type', 'Data']] = table['Title'].str.split(':', expand=True)
        table = table.drop(columns=['Title'])
        table['Data'] = '`' + table['Data'] + '`'
    except:
        table = pd.DataFrame(results)
        table.columns = ['Data']

    await qu.answer([
        types.InlineQueryResultArticle(
            title='Click Here',
            input_message_content=types.InputTextMessageContent(
                message_text=f'```{table.to_string(index=False)}```'))])
