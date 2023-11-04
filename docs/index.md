# Project Layout

For full documentation visit [my GitHub repo](https://github.com/felipesebben/workshop-structure).

## Workflow



```mermaid
---
title: Project Worfklow
---
flowchart TD

id1[(Excel files)] --> id2(Extract) --> id3(Transform) --> id4(Load) --> id5([Concatenated Excel File])

```


# Function that tranforms the data #

### ::: app.pipeline.extract.extract_from_excel
