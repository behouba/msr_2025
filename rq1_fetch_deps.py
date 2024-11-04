from neo4j import GraphDatabase
import pandas as pd
import csv


# This script collect the data we will need for RQ.
# RQ1: Do libraries use more dependencies now than in the past?

# Approach: Extract the number of dependencies per library release.
# Compare averages across different timeframes to observe changes in dependency use.

# Neo4j connection
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "Password1"
OUTPUT_FILE="data/dependency_data.csv"

# Initialize Neo4j driver
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

# List all libraries
def get_all_libraries():
    query = """
    MATCH (lib:Artifact)
    RETURN lib.id AS library
    ORDER BY library
    """
    with driver.session() as session:
        result = session.run(query)
        libraries = [record["library"] for record in result]
    return libraries

# Retrieve releases for each library
def get_releases_for_library(library_id):
    query = """
    MATCH (lib:Artifact {id: $library_id})-[:relationship_AR]->(release:Release)
    RETURN release.version AS version, release.timestamp AS release_date
    ORDER BY release_date
    """
    with driver.session() as session:
        result = session.run(query, library_id=library_id)
        releases = [{"version": record["version"], "release_date": record["release_date"]} for record in result]
    return releases

# Count dependencies for each release of a library
def get_dependency_count(library_id, release_version):
    query = """
    MATCH (lib:Artifact {id: $library_id})-[:relationship_AR]->(release:Release {version: $release_version})
           -[dep:dependency]->(depLib:Artifact)
    RETURN count(dep) AS dependency_count
    """
    with driver.session() as session:
        result = session.run(query, library_id=library_id, release_version=release_version)
        dependency_count = result.single()["dependency_count"]
    return dependency_count

# Collect data for RQ1
def collect_dependency_data():
    # Initialize CSV file with headers
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Library", "Version", "Release_Date", "Dependency_Count"])

    print("Fetching all libraries...")
    libraries = get_all_libraries()
    total_libraries = len(libraries)

    for idx, library in enumerate(libraries, start=1):
        print(f"Processing library {idx}/{total_libraries}: {library}")

        
        releases = get_releases_for_library(library)
        
        data = []
        
        for release in releases:
            version = release["version"]
            release_date = release["release_date"]
            dependency_count = get_dependency_count(library, version)
            
            data.append([library, version, release_date, dependency_count])

        with open(OUTPUT_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    print(f"Data collection completed and saved to {OUTPUT_FILE}")


collect_dependency_data()

# Close the Neo4j driver
driver.close()
