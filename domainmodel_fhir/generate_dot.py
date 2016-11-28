from sqlalchemy import create_engine

engine = create_engine("postgresql://costiaan:taichi78@127.0.0.1:5432/fhir", echo=True)

result = engine.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='dv'
        AND table_type='BASE TABLE'
        AND RIGHT (table_name , 4)='_hub'
        ORDER BY table_name
        """)

hubs = ""
for row in result:
    hubs += row[0]+"; "

result = engine.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'dv'
        and table_type='BASE TABLE'
        AND right(table_name, 5)='_link'
        ORDER BY table_name
        """)

links = ""
for row in result:
    links += row[0]+"; "

result = engine.execute("""
        SELECT table_name, column_name
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE right(table_name, 5) ='_link'
        AND left(column_name,3) = 'fk_'
        ORDER BY table_name
        """)

joins = ""
for row in result:
    joins += """\t\t"""+row[0]+""" -- """+row[1][3:]+"\n"


graph = """graph fhir {\n\toverlap=false;\n\tsplines=true;
\n\tnode [shape=box fontsize=12 fontname="arial" fontcolor=black style=filled fillcolor=lightblue];\n\t\t"""+hubs+"""
\n\tnode [shape=box fontsize=10 fontname="arial" fontcolor=black style=filled fillcolor="#ff9900"];\n\t\t"""+links+"""
\n\tedge [arrowhead=none color="#ff9900"];\n"""+joins+"""\n}
"""

graphfile = open('fhir_datavault.gv', "w")
graphfile.write(graph)
graphfile.close()
print(graph)
