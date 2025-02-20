## Destinations Catalogue - my personal Django Web Project

<!-- This repository contains the code for my awesome project. Check out the http://destinations-catalogue.eu/ to see it in action! -->


<img src="https://github.com/GalkaKG/Destinations_Catalogue/blob/main/images_for_github/destinations_catalogue_home.png" alt="Project image" style="width: 700px"/>

<h3> Table of Contents </h3>
<ul>
  <li>Features</li>
  <li>Installation</li>
  <li>Technologies Used</li>
  <li>Demo</li>
  <li>License</li>
  <li>More pictures</li>
</ul>

<h2> Features </h2>
<ul>
  <li>User authentication and registration</li>
  <li>Browse and search for destinations</li>
  <li>Add, edit, and delete destinations</li>
  <li>User-friendly interface with a responsive design</li>
</ul>

<h2> Installation </h2>
<ol>
  <li>Clone the repository: <br/>git clone https://github.com/GalkaKG/Destinations_Catalogue.git </li>
  <li>Set up a virtual environment (optional, but recommended) <br/>pip install virtualenv<br/>cd Destinations_Catalogue<br/>python -m virtualenv venv
  <br/>- On Windows:<br/>venv\Scripts\activate<br/>- On macOS and Linux:<br/>source venv/bin/activate
  <li>Install project dependencies: <br /> pip install -r requirements.txt
  </li>
  <li>Set up environment variables</li>
  <li> Apply database migrations: <br /> python manage.py makemigrations <br/ > python manage.py migrate
  </li>
  <li>Create a superuser (optional) <br /> python manage.py createsuperuser </li>
  <li>Run the development server: <br />python manage.py runserver</li>
</ol>
<h3><strong>Important:</strong> Before running the project, you need to set up the database with initial data. To do this, upload the file data-db.sql to the Docker PostgreSQL container under "Files" and then execute the following command in the Docker terminal:</h3>
    <p> psql -h localhost -p 5432 -U postgres-user -d destinations_catalogue_db -f data-db.sql</p>
<p>You may need to run this command two or three times until there is data in the table "explore_attraction".</p>

<h2> Technologies Used </h2>
<ul>
  <li>Django</li>
  <li>HTML, CSS, JavaScript</li>
  <li>PostgreSQL </li>
  <li>Google Maps API</li>
  <li>SMTP server for sending password reset emails</li>
</ul>

<h2> Demo </h2>

<h2> License </h2>
<ul>
  <li>MIT License</li>
</ul>

<h2> More pictures: </h2>
<img src="https://github.com/GalkaKG/Destinations_Catalogue/blob/main/images_for_github/localhost_8000_explore_.png" />
<img src="https://github.com/GalkaKG/Destinations_Catalogue/blob/main/images_for_github/localhost_8000_catalogue_.png" />
<img src="https://github.com/GalkaKG/Destinations_Catalogue/blob/main/images_for_github/Screenshot%202023-07-25%20085603.png" />
<img src="https://github.com/GalkaKG/Destinations_Catalogue/blob/main/images_for_github/Screenshot%202023-07-24%20191909.png" />
<img src="https://github.com/GalkaKG/Destinations_Catalogue/blob/main/images_for_github/Screenshot%202023-07-24%20191942.png" />
<img src="https://github.com/GalkaKG/Destinations_Catalogue/blob/main/images_for_github/Screenshot%202023-07-24%20192006.png" />

