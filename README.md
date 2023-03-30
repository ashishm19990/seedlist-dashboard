# Seedlist Dashboard
Summary
-------
Internal dashboard for managing the seedlist

A seed is an email account that is added to email campaigns to track how well that campaign is being delivered to the inbox. Inboxable utilizes hundreds of seed accounts, and this dashboard indicated the health of each seed as well as provides tools for correcting common problems.

Frontend
============

Prerequisites
-------
Node.js (v18.12.1), npm (8.19.2)

Installation
============
* Clone the repository

* Install node dependencies
    ```sh
    $ npm install
    ```

* Build application
    ```sh
    $ npm run build 
    ```

* Start server locally
    ```sh
    $ npm run start
    ```

Configurations
============

To change configurations, update `src/utils/env.js` file.

## Project Structure
====================
```
.
├── README.md
├── frontend
│   ├── README.md
│   └── ...
├── backend
│   ├── README.md
│   ├── libs
│   └── projects
└── terraform
```

`/frontend`

Code and custom libraries for frontend code lives in this folder.

`/backend`

Code and custom libraries for backend code lives in this folder.

`/terraform`

Infrastucture-as-code definitions live in this folder.
