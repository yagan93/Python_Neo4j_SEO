from neo4j import GraphDatabase, basic_auth


def graph_embedding(ambiguous_mappings):
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", str("secret")))
    with driver.session() as session:
        try:
            for index, key in enumerate(ambiguous_mappings, start=0):
                session.write_transaction(_create_node, key, ambiguous_mappings[key])
        finally:
            driver.close()
            return "embedded"


def _create_node(tx, key, values):
    tx.run("CREATE (a:Anchor {name: $name})", name=key)
    for value in values:
        tx.run("MATCH (a: Anchor {name: $name})"
               "CREATE (a)-[:REFERENCES]->(l:Link {href: $href})", name=key, href=value)

