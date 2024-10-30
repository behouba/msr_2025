from neo4j import GraphDatabase

query = """
MATCH (lib:Artifact)
RETURN lib.id AS LibraryID
LIMIT 1000
"""

class LibDepsMiner:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.driver.verify_connectivity()

    def close(self):
        self.driver.close()

    def get_libs(self):
        with self.driver.session() as session:
            result = session.run(query)
            #Retrieve Only a List of Libraries First:
            #Loop Over Libraries for Dependencies: Retrieve dependencies for each library individually or in smaller groups.
            for record in result:
                print(record)
                # library = record["Library"]
                # year = record["Year"]
                # dependency_count = record["DependencyCount"]
                # print(f"Library: {library}, Year: {year}, Dependency Count: {dependency_count}")

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]


if __name__ == "__main__":
    greeter = LibDepsMiner("bolt://localhost:7687", "neo4j", "Password1")
    greeter.get_libs()
    greeter.close()