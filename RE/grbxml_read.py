import pandas as pd
import xml.etree.ElementTree as et
xtree = et.parse("GRB_107.xml")
xroot = xtree.getroot()
df_cols = ["PI", "Researcher", "Title", "ORGAN"]
rows = []
for node in xroot[:11]:
    s_pi = node.find("PI").text if node is not None else None
    s_research = node.find("RESEARCHER").text if node is not None else None
    s_researcher = s_research.split(',') if s_research is not None else []
    s_title = node.find("PNCH_DESC").text if node is not None else None
    s_organ = node.find("PLAN_ORGAN_CODE").text if node is not None else None
    rows.append({"PI": s_pi, "Researcher": s_researcher,
                 "Title": s_title, "ORGAN": s_organ})
out_df = pd.DataFrame(rows, columns=df_cols)
for item in out_df["Researcher"]:
    print(item)
