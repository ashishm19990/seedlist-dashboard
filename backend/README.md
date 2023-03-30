# Backend

## What is this ?

This portion of the repository contains all backend code.



## Generate new project

```bash
cd apps/backend/projects
cd {new project name}
```


## Project Structure

```
.
├── README.md
├── libs
│   ├── lib-one
│   └── lib-two
├── projects
│   ├── project-one
│   └── project-two

```

`/projects`

Project code (Python modules) go here.
Each project has its own dependencies.
One Project can not use other project as dependency

`/libs`
Each lib specifies its dependencies.
Each lib has its own dependencies.
Each lib can use other lib as a dependency.
