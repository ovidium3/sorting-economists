# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import time

start=time.time()

api_key = "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"
    
prompt="""
Parse them into separate columns: Last Name, First Name, Middle Name, Title, School, PHD, PHD year, year entered, other comments
If there are other comments in the next row, put it in other comments at the end of the row.
Return the result in a table that can be formulated as a csv table in python.
Some have middle initials and some do not.
Some have special titles and some do not.
Some have mark and some do not.
Use ; as delimiters. be very careful with adding ; so that my csv output is nice.
Add \n at the end of each line
If a cell in the produced table is empty, add a dot.

Engers, Maxim P.  Prof						Virginia  ACDQ	PHD	84	UCLA	1982						
Engle, Robert F.  Retir						Ca-San Diego  CGR	PHD	66	Cornell	1975						
Enke, Benjamin  Assoc						Harvard	PHD	16	Bonn	2016						
Ensminger, Jean E.  Prof						Cal Tech	PHD	84	Northwstrn	2000	Edie and Lew Wasserman Professor of Social Science					
Epple, Dennis N.  Prof Thomas Lord Professor						Carnegie Mel	PHD	75	Princeton	1974						
Epstein, Larry G.  Prof						Boston Univ	PHD	77	Brit Colum	7-07						
Eraslan, Hulya K.K.  Prof						Rice	PHD	01	Minnesota	7-15	Ralph O'Connor Professor of Economics					
Eren, Ozkan  Assoc						Cal-Riversid	PHD	07	So Meth	7-18						
Ergin, Haluk I.  Assoc						Cal-Berkeley	PHD	03	Princeton	2011						
Eriksson, Katherine  Asst						Cal-Davis	PHD	13	UCLA	2015						
Erkkila, John  Retir						Lk Superior  2009	PHD	87	W Ontario	9-90						
Erol, Selman  Asst						Carnegie Mel	PHD	16	Penn							
Escaleras, Monica  Prof						Fla Atlantic	PHD	03	Fla Intl	2003						
Esfahani, Hadi S.  Prof						Illinois  EFLO	PHD	84	Berkeley	1984						
Espey, Molly  Prof						Clemson	PHD	94	Ca-Davis							
Espin-Sanchez, Jose-Antonio  Asst						Yale	PHD	14	Northwstrn	2014						
Esponda, Ignacio  Assoc						Cal-Santa Br  L	PHD	96	Stanford	2017						
Walter J. Mead Chair of Economics																
Esposito, Federico  Asst						Tufts	PHD	16	Yale	7-16						
Esquivel, Carlos  Asst						Rutgers-N Br	PHD	20	Minnesota	2020														
"""

wholeresponse=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": prompt}
    ]
)

response=wholeresponse["choices"][0]["message"]["content"]

import csv

response = response.replace(".; PHD", "PHD")
response = response.replace(".;PHD", "PHD")
lines=response.strip().splitlines()

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for line in lines:
        row=line.strip().split(';')
        writer.writerow(row)

end = time.time()

print("Time taken: ", end - start, "seconds")