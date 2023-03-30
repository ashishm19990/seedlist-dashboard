# Seedlist Dashboard
Summary
-------
Internal dashboard for managing the seedlist

A seed is an email account that is added to email campaigns to track how well that campaign is being delivered to the inbox. Inboxable utilizes hundreds of seed accounts, and this dashboard indicated the health of each seed as well as provides tools for correcting common problems.

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

Folder Structure Conventions
============================

### A typical top-level directory layout

    .
    ├── build                   # Compiled files
    ├── patches                 # Webpack patch file
    ├── public                  # Favicon
    ├── src                     # Source files
    │   ├── app                 # Root component
    │   ├── components          # Subcomponents
    │   ├── style               # Scss files
    │   ├── templates           # Html files
    │   ├── tests               # Unit tests
    │   ├── utils               # Utility files
    │   └── views               # View files
    └── README.md

Notes:

* Files js and css will be compiled at `/public/build` folder
