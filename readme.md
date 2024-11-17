# Setup Goblin dataset and weaver docker

This directory allows you to set up the [Maven Central Neo4j database](https://zenodo.org/records/11104819) and the [Weaver API](https://github.com/Goblin-Ecosystem/goblinWeaver) easily using Docker.

## Fisrt launch
To run it for the first time, use the command:
```
docker-compose up --build
```

On first launch, Docker will download the database dump, which may take some time.

## Second launch
To run it after the first time, use the command:
```
docker-compose up
```

The data is thus persistent.

## Accessibility

**Neo4j user**: neo4j

**Neo4j password**: Password1

- **Neo4j** will be accessible via http://localhost:7474 (web interface).
- **Weaver REST API** will be accessible via http://localhost:8080.
- **Weaver documentation** will be accessible via http://localhost:8080/swagger-ui/index.html


# Data for RQ1: Do libraries tend to use more dependencies than in the past?

For RQ1, the approach is to fetch all libraries, then for each library, retrieve its releases and count the number of dependencies for each release. Finally, we use the dependency counts for each library release to compare averages across different timeframes and observe changes in dependency usage over time.



## Collect dependencies data

### Setup virtual environment (Optional)

```bash
python -m venv .venv
source .venv/bin/activate
```


### Install Required Dependencies

```bash
pip install -r requirements.txt 
```

### Run Data Collection Script

```bash
python rq1_fetch_deps.py
```

Given the large database, the script may take several hours to complete. Once finished, it will generate a `dependency_data.csv` file in the `data` folder. Alternatively, you can download the pre-mined data [here](https://mega.nz/file/dIJADCzT#VOdYTl3_RDrQ9XgW-u4A8RAaPUsd6yCbx9uJKbi7idU).


## Analyze and Plot Dependency Trends

After collecting the data, use the following command to analyze and visualize dependency trends over time:

```bash
python rq1_dependency_trends.py 
```


### Plot average dependency count over time

![Plot average dependency count over time](rq1_figure1.png)

### Plot year-over-year percentage change in dependency count

![Plot year-over-year percentage change in dependency count](rq1_figure2.png)

### Box plot of dependency counts by year

![Box plot of dependency counts by year](rq1_figure3.png)