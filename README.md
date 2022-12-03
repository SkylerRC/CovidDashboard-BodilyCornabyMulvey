# CovidDashboard-BodilyCornabyMulvey

This project is for the Programming for Engineers course at the University of Utah (fall 2022 semester).
The collaborators are Braden Mulvey, Skyler Cornaby, and Preston Bodily.

This project is an interactive dashboard designed to support the visualization of coronavirus-related data.
  - It allows users to compare the numbers between multiple countries.
  - Users can view both static and dynamic graphs.
  - Users can query the system for specific countries if desired.
  - The main scope will be to focus on visualizing death rates, but may be expanded if necessary.

  To run, you must install requests and beautifulsoup4. Do this thorugh your terminal using pip. Then open the main function, ensuring that the ScrapeWebsite module and the input file, scrapecountries.txt are in the same directory as your main. Then run the main in your favorite python IDE. A directory called Covid_Data will be created in that directory, which stores the Excel and JSON data for each day of scraping.

  Current implementation uses Worldometer for scraping statistics because it has more robust data. In order to limit the number of requests, the current iteration also only has 25 country names in the scrapecountires.txt file. You may add or reomve countries from this text file in order to scrape the information you really want.
