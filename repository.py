from neo4j import GraphDatabase, basic_auth


def embed_anchor_href_combinations(anchor_href_combinations):
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", str("secret")))
    with driver.session() as session:
        try:
            session.write_transaction(_tf_detach_delete)
            for combination in anchor_href_combinations:
                session.write_transaction(_tf_anchor_href_combinations, combination)
        finally:
            driver.close()


def embed_ambiguous_combinations(ambiguous_combinations, mode):
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", str("secret")))
    with driver.session() as session:
        try:
            session.write_transaction(_tf_detach_delete)
            for key in ambiguous_combinations:
                if mode:
                    session.write_transaction(_tf_href_with_ambiguous_anchors, key, ambiguous_combinations[key])
                else:
                    session.write_transaction(_tf_anchor_with_ambiguous_hrefs, key, ambiguous_combinations[key])
        finally:
            driver.close()


def _tf_detach_delete(tx):
    tx.run("MATCH (n) DETACH DELETE n")


def _tf_anchor_href_combinations(tx, element):
    tx.run("CREATE (a: Anchor {name: $name})-[:REFERENCES]->(l:Link {href: $href})", name=element[0], href=element[1])


def _tf_href_with_ambiguous_anchors(tx, key, values):
    tx.run("CREATE (l:Link {href: $href})", href=key)
    for value in values:
        tx.run("MATCH (l:Link {href: $href})"
               "CREATE (l)<-[:REFERENCED_BY]-(a:Anchor {name: $name})", name=value, href=key)


def _tf_anchor_with_ambiguous_hrefs(tx, key, values):
    tx.run("CREATE (a:Anchor {name: $name})", name=key)
    for value in values:
        tx.run("MATCH (a: Anchor {name: $name})"
               "CREATE (a)-[:REFERENCES]->(l:Link {href: $href})", name=key, href=value)
